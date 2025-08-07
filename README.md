# Small Calendar

A simple command-line calendar tool written in Python.

## Features

- Display monthly calendar view
- Navigate between months and years
- Highlight current date
- Simple and clean interface

## Installation

```bash
git clone https://github.com/yourusername/small_calendar.git
cd small_calendar
pip install -r requirements.txt
```

## Usage

```bash
python3 small_calendar.py
```

Or with specific month/year:

```bash
python3 small_calendar.py --month 12 --year 2024
```

## Options

- `--month`: Specify month (1-12)
- `--year`: Specify year
- `--current`: Show current month (default)

## Examples

```bash
# Show current month
python3 small_calendar.py

# Show December 2024
python3 small_calendar.py --month 12 --year 2024

# Show March 2023
python3 small_calendar.py --month 3 --year 2023
```

## License

MIT License 