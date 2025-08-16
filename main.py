import argparse
import os
import sys

from file_searcher.search import search_by_extension, search_by_name


def main():
    try:
        parser = argparse.ArgumentParser(
            description="Search files by extension or name"
        )
        parser.add_argument("directory", help="Directory to search in ")
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument(
            "-e",
            "--extension",
            nargs="+",
            help="Search files by extension(s) (e.g., .txt)",
        )
        group.add_argument("-n", "--name", help="Search files by name (e.g., report)")

        args = parser.parse_args()

        if not os.path.isdir(args.directory):
            print(f"\nError: The directory '{args.directory}' does not exist\n")
            sys.exit(1)

        if args.extension:
            results = search_by_extension(args.directory, args.extension)
        else:
            results = search_by_name(args.directory, args.name)

        if results:
            print("Found files: ")
            for path in results:
                print(f"- {path}")
        else:
            print("⚠️ No files were found that match your criteria.")
            print("   ➤ Try using a different extension or name.")

    except KeyboardInterrupt:
        print("\n⛔ Operation cancelled by the user.")
        sys.exit(1)
    except Exception as e:
        print("An Unexpected error ocurred:")
        print(f"    {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
