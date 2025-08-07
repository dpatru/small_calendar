#!/usr/bin/env python3
"""
Small Calendar - A simple command-line calendar tool
"""

import argparse
import calendar
import sys
from datetime import datetime, date


def display_yearly_calendar(year):
    """Display a condensed yearly calendar with 7 rows (days of week) and 52 columns (weeks)."""
    # Initialize the yearly grid: 7 rows (days of week) x 53 weeks (max possible)
    yearly_grid = [[' ' for _ in range(53)] for _ in range(7)]
    
    # Day names for the first column
    day_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    # Get current date for highlighting
    today = date.today()
    current_year = today.year
    current_month = today.month
    current_day = today.day
    
    week_num = 0
    
    # Fill the grid with all days of the year
    for month in range(1, 13):
        cal = calendar.monthcalendar(year, month)
        
        for week in cal:
            if week_num >= 53:  # Safety check
                break
                
            for day_of_week in range(7):
                day = week[day_of_week]
                if day != 0:
                    # Check if this is the first day of a month
                    is_first_day = (day == 1)
                    
                    # Check if this is today
                    is_today = (year == current_year and 
                               month == current_month and 
                               day == current_day)
                    
                    # Create the box character
                    if is_first_day:
                        # Bold/emphasized box for first day of month
                        box = '█'
                    elif is_today:
                        # Special box for today
                        box = '▓'
                    else:
                        # Regular box
                        box = '░'
                    
                    yearly_grid[day_of_week][week_num] = box
            
            week_num += 1
    
    # Display the yearly calendar
    print(f"\n{year}")
    print("=" * 53)
    
    # Print each day row
    for i, day_name in enumerate(day_names):
        row = f"{day_name} "
        for week in range(min(53, week_num)):
            row += yearly_grid[i][week]
        print(row)
    
    print("=" * 53)
    print("Legend: █ = First day of month, ▓ = Today, ░ = Regular day")


def display_monthly_calendar(year, month):
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
    parser.add_argument(
        "--yearly", "-Y",
        action="store_true",
        help="Show yearly view (default when no month specified)"
    )
    
    args = parser.parse_args()
    
    # Get current date if no arguments provided
    now = datetime.now()
    
    # Determine what to display
    if args.month is not None:
        # Show specific month
        year = args.year if args.year is not None else now.year
        month = args.month
        display_monthly_calendar(year, month)
    elif args.year is not None and args.month is None:
        # Show yearly view for specific year
        year = args.year
        display_yearly_calendar(year)
    elif args.current:
        # Show current month
        year = now.year
        month = now.month
        display_monthly_calendar(year, month)
    else:
        # Default: show yearly view for current year
        year = now.year
        display_yearly_calendar(year)
    
    # Validate year (reasonable range)
    if year < 1900 or year > 2100:
        print("Error: Year must be between 1900 and 2100")
        sys.exit(1)
    
    try:
        # Display logic is handled above based on arguments
        pass
    except Exception as e:
        print(f"Error displaying calendar: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 