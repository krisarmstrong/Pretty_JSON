#!/usr/bin/env python3
"""
Tests for JsonPrettyPrinter.
"""
import json
import os
import pytest
from json_pretty_printer import __version__, format_json

@pytest.fixture
def json_file(tmp_path):
    """Create a temporary JSON file."""
    input_path = tmp_path / "input.json"
    output_path = tmp_path / "output.json"
    data = {"key": "value", "nested": {"a": 1, "b": 2}}
    with open(input_path, "w") as f:
        json.dump(data, f)
    return input_path, output_path

def test_version() -> None:
    """Test version format."""
    assert __version__ == "1.0.1"

def test_format_json(json_file) -> None:
    """Test formatting a JSON file."""
    input_path, output_path = json_file
    format_json(str(input_path), str(output_path))

    with open(output_path, "r") as f:
        formatted = f.read()
    expected = '{\n  "key": "value",\n  "nested": {\n    "a": 1,\n    "b": 2\n  }\n}'
    assert formatted == expected

def test_format_json_invalid_file() -> None:
    """Test formatting an invalid JSON file."""
    with pytest.raises(FileNotFoundError):
        format_json("nonexistent.json", "output.json")

def test_format_json_invalid_json(tmp_path) -> None:
    """Test formatting a file with invalid JSON."""
    input_path = tmp_path / "invalid.json"
    with open(input_path, "w") as f:
        f.write("{invalid json}")
    with pytest.raises(json.JSONDecodeError):
        format_json(str(input_path), str(tmp_path / "output.json"))