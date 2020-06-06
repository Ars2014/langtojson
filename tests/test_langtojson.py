#!/usr/bin/env python

"""Tests for `langtojson` package."""
import json

from click.testing import CliRunner

from langtojson import cli


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("test.lang", "w") as f:
            f.write("text1=2\n" +
                    "text2=3")

        result = runner.invoke(cli.main, ["test.lang"])

        with open("test.json", "r") as f:
            parsed = json.load(f)

        assert parsed["text1"] == "2"
        assert parsed["text2"] == "3"
