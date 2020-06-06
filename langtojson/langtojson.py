import json
import re
from typing import TextIO, Dict

re_exp = re.compile(r'^(?P<name>.+)=(?P<localized>.+)$', re.MULTILINE)


def parse_lang_file(file: TextIO) -> Dict[str, str]:
    """
    Parse .lang file
    """
    result = {}

    line = file.readline()
    while line:
        match = re_exp.match(line)

        if match:
            name = match.group("name")
            localized = match.group("localized")
            result[name] = localized

        line = file.readline()

    return result


def write_to_json(data: Dict[str, str], file: TextIO):
    """
    Write data to json file
    """
    json.dump(data, file, indent=2, ensure_ascii=False)
