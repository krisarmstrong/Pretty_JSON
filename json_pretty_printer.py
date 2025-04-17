#!/usr/bin/env python3
"""
Project Title: JsonPrettyPrinter

Formats JSON files with proper indentation and writes to an output file.

Author: Kris Armstrong
"""
import argparse
import json
import logging
import sys
from logging.handlers import RotatingFileHandler
from typing import Any

__version__ = "1.0.1"

class Config:
    """Global constants for JsonPrettyPrinter."""
    LOG_FILE: str = "json_pretty_printer.log"
    ENCODING: str = "utf-8"

def setup_logging(verbose: bool, logfile: str = Config.LOG_FILE) -> None:
    """Configure logging with rotating file handler.

    Args:
        verbose: Enable DEBUG level logging if True.
        logfile: Path to log file.

    Raises:
        PermissionError: If log file cannot be written.
    """
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            RotatingFileHandler(logfile, maxBytes=1048576, backupCount=3),
            logging.StreamHandler(),
        ],
    )

def parse_args() -> argparse.Namespace:
    """Parse command-line arguments.

    Returns:
        Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Format JSON files with proper indentation.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("input_file", help="Input JSON file")
    parser.add_argument("output_file", help="Output formatted JSON file")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")
    parser.add_argument("--logfile", default=Config.LOG_FILE, help="Log file path")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser.parse_args()

def format_json(input_file: str, output_file: str) -> None:
    """Read JSON file, format with indentation, and write to output file.

    Args:
        input_file: Path to input JSON file.
        output_file: Path to output formatted JSON file.

    Raises:
        FileNotFoundError: If input file doesn't exist.
        PermissionError: If files cannot be read/written.
        json.JSONDecodeError: If JSON is invalid.
    """
    logging.info("Formatting JSON file: %s", input_file)
    try:
        with open(input_file, "r", encoding=Config.ENCODING) as f:
            json_object: Any = json.load(f)
        logging.debug("JSON object loaded successfully")
    except FileNotFoundError as e:
        logging.error("Input file not found: %s", input_file)
        raise
    except PermissionError as e:
        logging.error("Cannot read input file %s: %s", input_file, e)
        raise
    except json.JSONDecodeError as e:
        logging.error("Invalid JSON in input file: %s", e)
        raise
    except Exception as e:
        logging.error("Error reading JSON file: %s", e)
        raise

    try:
        formatted_json = json.dumps(json_object, indent=2)
        with open(output_file, "w", encoding=Config.ENCODING) as f:
            f.write(formatted_json)
        logging.info("Formatted JSON written to %s", output_file)
    except PermissionError as e:
        logging.error("Cannot write to output file %s: %s", output_file, e)
        raise
    except Exception as e:
        logging.error("Error writing formatted JSON: %s", e)
        raise

def main() -> int:
    """Main entry point for JsonPrettyPrinter.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    args = parse_args()
    setup_logging(args.verbose, args.logfile)

    # Validate file extensions
    if not args.input_file.lower().endswith(".json"):
        logging.error("Input file must have .json extension")
        return 1
    if not args.output_file.lower().endswith(".json"):
        logging.error("Output file must have .json extension")
        return 1

    try:
        format_json(args.input_file, args.output_file)
        return 0
    except KeyboardInterrupt:
        logging.info("Cancelled by user")
        return 0
    except Exception as e:
        logging.error("Error: %s", e)
        return 1

if __name__ == "__main__":
    sys.exit(main())