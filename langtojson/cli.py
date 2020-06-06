"""Console script for langtojson."""
import sys
from pathlib import Path
from typing import Tuple, TextIO, List

import click

from .langtojson import parse_lang_file, write_to_json


def validate_input(ctx: click.core.Context, param: click.core.Argument, values: Tuple[TextIO]):
    res = []
    for file in values:
        path = Path(file.name)
        if path.suffix != ".lang":
            raise click.BadParameter("file must have .lang extension")
        res.append((file, path))

    return res


@click.command()
@click.argument("files", type=click.File("r", encoding="utf-8"), nargs=-1, callback=validate_input)
def main(files: List[Tuple[TextIO, Path]]):
    """Console script for langtojson."""
    for infile, path in files:
        data = parse_lang_file(infile)

        new_path = path.with_suffix(".json")
        with new_path.open("w", encoding="utf-8") as outfile:
            write_to_json(data, outfile)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
