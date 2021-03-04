#!/usr/bin/python
import os
import pathlib
import argparse
from datetime import datetime

DOWNLOADS = "~/Downloads"


def main():
    parser = argparse.ArgumentParser(
        description="Sort the Downloads directory by year and month"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not actually move the files, just print where they would be moved to.",
    )
    args = parser.parse_args()

    downloads = os.path.expanduser(DOWNLOADS)

    for entry in os.listdir(downloads):
        try:
            int(entry)
            print("Skipping", entry)
            continue
        except ValueError:
            pass

        path = pathlib.Path(os.path.join(downloads, entry))
        stat = path.stat()
        mtime = datetime.fromtimestamp(stat.st_mtime)

        year = str(mtime.year)
        month = mtime.strftime("%m. %B")

        new_dir = os.path.join(downloads, year, month)
        pathlib.Path(new_dir).mkdir(parents=True, exist_ok=True)
        new_path = os.path.join(new_dir, entry)

        print(path, "->", new_path)
        if not args.dry_run:
            os.rename(path, new_path)


if __name__ == "__main__":
    main()
