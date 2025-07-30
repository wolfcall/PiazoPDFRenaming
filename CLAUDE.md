# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a minimal Python project called "PiazoPDFProcessor" that currently contains only a basic main.py file with a simple entry point structure. The project appears to be in its initial stages with just a skeleton implementation.

## Commands

### Running the Application
```bash
python main.py <file1>
```
The main script expects one command-line argument (file1) but currently doesn't process it.

### Development Commands
Since this is a minimal Python project without dependencies or configuration files, standard Python commands apply:
- `python main.py` - Run the main script (requires one argument)
- `python -m py_compile main.py` - Check syntax
- `python -c "import py_compile; py_compile.compile('main.py', doraise=True)"` - Compile check with error reporting

## Architecture

### Current Structure
- `main.py` - Entry point with basic argument handling structure
  - Contains a `main()` function that accepts one command-line argument
  - Currently incomplete implementation (returns 0 without processing)

### Key Points
- The project name suggests PDF processing functionality, but no PDF-related code exists yet
- The code structure follows standard Python conventions with `if __name__ == "__main__"` pattern
- No external dependencies, configuration files, or package structure present
- No tests, documentation, or build configuration detected