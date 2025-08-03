# Paizo PDF Processor

A Python utility for processing and renaming Paizo PDF files from uncompressed zip archives.

## Overview

This tool recursively searches through directories to find Paizo PDF files (identified by the pattern `PZO[0-9A-Z]{3,6}[ -]{0,1}.*`) and renames them to be more descriptive.

## Usage

```bash
python main.py <directory_path>
```

Where `<directory_path>` is the location containing zip files or extracted Paizo content.

## Requirements

- Python 3.x
- No external dependencies (uses only standard library modules)

## Features

- Recursive directory traversal
- Paizo product code detection using regex patterns
- Directory structure analysis
- Currently in development phase (prints analysis output)

## File Structure

- `main.py` - Main entry point and processing logic
- `CLAUDE.md` - Development guidance for AI assistants

## Development

To check syntax:
```bash
python -m py_compile main.py
```

To compile with error reporting:
```bash
python -c "import py_compile; py_compile.compile('main.py', doraise=True)"
```

## Note

This project is currently in development. The tool analyzes and identifies Paizo files but does not yet perform actual file renaming operations.