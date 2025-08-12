# Small Calendar

A simple command-line calendar tool written in Python that displays yearly calendars in a condensed format.

## Features

- **Yearly Calendar View** - Shows entire year in condensed format with days as rows and months as columns
- **Multi-Year Display** - Display multiple years at once
- **Vertical/Horizontal Layout** - Choose between horizontal (default) or vertical calendar layout
- **Enhanced Vertical Display** - `--Vertical` option provides compact vertical layout with integrated year labels
- **Flexible Date Highlighting** - Highlight today's date, a specific date, or no date at all
- **First Day Indicators** - Shows first day of each month with month abbreviations
- **Week Starting on Sunday** - Follows US calendar convention with weeks starting on Sunday
- **No External Dependencies** - Uses only Python standard library modules

## Installation

```bash
git clone https://github.com/dpatru/small_calendar.git
cd small_calendar
```

**Note:** No external dependencies required. This project uses only Python standard library modules.

## Usage

```bash
# Show yearly view for current year (default)
python3 small_calendar.py

# Show yearly view for specific year
python3 small_calendar.py --year 2024

# Show multiple years starting from specific year
python3 small_calendar.py --year 2024 --number 3

# Show current year
python3 small_calendar.py --current

# Display calendar vertically (weeks as rows, weekdays as columns)
python3 small_calendar.py --vertical

# Display calendar vertically with enhanced formatting (compact layout)
python3 small_calendar.py --Vertical

# Highlight today's date
python3 small_calendar.py --mark-date

# Highlight a specific date
python3 small_calendar.py --mark-date 2024-06-15

# Combine options
python3 small_calendar.py --year 2024 --number 2 --Vertical --mark-date 2024-12-25
```

## Command-Line Options

- `--year, -y`: Specify start year for calendar display
- `--number, -n`: Number of years to display (use with --year to specify start year, default: 1)
- `--current, -c`: Show current year (explicit)
- `--vertical, -v`: Display calendar vertically (weeks as rows) with year labels to the left of the calendar
- `--Vertical, -V`: Display calendar more vertically, with year label aligned with calendar.
- `--mark-date [DATE]`: Highlight a date (no argument = today's date, with DATE = specific date in YYYY-MM-DD format)

## Examples

```bash
# Show yearly view for current year (default)
python3 small_calendar.py

# Show yearly view for 2024
python3 small_calendar.py --year 2024

# Show 3 years starting from 2024
python3 small_calendar.py --year 2024 --number 3

# Show current year in vertical layout
python3 small_calendar.py --vertical

# Show current year in enhanced vertical layout (compact)
python3 small_calendar.py --Vertical

# Show 2024-2026 in enhanced vertical layout
python3 small_calendar.py --year 2024 --number 3 --Vertical

# Highlight today's date
python3 small_calendar.py --mark-date

# Highlight Christmas 2024
python3 small_calendar.py --year 2024 --mark-date 2024-12-25

# Highlight a specific date in current year
python3 small_calendar.py --mark-date 2024-06-15

# No highlighting (default behavior)
python3 small_calendar.py --year 2024
```

## Calendar Display Format

The calendar displays in a condensed yearly format where:
- **Rows** represent days of the week (Sunday through Saturday)
- **Columns** represent months
- **Symbols** indicate:
  - `*` - Highlighted date (when using `--mark-date`)
  - `X`, `J`, `F`, `M`, `A`, `M`, `J`, `J`, `A`, `S`, `O`, `N`, `D` - First day of each month
  - `.` - Regular days

**Date Highlighting Options:**
- **No highlighting**: Default behavior when no `--mark-date` is used
- **Highlight today**: Use `--mark-date` without arguments
- **Highlight specific date**: Use `--mark-date YYYY-MM-DD`

**Vertical Display Modes:**
- **`--vertical`**: Standard vertical layout with year labels above the calendar
- **`--Vertical`**: Enhanced vertical layout with year labels integrated into the calendar columns for a more compact display

## Requirements

- Python 3.6+
- No external packages required (uses only standard library)

## License

MIT License 