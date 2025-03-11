import os
import argparse
from .converter import LatexToPngConverter


def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description="Convert LaTeX equations to PNG images")
    parser.add_argument("input", nargs="?", help="Input file with LaTeX expressions or a single expression")
    parser.add_argument("--output-dir", "-o", help="Directory to save output images")
    parser.add_argument("--dpi", type=int, help="DPI for output images", default=300)
    parser.add_argument("--font-size", type=int, help="Font size for equations", default=14)
    parser.add_argument("--transparent", action="store_true", help="Make background transparent")
    parser.add_argument("--padding", type=int, help="Padding around equations in pixels", default=10)
    parser.add_argument("--prefix", help="Filename prefix for equations", default="equation_")

    args = parser.parse_args()

    # Get default config first
    config = LatexToPngConverter.default_config()

    # Update with command line arguments
    config.update(
        {
            "dpi": args.dpi,
            "font_size": args.font_size,
            "transparent": args.transparent,
            "padding": args.padding,
            "filename_prefix": args.prefix,
        }
    )

    if args.output_dir:
        config["output_dir"] = args.output_dir

    converter = LatexToPngConverter(config)

    # Process input
    if not args.input:
        # Interactive mode
        print("Enter LaTeX expressions (one per line, empty line to finish):")
        expressions = []
        while True:
            try:
                line = input().strip()
                if not line:
                    break
                expressions.append(line)
            except EOFError:
                break

        if expressions:
            paths = converter.convert_batch(expressions)
            print(f"Generated {len(paths)} images:")
            for path in paths:
                print(f" - {path}")
    elif args.input.startswith("$") and args.input.endswith("$"):
        # Single expression mode with dollar signs
        path = converter.convert_single(args.input[1:-1])
        print(f"Generated image: {path}")
    elif os.path.isfile(args.input):
        # File input mode
        paths = converter.convert_from_file(args.input, args.output_dir)
        print(f"Generated {len(paths)} images:")
        for path in paths:
            print(f" - {path}")
    else:
        # Single expression mode without dollar signs
        path = converter.convert_single(args.input)
        print(f"Generated image: {path}")


if __name__ == "__main__":
    main()
