#!/usr/bin/env python3
"""
Academic DOCX Generator with Native Editable OMML Formulas
Converts academic Markdown or structured text with LaTeX equations into professional Microsoft Word (.docx) documents.
Equations are converted into native Office Math Markup Language (OMML) so they can be clicked and edited directly in Word's Equation Editor.
"""

import sys
import os
import re
from typing import List, Tuple, Optional

import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from lxml import etree
import latex2mathml.commands
from latex2mathml.converter import convert as latex2mathml_convert

# Find or resolve MML2OMML.XSL
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOCAL_XSL = os.path.join(SCRIPT_DIR, "MML2OMML.XSL")
SYSTEM_XSL = r"C:\Program Files\Microsoft Office\root\Office16\MML2OMML.XSL"

XSL_PATH = LOCAL_XSL if os.path.exists(LOCAL_XSL) else (SYSTEM_XSL if os.path.exists(SYSTEM_XSL) else None)
TRANSFORM = None

if XSL_PATH and os.path.exists(XSL_PATH):
    try:
        xslt_tree = etree.parse(XSL_PATH)
        TRANSFORM = etree.XSLT(xslt_tree)
    except Exception as e:
        sys.stderr.write(f"Warning: Failed to load MML2OMML.XSL from {XSL_PATH}: {e}\n")


def latex_to_omml(latex_code: str, is_display: bool = True) -> Optional[OxmlElement]:
    """Convert a LaTeX formula string to a native Word OMML XML element."""
    if not TRANSFORM:
        return None
    try:
        # Clean latex string
        clean_latex = latex_code.strip()
        if clean_latex.startswith("$$") and clean_latex.endswith("$$"):
            clean_latex = clean_latex[2:-2].strip()
        elif clean_latex.startswith("$") and clean_latex.endswith("$"):
            clean_latex = clean_latex[1:-1].strip()

        # Handle common macro edge cases
        clean_latex = clean_latex.replace(r"\mid", "|")
        clean_latex = clean_latex.replace(r"\mathbb", r"\mathbf")
        
        mathml_str = latex2mathml_convert(clean_latex)
        mathml_tree = etree.fromstring(mathml_str)
        omml_tree = TRANSFORM(mathml_tree)
        omml_root = omml_tree.getroot()
        
        # Convert lxml element to python-docx OxmlElement
        xml_string = etree.tostring(omml_root, encoding="utf-8").decode("utf-8")
        
        # If display equation, wrap in m:oMathPara if not already
        if is_display and "oMathPara" not in xml_string:
            xml_string = f'<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">{xml_string}</m:oMathPara>'
            
        element = parse_xml(xml_string)
        return element
    except Exception as e:
        sys.stderr.write(f"Notice: Failed to convert LaTeX formula '{latex_code[:30]}...': {e}\n")
        return None


def setup_document_styles(doc: Document):
    """Configure margins, typography, and spacing for professional academic presentation."""
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Base Normal style
    style = doc.styles["Normal"]
    font = style.font
    font.name = "Times New Roman"
    font.size = Pt(12)
    font.color.rgb = RGBColor(33, 33, 33)
    p_format = style.paragraph_format
    p_format.line_spacing = 1.15
    p_format.space_after = Pt(6)
    p_format.space_before = Pt(0)


def add_formatted_paragraph(doc: Document, text: str):
    """Parse paragraph text with inline LaTeX math ($...$) and inject OMML elements."""
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(6)

    # Match inline math: $...$
    pattern = re.compile(r'(\$[^\$\n]+?\$)')
    tokens = pattern.split(text)

    for token in tokens:
        if not token:
            continue
        if token.startswith("$") and token.endswith("$") and len(token) > 2:
            omml_elem = latex_to_omml(token, is_display=False)
            if omml_elem is not None:
                p._p.append(omml_elem)
            else:
                # Fallback to italicized text if conversion fails
                run = p.add_run(token[1:-1])
                run.italic = True
        else:
            # Add normal text runs, parsing markdown italics *text* if present
            italic_tokens = re.split(r'(\*[^\*\n]+?\*)', token)
            for it in italic_tokens:
                if it.startswith("*") and it.endswith("*") and len(it) > 2:
                    r = p.add_run(it[1:-1])
                    r.italic = True
                else:
                    p.add_run(it)


def add_display_equation(doc: Document, formula: str):
    """Add a centered, numbered or unnumbered display equation in native OMML."""
    omml_elem = latex_to_omml(formula, is_display=True)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(6)

    if omml_elem is not None:
        p._p.append(omml_elem)
    else:
        # Fallback text representation
        clean = formula.strip().strip("$").strip()
        run = p.add_run(clean)
        run.italic = True
        run.font.name = "Cambria Math"


def add_markdown_table(doc: Document, table_lines: List[str]):
    """Convert markdown table lines into a styled Word table."""
    rows_data = []
    for line in table_lines:
        line = line.strip()
        if not line or line.startswith("|---") or line.startswith("|:--") or line.startswith("|-"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows_data.append(cells)

    if not rows_data:
        return

    num_rows = len(rows_data)
    num_cols = max(len(r) for r in rows_data)

    table = doc.add_table(rows=num_rows, cols=num_cols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True

    for r_idx, row in enumerate(rows_data):
        for c_idx, val in enumerate(row):
            if c_idx < num_cols:
                cell = table.cell(r_idx, c_idx)
                cell.text = val
                cell_p = cell.paragraphs[0]
                cell_p.paragraph_format.space_after = Pt(2)
                cell_p.paragraph_format.space_before = Pt(2)
                
                # Header row styling
                if r_idx == 0:
                    shading = parse_xml(r'<w:shd {} w:fill="F2F2F2"/>'.format(nsdecls('w')))
                    cell._tc.get_or_add_tcPr().append(shading)
                    for run in cell_p.runs:
                        run.font.bold = True
                        run.font.size = Pt(10.5)
                else:
                    for run in cell_p.runs:
                        run.font.size = Pt(10)

    # Add spacing after table
    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_before = Pt(0)
    p_spacer.paragraph_format.space_after = Pt(4)


def convert_markdown_to_docx(markdown_content: str, output_path: str):
    """Main compilation pipeline converting markdown text to an academic .docx document."""
    doc = Document()
    setup_document_styles(doc)

    lines = markdown_content.splitlines()
    i = 0
    in_display_math = False
    display_math_buffer = []
    in_table = False
    table_buffer = []

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Handle display math block $$ ... $$
        if stripped.startswith("$$"):
            if stripped.endswith("$$") and len(stripped) > 2:
                # Single line display math
                add_display_equation(doc, stripped)
                i += 1
                continue
            elif not in_display_math:
                in_display_math = True
                display_math_buffer = [stripped[2:]]
                i += 1
                continue
            else:
                in_display_math = False
                display_math_buffer.append(stripped[:-2])
                formula_text = " ".join(display_math_buffer)
                add_display_equation(doc, formula_text)
                display_math_buffer = []
                i += 1
                continue

        if in_display_math:
            if stripped.endswith("$$"):
                in_display_math = False
                display_math_buffer.append(stripped[:-2])
                formula_text = " ".join(display_math_buffer)
                add_display_equation(doc, formula_text)
                display_math_buffer = []
            else:
                display_math_buffer.append(stripped)
            i += 1
            continue

        # Handle Markdown tables
        if stripped.startswith("|") and stripped.endswith("|"):
            in_table = True
            table_buffer.append(stripped)
            i += 1
            continue
        elif in_table:
            in_table = False
            add_markdown_table(doc, table_buffer)
            table_buffer = []
            # Do not increment i, let current line be evaluated

        # Blank lines
        if not stripped:
            i += 1
            continue

        # Headings
        if stripped.startswith("# "):
            h = doc.add_heading(stripped[2:].strip(), level=1)
            h.paragraph_format.space_before = Pt(14)
            h.paragraph_format.space_after = Pt(6)
            for r in h.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(16)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0, 0, 0)
        elif stripped.startswith("## "):
            h = doc.add_heading(stripped[3:].strip(), level=2)
            h.paragraph_format.space_before = Pt(12)
            h.paragraph_format.space_after = Pt(4)
            for r in h.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(14)
                r.font.bold = True
                r.font.color.rgb = RGBColor(30, 30, 30)
        elif stripped.startswith("### "):
            h = doc.add_heading(stripped[4:].strip(), level=3)
            h.paragraph_format.space_before = Pt(8)
            h.paragraph_format.space_after = Pt(2)
            for r in h.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(12)
                r.font.bold = True
                r.font.italic = True
                r.font.color.rgb = RGBColor(50, 50, 50)
        elif stripped.startswith("#### "):
            h = doc.add_heading(stripped[5:].strip(), level=4)
            h.paragraph_format.space_before = Pt(6)
            h.paragraph_format.space_after = Pt(2)
            for r in h.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(12)
                r.font.bold = True
                r.font.color.rgb = RGBColor(60, 60, 60)
        elif stripped.startswith("> "):
            # Blockquote
            bq_text = stripped[2:].strip()
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.5)
            p.paragraph_format.right_indent = Inches(0.5)
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(4)
            run = p.add_run(bq_text)
            run.italic = True
            run.font.size = Pt(11)
        else:
            # Standard paragraph
            add_formatted_paragraph(doc, stripped)

        i += 1

    if in_table and table_buffer:
        add_markdown_table(doc, table_buffer)

    doc.save(output_path)
    print(f"Academic DOCX successfully created: {os.path.abspath(output_path)}")


def main():
    if len(sys.argv) < 3:
        print("Usage: python generate_academic_docx.py <input_markdown_file> <output_docx_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        print(f"Error: Input file not found: {input_file}")
        sys.exit(1)

    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    convert_markdown_to_docx(content, output_file)


if __name__ == "__main__":
    main()
