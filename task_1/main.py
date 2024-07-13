"""Module for recursively copying and sorting files by extension."""

import shutil
import argparse
from pathlib import Path

def parse_arguments():
    """
    Parse command line arguments.
    """
    parser = argparse.ArgumentParser(description='Recursively copy and sort files by extension.')
    parser.add_argument('src_dir', type=Path, help='Source directory')
    parser.add_argument('dst_dir', type=Path, nargs='?', default=Path('dist'), help='Destination directory (default: dist)')
    return parser.parse_args()

def copy_files_recursively(src_dir, dst_dir):
    """
    Recursively copies files from the source directory to the destination directory.
    Files are sorted by extension or placed in a 'no_extension' directory.
    """
    try:
        for item in src_dir.iterdir():
            src_path = src_dir / item

            if src_path.is_dir():
                # Recursion step
                copy_files_recursively(src_path, dst_dir)

            elif src_path.is_file():
                # Recursion base case

                # Get the file extension without the dot
                file_extension = src_path.suffix[1:]
                if not file_extension:  # Handle files without extension
                    file_extension = 'no_extension'

                ext_dir = dst_dir / file_extension
                ext_dir.mkdir(parents=True, exist_ok=True)
                dst_path = ext_dir / item.name
                shutil.copy2(src_path, dst_path)
    except OSError as e:
        print(f"Error while processing {src_dir}: {e}")

def main():
    """
    Main function parses args and copy files recursively.
    If dest dir is not provided, it will create a 'dist' directory
    in the current working directory.
    """
    args = parse_arguments()
    src_dir = args.src_dir
    dst_dir = args.dst_dir

    if dst_dir == Path('dist'):
        dst_dir = Path.cwd() / dst_dir

    if not src_dir.exists() or not src_dir.is_dir():
        print(f"Source {src_dir} does not exist or is not a directory.")
        return

    if dst_dir.exists() and not dst_dir.is_dir():
        print(f"Destination {dst_dir} is not a directory.")
        return

    if not dst_dir.exists():
        dst_dir.mkdir(parents=True)

    copy_files_recursively(src_dir, dst_dir)
    print(f"Files copied to {dst_dir}")

if __name__ == "__main__":
    main()