# Office Math Markup Language (OMML) Guide for Editable Word Equations

Microsoft Word (.docx) documents represent native mathematical equations using **Office Math Markup Language (OMML)**, standardized under ISO/IEC 29500 (OpenXML). Unlike static images or legacy OLE objects, OMML equations can be clicked and edited directly within Word's native Equation Editor.

---

## 1. Technical Architecture of OMML Conversion

```
[LaTeX Equation: \frac{a}{b}]
              │
              ▼ (via latex2mathml)
[MathML XML: <math><mfrac><mi>a</mi><mi>b</mi></mfrac></math>]
              │
              ▼ (via MML2OMML.XSL & lxml XSLT engine)
[OMML XML: <m:oMath><m:f><m:num><m:r><m:t>a</m:t>...</m:f></m:oMath>]
              │
              ▼ (via python-docx OxmlElement insertion)
[Native Editable Word Equation in Document Tree]
```

### Core XML Elements:
* `<m:oMath>`: The root container for an inline or display math expression.
* `<m:oMathPara>`: The paragraph wrapper that centers and spaces a standalone display equation block.
* `<m:f>`: A fraction container (`<m:num>` for numerator, `<m:den>` for denominator).
* `<m:sSup>`: A superscript container.
* `<m:sSub>`: A subscript container.
* `<m:rad>`: A radical / square root container.
* `<m:nary>`: An n-ary operator (summation $\sum$, integral $\int$, product $\prod$).

---

## 2. LaTeX Writing Guidelines for Flawless Word Conversion

To ensure clean OMML conversion:

1. **Greek Letters and Math Symbols:**
   * Use standard LaTeX commands: `\alpha`, `\beta`, `\theta`, `\pi`, `\sigma`, `\Omega`, `\mathbb{E}`, `\mathbb{V}`, `\sum`, `\int`, `\prod`.
2. **Fractions and Roots:**
   * Use `\frac{numerator}{denominator}` and `\sqrt{expression}`.
3. **Subscripts and Superscripts:**
   * Always wrap multi-character indices in braces: `x_{ij}`, `\hat{\theta}_{(-k)}`, `\pi_{2i|1}`.
4. **Delimiters:**
   * Use `\left(` and `\right)` or `\left[` and `\right]` to produce properly scaling brackets in Word.
5. **Display vs. Inline:**
   * Put major theorems and formulas on their own lines between `$$...$$` for centered display formatting.
   * Put inline variables and expressions between `$...$` inside paragraph text.

---

## 3. Verifying Equation Editability in Microsoft Word

When you open the resulting `.docx` file in Microsoft Word:
1. Click on any equation.
2. Word will immediately highlight the formula with a blue outline and reveal the **Equation** tab in the ribbon.
3. You can edit variables, change exponents, add fractions, or copy the equation in linear or professional format.
