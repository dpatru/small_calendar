#!/usr/bin/env python3
"""
Small Calendar - A simple command-line calendar tool
"""

import argparse
import calendar
import sys
from datetime import datetime, date



def display_yearly_calendar(year, n=1):
    """Display a condensed yearly calendar with 7 rows (days of week) and actual number of weeks."""
    weekdays = [[] for _ in range(7)]
    first_day, today_char, regular_day = ('█', '.', '.')
    first_day = ['X','J','F','M','A','M','J','J','A','S','O','N','D'] 
    # Get current date for highlighting
    today_date = date.today()
    current_year = today_date.year
    current_month = today_date.month
    current_day = today_date.day
    cal = calendar.Calendar()
    cal.firstweekday = 6
    year_row = ''
    for m in range(12*n):
        for (y,m2,dm,dw) in cal.itermonthdays4(year+m//12, m%12+1):
            # print(f"{m}: {y} {m2} {dm} {dw}")
            if m2 != m%12+1: continue
            # align the year name with the first day of the month
            if m2 == 1 and dm == 1: 
                year_row += (len(''.join(weekdays[0])) - len(year_row))*' ' + str(y)
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
    
   
    print(f"\n  {year_row}")
    
    # Print each day row with borders
    for i, day_name in enumerate(day_names):
        row = f"{day_name} {''.join(weekdays[i])}"
        print(row)
        
    
def main():
    """Main function to handle command-line arguments and display calendar."""
    parser = argparse.ArgumentParser(
        description="Display a simple calendar for a specific year or range of years"
    )
    parser.add_argument(
        "--year", "-y",
        type=int,
        help="Year (e.g., 2024)"
    )
    parser.add_argument(
        "--number", "-n",
        type=int,
        help="Number of years to display (use with --year to specify start year)"
    )
    parser.add_argument(
        "--current", "-c",
        action="store_true",
        help="Show current year (default)"
    )
    parser.add_argument(
        "--yearly",
        action="store_true",
        help="Show yearly view (default)"
    )
    
    args = parser.parse_args()
    
    # Get current date if no arguments provided
    now = datetime.now()
    
    # Determine what to display
    if args.number is not None:
        # Show specified number of years
        if args.year is not None:
            start_year = args.year
        else:
            start_year = now.year
        
        display_yearly_calendar(start_year, args.number)
    elif args.year is not None:
        # Show yearly view for specific year
        year = args.year
        display_yearly_calendar(year, 1)
    elif args.current:
        # Show current year
        year = now.year
        display_yearly_calendar(year, 1)
    else:
        # Default: show yearly view for current year
        year = now.year
        display_yearly_calendar(year, 1)
    
    try:
        # Display logic is handled above based on arguments
        pass
    except Exception as e:
        print(f"Error displaying calendar: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 