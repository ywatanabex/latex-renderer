import os
import matplotlib.pyplot as plt
import matplotlib as mpl


class LatexToPngConverter:
    def __init__(self, config=None):
        self.config = config or self.default_config()
        self._setup_matplotlib()

    @staticmethod
    def default_config():
        return {
            "dpi": 300,
            "font_size": 14,
            "font_color": "black",
            "background_color": "white",
            "transparent": False,
            "padding": 10,  # pixels of padding around the equation
            "output_dir": "output",
            "filename_prefix": "equation_",
        }

    def _setup_matplotlib(self):
        # Configure matplotlib for high-quality rendering
        mpl.rcParams["mathtext.fontset"] = "cm"
        mpl.rcParams["font.size"] = self.config["font_size"]
        mpl.rcParams["text.color"] = self.config["font_color"]
        mpl.rcParams["figure.facecolor"] = self.config["background_color"]
        mpl.rcParams["savefig.transparent"] = self.config["transparent"]
        mpl.rcParams["savefig.dpi"] = self.config["dpi"]
        mpl.rcParams["savefig.bbox"] = "tight"
        mpl.rcParams["savefig.pad_inches"] = self.config["padding"] / self.config["dpi"]

    def convert_single(self, latex_expr, output_path=None):
        """Convert a single LaTeX expression to PNG"""
        # Create figure with transparent background if configured
        fig = plt.figure(figsize=(1, 1))

        # Handle multi-line equations (aligned environment)
        if r"\begin{aligned}" in latex_expr:
            # Extract the lines between \begin{aligned} and \end{aligned}
            content = latex_expr.replace(r"\begin{aligned}", "").replace(r"\end{aligned}", "")
            # Split lines and clean them
            lines = [line.strip() for line in content.split(r"\\") if line.strip()]
            # Remove alignment markers and create simple equations
            lines = [line.replace("&", "") for line in lines]
            latex_expr = r" \\ ".join(lines)

        # Render the equation
        plt.text(
            0.5,
            0.5,
            f"${latex_expr}$",
            horizontalalignment="center",
            verticalalignment="center",
            transform=fig.transFigure,
        )

        # Remove axes
        plt.axis("off")

        # Generate output path if not provided
        if output_path is None:
            os.makedirs(self.config["output_dir"], exist_ok=True)
            output_path = os.path.join(
                self.config["output_dir"], f"{self.config['filename_prefix']}{hash(latex_expr) % 10000}.png"
            )

        # Save the figure with a larger figure size for multi-line equations
        if r"\\" in latex_expr:
            fig.set_size_inches(8, 6)  # Adjust size for multi-line equations
        plt.savefig(output_path, bbox_inches="tight", pad_inches=self.config["padding"] / self.config["dpi"])
        plt.close(fig)

        return output_path

    def convert_batch(self, latex_expressions, output_paths=None):
        """Convert multiple LaTeX expressions to PNGs"""
        if output_paths is None:
            output_paths = [None] * len(latex_expressions)

        results = []
        for expr, path in zip(latex_expressions, output_paths):
            results.append(self.convert_single(expr, path))

        return results

    def convert_from_file(self, input_file, output_dir=None):
        """Read LaTeX expressions from a file and convert them"""
        if output_dir:
            self.config["output_dir"] = output_dir

        with open(input_file, "r") as f:
            content = f.read()

        # Split content by triple dashes (section separators)
        sections = content.split("---")
        expressions = []

        for section in sections:
            if not section.strip():
                continue

            # Remove comments and get the actual expression
            lines = [line.strip() for line in section.split("\n")]
            expr_lines = []
            in_equation = False

            for line in lines:
                if not line or line.startswith("#"):
                    continue

                if r"\begin{aligned}" in line:
                    in_equation = True
                    expr_lines.append(line)
                elif r"\end{aligned}" in line:
                    in_equation = False
                    expr_lines.append(line)
                elif in_equation or not any(marker in line for marker in ["#", "---"]):
                    expr_lines.append(line)

            if expr_lines:
                expressions.append(" ".join(expr_lines))

        return self.convert_batch(expressions)
