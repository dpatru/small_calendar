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
    weekdays = [[] for _ in range(8)]
    first_day, today_char, regular_day = ('█', '.', '.')
    first_day = ['X','J','F','M','A','M','J','J','A','S','O','N','D'] 
    # Get current date for highlighting
    today_date = date.today()
    current_year = today_date.year
    current_month = today_date.month
    current_day = today_date.day
    cal = calendar.Calendar()
    cal.firstweekday = 6
    for m in range(1,13):
        for (y,m2,dm,dw) in cal.itermonthdays4(year, m):
            if m2 != m: continue
            # print(y,m2,dm,dw)
            v = (today_char if (y==current_year and m==current_month and dm==current_day) \
                 else first_day[m2] if dm==1 \
                 else regular_day)
            weekdays[(dw+1)%7].append(v) # shift by 1 to make Sunday the first day of the week
    # add empty days to the beginning of the week if the first day is not Sunday
    for dw in range(7):
        if weekdays[dw][0] in first_day: 
            break
        else: 
            weekdays[dw].insert(0, ' ')
    # add empty days to the end of the week if the last day is not Saturday
    for dw in range(1,7):
        if len(weekdays[dw]) < len(weekdays[0]):
            weekdays[dw].append(' ')


    # Day names for the first column (Sunday first)
    day_names = ['S','M','T','W','T','F','S'] # ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    
    week_num = len(weekdays[0])
    # Display the yearly calendar with bordered boxes
    print(f"\n{year}") # ({week_num} weeks)")
    
    # Print top border
    # print("┌" + "─" * (week_num + 4) + "┐")
    
    # Print each day row with borders
    for i, day_name in enumerate(day_names):
        row = f"{day_name} {''.join(weekdays[i])}"
        print(row)
        
        # Print separator line (except for last row)
        # if i < 6:
        #     print("├" + "─" * (week_num + 4) + "┤")
    
    # Print bottom border
    # print("└" + "─" * (week_num + 4) + "┘")
    # print(f"Legend: {first_day} = First day of month, {today_char} = Today, {regular_day} = Regular day")


def display_multiple_years_side_by_side(years):
    """Display multiple years side by side with year names above January columns."""
    if not years:
        return
    
    # Get current date for highlighting
    today_date = date.today()
    current_year = today_date.year
    current_month = today_date.month
    current_day = today_date.day
    
    # Initialize data structure for all years
    all_years_data = {}
    cal = calendar.Calendar()
    cal.firstweekday = 6  # Sunday first
    
    # Process each year
    for year in years:
        weekdays = [[] for _ in range(7)]
        first_day = ['X','J','F','M','A','M','J','J','A','S','O','N','D']
        today_char, regular_day = '.', '.'
        
        for m in range(1, 13):
            for (y, m2, dm, dw) in cal.itermonthdays4(year, m):
                if m2 != m:
                    continue
                v = (today_char if (y == current_year and m == current_month and dm == current_day)
                     else first_day[m2] if dm == 1
                     else regular_day)
                weekdays[(dw + 1) % 7].append(v)  # shift by 1 to make Sunday first
        
        # Pad weeks to uniform length
        max_weeks = max(len(row) for row in weekdays)
        for dw in range(7):
            # Add spaces at beginning if needed
            if weekdays[dw][0] in first_day:
                weekdays[dw].insert(0, ' ')
            # Pad to uniform length
            while len(weekdays[dw]) < max_weeks:
                weekdays[dw].append(' ')
        
        all_years_data[year] = weekdays
    
    # Day names
    day_names = ['S', 'M', 'T', 'W', 'T', 'F', 'S']
    
    # Calculate the width of each year's data for proper alignment
    year_width = len(all_years_data[years[0]][0]) if years else 52
    
    # Print year headers - align with the start of each year's data
    year_header = "   "  # Space for day name column
    for year in years:
        # Find the position of January (J) in the first row to align the year name
        first_row = all_years_data[year][0]
        jan_pos = -1
        for i, char in enumerate(first_row):
            if char == 'J':
                jan_pos = i
                break
        
        if jan_pos >= 0:
            # Align year name with January
            year_header += " " * jan_pos + str(year)
        else:
            # Fallback alignment
            year_header += f"{year:>52}"
    print(year_header)
    
    # Print each day row across all years
    for i, day_name in enumerate(day_names):
        row = f"{day_name} "
        for year in years:
            row += ''.join(all_years_data[year][i])
        print(row)


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
        "--years", "-Y",
        type=str,
        help="Range of years (e.g., '2020-2025' or '2020,2022,2024')"
    )
    parser.add_argument(
        "--number", "-n",
        type=int,
        help="Number of years to display (use with --year to specify start year)"
    )
    parser.add_argument(
        "--current", "-c",
        action="store_true",
        help="Show current month (default)"
    )
    parser.add_argument(
        "--yearly",
        action="store_true",
        help="Show yearly view (default when no month specified)"
    )
    
    args = parser.parse_args()
    
    # Get current date if no arguments provided
    now = datetime.now()
    
    # Determine what to display
    if args.years is not None:
        # Show multiple years
        years = parse_years_range(args.years)
        display_multiple_years_side_by_side(years)
    elif args.number is not None:
        # Show specified number of years
        if args.year is not None:
            start_year = args.year
        else:
            start_year = now.year
        
        years = list(range(start_year, start_year + args.number))
        display_multiple_years_side_by_side(years)
    elif args.month is not None:
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
    
    try:
        # Display logic is handled above based on arguments
        pass
    except Exception as e:
        print(f"Error displaying calendar: {e}")
        sys.exit(1)


def parse_years_range(years_str):
    """Parse a string of years into a list of years."""
    years = []
    
    # Handle comma-separated years
    if ',' in years_str:
        for year_str in years_str.split(','):
            year_str = year_str.strip()
            if '-' in year_str:
                # Handle ranges within comma-separated list
                years.extend(parse_years_range(year_str))
            else:
                try:
                    year = int(year_str)
                    if 1900 <= year <= 2100:
                        years.append(year)
                    else:
                        print(f"Warning: Year {year} is out of range (1900-2100)")
                except ValueError:
                    print(f"Warning: Invalid year '{year_str}'")
    
    # Handle year ranges (e.g., "2020-2025")
    elif '-' in years_str:
        try:
            start_str, end_str = years_str.split('-', 1)
            start_year = int(start_str.strip())
            end_year = int(end_str.strip())
            
            if start_year > end_year:
                start_year, end_year = end_year, start_year
            
            if start_year < 1900 or end_year > 2100:
                print("Warning: Some years are out of range (1900-2100)")
            
            for year in range(start_year, end_year + 1):
                if 1900 <= year <= 2100:
                    years.append(year)
        except ValueError:
            print(f"Error: Invalid year range '{years_str}'")
    
    # Handle single year
    else:
        try:
            year = int(years_str)
            if 1900 <= year <= 2100:
                years.append(year)
            else:
                print(f"Warning: Year {year} is out of range (1900-2100)")
        except ValueError:
            print(f"Error: Invalid year '{years_str}'")
    
    return years


if __name__ == "__main__":
    main() 