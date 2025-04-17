# JsonPrettyPrinter

Formats JSON files with proper indentation.

## Installation

```bash
git clone https://github.com/krisarmstrong/json-pretty-printer
cd json-pretty-printer
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python json_pretty_printer.py input.json output.json --verbose
```

- `input_file`: Input JSON file.
- `output_file`: Output formatted JSON file.
- `-v, --verbose`: Enable verbose logging.
- `--logfile`: Log file path (default: json_pretty_printer.log).

## Files

- `json_pretty_printer.py`: Main script.
- `version_bumper.py`: Version management tool.
- `tests/test_json_pretty_printer.py`: Pytest suite.
- `requirements.txt`: Dependencies.
- `CHANGELOG.md`: Version history.
- `LICENSE`: MIT License.
- `CONTRIBUTING.md`: Contribution guidelines.
- `CODE_OF_CONDUCT.md`: Contributor Covenant.

## GitHub Setup

```bash
gh repo create json-pretty-printer --public --source=. --remote=origin
git init
git add .
git commit -m "Initial commit: JsonPrettyPrinter v1.0.1"
git tag v1.0.1
git push origin main --tags
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

MIT License. See [LICENSE](LICENSE) for details.