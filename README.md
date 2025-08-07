# Small Calendar

A simple command-line calendar tool written in Python.

## Features

- Display yearly calendar view (default) - shows entire year in condensed format
- Display monthly calendar view
- Navigate between months and years
- Highlight current date and first day of each month
- Simple and clean interface

## Installation

```bash
git clone https://github.com/yourusername/small_calendar.git
cd small_calendar
pip install -r requirements.txt
```

## Usage

```bash
# Show yearly view (default)
python3 small_calendar.py

# Show specific year
python3 small_calendar.py --year 2024

# Show specific month
python3 small_calendar.py --month 12 --year 2024

# Show current month
python3 small_calendar.py --current
```

## Options

- `--year`: Specify year for yearly view
- `--month`: Specify month (1-12) for monthly view
- `--current`: Show current month
- `--yearly`: Show yearly view (default when no arguments provided)

## Examples

```bash
# Show yearly view for current year (default)
python3 small_calendar.py

# Show yearly view for 2024
python3 small_calendar.py --year 2024

# Show December 2024 (monthly view)
python3 small_calendar.py --month 12 --year 2024

# Show current month
python3 small_calendar.py --current
```

## License

MIT License 