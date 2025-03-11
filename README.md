# latex-renderer

[![PyPI version](https://badge.fury.io/py/latex-renderer.svg)](https://badge.fury.io/py/latex-renderer)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful Python tool to convert LaTeX mathematical equations into high-quality images using Matplotlib's mathtext engine. Perfect for creating equation images for presentations, documentation, or educational materials.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Command Line Options](#command-line-options)
  - [Input File Format](#input-file-format)
- [Supported LaTeX Syntax](#supported-latex-syntax)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features
- Convert single equations or batch process multiple equations
- Interactive mode for equation-by-equation conversion
- Customizable output settings (DPI, font size, padding)
- Support for transparent backgrounds
- File-based input processing
- Comprehensive LaTeX math syntax support

## Requirements
- Python 3.10 or higher
- Matplotlib
- Operating System: Windows, macOS, or Linux

## Installation

The easiest way to install `latex-renderer` is using pipx:

```bash
pipx install latex-renderer
```

Alternatively, you can install it using pip:

```bash
pip install latex-renderer
```

## Usage

The `latex-renderer` command can be used in several ways:

1. Convert a single equation:
```bash
latex-renderer "x^2 + y^2 = z^2"
```

2. Interactive mode (enter equations one by one):
```bash
latex-renderer
# Enter equations one per line, press Enter twice to finish
```

3. Convert equations from a file:
```bash
latex-renderer input.txt
```

### Command Line Options

- `--output-dir`, `-o`: Directory to save output images (default: `output/`)
- `--dpi`: DPI for output images (default: 300)
- `--font-size`: Font size for equations (default: 14)
- `--transparent`: Make background transparent
- `--padding`: Padding around equations in pixels (default: 10)
- `--prefix`: Filename prefix for equations (default: 'equation_')

Example with options:
```bash
latex-renderer "E = mc^2" --dpi 600 --font-size 16 --transparent -o images/
```

## Input File Format

When using a file as input, equations should be separated by triple dashes (`---`). Comments can be added using `#`:

```
# First equation
x^2 + y^2 = z^2
---
# Second equation with alignment
\begin{aligned}
a &= b + c \\
d &= e + f
\end{aligned}
---
# A more complex equation
\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
```

## Supported LaTeX Syntax

This tool uses Matplotlib's mathtext engine to render mathematical expressions. While it supports many common LaTeX commands, it's a subset of full LaTeX functionality. Here's what's supported:

### Basic Syntax
- Mathematical expressions must be enclosed in dollar signs: `$...$`
- To display a literal dollar sign, escape it with a backslash: `\$`

### Subscripts and Superscripts
- Use `_` for subscripts: `$x_1$`
- Use `^` for superscripts: `$x^2$`
- For multi-character sub/superscripts, use curly braces: `$x_{12}$`, `$x^{34}$`

### Fractions and Binomials
- Fractions: `\frac{numerator}{denominator}`
- Binomials: `\binom{n}{k}`
- Nested fractions are supported: `$\frac{1}{\frac{2}{3}}$`

### Greek Letters
Common Greek letters are supported:
- Lowercase: `\alpha`, `\beta`, `\gamma`, `\delta`, etc.
- Uppercase: `\Gamma`, `\Delta`, `\Theta`, `\Lambda`, etc.

### Mathematical Operators
- Sum: `\sum`
- Product: `\prod`
- Integral: `\int`
- Limits can be added using sub/superscripts: `$\sum_{i=1}^n$`

### Delimiters
- Parentheses: `(`, `)`
- Square brackets: `[`, `]`
- Curly braces: `\{`, `\}`
- Angle brackets: `\langle`, `\rangle`
- Use `\left` and `\right` for auto-sizing: `\left(\frac{1}{2}\right)`

### Relations and Operators
- Equality: `=`, `\neq`, `\approx`
- Inequalities: `<`, `>`, `\leq`, `\geq`
- Plus/minus: `\pm`
- Times: `\times`
- Division: `\div`

### Special Functions
- Trigonometric: `\sin`, `\cos`, `\tan`
- Logarithmic: `\log`, `\ln`
- Limits: `\lim`
- Square root: `\sqrt{x}` or `\sqrt[n]{x}` for nth root

### Accents
- Hat: `\hat{x}`
- Bar: `\bar{x}`
- Vector arrow: `\vec{x}`
- Dot: `\dot{x}`, `\ddot{x}`

Note: This is not a complete LaTeX implementation. Some advanced LaTeX features like environments (`align`, `matrix`, etc.), custom macros, or package-specific commands are not supported.

For more details, refer to the [Matplotlib mathtext documentation](https://matplotlib.org/stable/users/explain/text/mathtext.html).

## Examples

Here are some example outputs from latex-renderer:

1. Simple equation:
```bash
latex-renderer "E = mc^2" --transparent
```

2. Complex equation with fractions:
```bash
latex-renderer "\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}" --dpi 400
```

3. Multiple equations from a file:
```bash
latex-renderer equations.txt --output-dir math_images/ --font-size 16
```

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please make sure to update tests as appropriate and follow the existing coding style.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
