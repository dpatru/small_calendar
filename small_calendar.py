#!/usr/bin/env python3
"""
Small Calendar - A simple command-line calendar tool
"""

import argparse
import calendar
import sys
from datetime import datetime, date


def display_calendar(year, month):
    """Display a formatted calendar for the specified month and year."""
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    
    # Header
    print(f"\n{month_name} {year}")
    print("=" * 30)
    print("Mon  Tue  Wed  Thu  Fri  Sat  Sun")
    print("-" * 30)
    
    # Get current date for highlighting
    today = date.today()
    current_year = today.year
    current_month = today.month
    current_day = today.day
    
    # Display calendar
    for week in cal:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "     "
            else:
                # Highlight current date
                if (year == current_year and 
                    month == current_month and 
                    day == current_day):
                    week_str += f"[{day:2d}] "
                else:
                    week_str += f" {day:2d}  "
        print(week_str.rstrip())
    
    print("-" * 30)


def main():
    """Main function to handle command-line arguments and display calendar."""
    parser = argparse.ArgumentParser(
        description="Display a simple calendar for a specific month and year"
    )
    parser.add_argument(
        "--month", "-m",
        type=int,
        help="Month (1-12)",
        choices=range(1, 13)
    )
    parser.add_argument(
        "--year", "-y",
        type=int,
        help="Year (e.g., 2024)"
    )
    parser.add_argument(
        "--current", "-c",
        action="store_true",
        help="Show current month (default)"
    )
    
    args = parser.parse_args()
    
    # Get current date if no arguments provided
    now = datetime.now()
    
    if args.current or (args.month is None and args.year is None):
        # Show current month
        year = now.year
        month = now.month
    else:
        # Use provided arguments, fallback to current for missing values
        year = args.year if args.year is not None else now.year
        month = args.month if args.month is not None else now.month
    
    # Validate year (reasonable range)
    if year < 1900 or year > 2100:
        print("Error: Year must be between 1900 and 2100")
        sys.exit(1)
    
    try:
        display_calendar(year, month)
    except Exception as e:
        print(f"Error displaying calendar: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 