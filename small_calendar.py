#!/usr/bin/env python3
"""
Small Calendar - A simple command-line calendar tool
"""

import argparse
import calendar
import sys
from datetime import datetime, date


def create_day_box(day_type="regular"):
    """Create a bordered box for a day based on its type."""
    if day_type == "first_day":
        # Bold/emphasized box for first day of month
        return "┌─┐"
    elif day_type == "today":
        # Special box for today
        return "┌─┐"
    else:
        # Regular box
        return "┌─┐"


def display_yearly_calendar(year):
    """Display a condensed yearly calendar with 7 rows (days of week) and actual number of weeks."""
    # Calculate the number of weeks properly
    # 52 full weeks = 364 days
    # Remaining days determine if we have 52, 53, or 54 weeks
    
    # Check if it's a leap year
    is_leap = calendar.isleap(year)
    
    # Get the day of week for January 1st (6=Sunday, 0=Monday, 6=Sunday)
    jan1_weekday = date(year, 1, 1).weekday()
    # Convert to Sunday-based (0=Sunday, 1=Monday, ..., 6=Saturday)
    jan1_sunday_based = (jan1_weekday + 1) % 7
    
    # Calculate weeks based on the correct logic
    if is_leap:
        # Leap year: 366 days
        # 52 full weeks = 364 days
        # Remaining 2 days
        if jan1_sunday_based == 6:  # Saturday
            # Starts Saturday, ends Sunday = 54 weeks (1 + 52 + 1)
            num_weeks = 54
        else:
            # Starts other day, ends other day = 53 weeks
            num_weeks = 53
    else:
        # Regular year: 365 days
        # 52 full weeks = 364 days
        # Remaining 1 day
        if jan1_sunday_based == 6:  # Saturday
            # Starts Saturday, ends Saturday = 53 weeks (1 + 52)
            num_weeks = 53
        else:
            # Starts other day, ends other day = 52 weeks
            num_weeks = 52
    
    # Initialize the yearly grid: 7 rows (days of week) x actual weeks
    yearly_grid = [[' ' for _ in range(num_weeks)] for _ in range(7)]
    
    # Day names for the first column (Sunday first)
    day_names = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    
    # Get current date for highlighting
    today = date.today()
    current_year = today.year
    current_month = today.month
    current_day = today.day
    
    week_num = 0
    
    # Fill the grid with all days of the year
    for month in range(1, 13):
        # Use Sunday as first day of week
        cal = calendar.monthcalendar(year, month)
        
        for week in cal:
            if week_num >= num_weeks:  # Safety check
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
    
    # Display the yearly calendar with bordered boxes
    print(f"\n{year} ({num_weeks} weeks)")
    
    # Print top border
    print("┌" + "─" * (num_weeks + 3) + "┐")
    
    # Print each day row with borders
    for i, day_name in enumerate(day_names):
        row = f"│{day_name}"
        for week in range(min(num_weeks, week_num)):
            row += yearly_grid[i][week]
        row += "│"
        print(row)
        
        # Print separator line (except for last row)
        if i < 6:
            print("├" + "─" * (num_weeks + 3) + "┤")
    
    # Print bottom border
    print("└" + "─" * (num_weeks + 3) + "┘")
    print("Legend: █ = First day of month, ▓ = Today, ░ = Regular day")


def display_monthly_calendar(year, month):
    """Display a formatted calendar for the specified month and year."""
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    
    # Header
    print(f"\n{month_name} {year}")
    
    # Print top border
    print("┌─────┬─────┬─────┬─────┬─────┬─────┬─────┐")
    print("│ Sun │ Mon │ Tue │ Wed │ Thu │ Fri │ Sat │")
    print("├─────┼─────┼─────┼─────┼─────┼─────┼─────┤")
    
    # Get current date for highlighting
    today = date.today()
    current_year = today.year
    current_month = today.month
    current_day = today.day
    
    # Display calendar
    for i, week in enumerate(cal):
        week_str = "│"
        for day in week:
            if day == 0:
                week_str += "     │"
            else:
                # Highlight current date
                if (year == current_year and 
                    month == current_month and 
                    day == current_day):
                    week_str += f" [{day:2d}] │"
                else:
                    week_str += f"  {day:2d} │"
        print(week_str)
        
        # Print separator line (except for last week)
        if i < len(cal) - 1:
            print("├─────┼─────┼─────┼─────┼─────┼─────┼─────┤")
    
    # Print bottom border
    print("└─────┴─────┴─────┴─────┴─────┴─────┴─────┘")


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