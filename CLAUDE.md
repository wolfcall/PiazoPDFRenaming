# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This project is intended to take uncompressed zip files from paizo and rename the files inside to be more descriptive.

## Commands

### Running the Application
```bash
python main.py <file1>
```
The main script expects one command-line argument which holds the location of the zip files and finds any paizo files to rename

### Development Commands
Since this is a minimal Python project without dependencies or configuration files, standard Python commands apply:
- `python main.py` - Run the main script (requires one argument)
- `python -m py_compile main.py` - Check syntax
- `python -c "import py_compile; py_compile.compile('main.py', doraise=True)"` - Compile check with error reporting

## Architecture

### Current Structure
- `main.py` - Entry point with directory traversal and PDF processing logic
  - `main()` - Entry point that validates directory input and calls directorySearch
  - `directorySearch(dirPath)` - Recursively traverses directories looking for PDF files
  - `processPDF(dirPath, item)` - Processes PDF files matching Paizo naming patterns

### Implementation Details
- Uses regex patterns to identify Paizo PDF files (format: `PZO[0-9A-Z]{3,6}[ -]{0,1}.*`)
- Recursively searches through directory structures using `os.listdir()`
- Currently in development phase - prints analysis output but doesn't perform actual file renaming yet
- Extracts Paizo product codes and analyzes directory naming patterns

### Key Points
- The code structure follows standard Python conventions with `if __name__ == "__main__"` pattern
- Uses standard library modules: `os`, `sys`, `re`
- No external dependencies, configuration files, or package structure present
- No tests, documentation, or build configuration detected