#!/usr/bin/env python3
"""
Small Calendar - A simple command-line calendar tool
"""

import argparse
import calendar
import sys
from datetime import datetime, date
import itertools


def display_yearly_calendar(year, n=1, vertical=False):
    """Display a condensed yearly calendar with 7 rows (days of week) and actual number of weeks."""
    if vertical:
        # Vertical display: transpose the horizontal data
        display_yearly_calendar_horizontal(year, n, vertical=True)
    else:
        # Horizontal display: days as rows, months as columns (original behavior)
        display_yearly_calendar_horizontal(year, n, vertical=False)

def display_yearly_calendar_horizontal(year, n=1, vertical=False):
    """Display a condensed yearly calendar horizontally with 7 rows (days of week) and actual number of weeks."""
    weekdays = ['S','M','T','W','T','F','S'] 
    _, today_char, regular_day = ('█', '.', '.')
    first_day = ['X','J','F','M','A','M','J','J','A','S','O','N','D'] 
    # Get current date for highlighting
    today_date = date.today()
    current_year = today_date.year
    current_month = today_date.month
    current_day = today_date.day
    cal = calendar.Calendar()
    cal.firstweekday = 6
    if vertical:
        print(f'     {''.join(weekdays)}')
        weekstring = str(year)+' '
        for m in range(12*n):
            for (y,m2,dm,dw) in cal.itermonthdays4(year+m//12, m%12+1):
                if y < year or y == year + n: # need to add padding before we start and after we finish
                    weekstring += ' '
                    # print(f"Adding padding for year {y}-{m2}-{dm}-{dw}")
                elif m2 != m%12+1: # skip months that are not the current month
                    if y == year + n: pass
                    else:continue
                elif dm == 1: # first day of the month
                    weekstring += first_day[m2]
                else:
                    weekstring += regular_day
                if dw == 5:
                    print(weekstring)
                    weekstring = ((str(y+1) + ' ') if m2 == 12 and dm > 31-7 and y < year + n - 1 else 
                                  '     ')

        return # finished vertical
    # horizontal
    year_row = []
    weekdays = [[day+' '] for day in weekdays]
    for m in range(12*n):
        for (y,m2,dm,dw) in cal.itermonthdays4(year+m//12, m%12+1):
            # print(f"{m}: {y} {m2} {dm} {dw}")
            # align the year name with the first day of the month, 
            # but only if we are actually processing this month.
            if m2 == 1 and dm == 1 and y < year + n and m2 == m%12+1: 
                print(f"Adding year {y} to the row")
                print(f"weekdays[dw]: {weekdays[dw+1]}")
                print(f"year_row: {year_row}")
                year_row.append((len(''.join(weekdays[dw+1])) - len(''.join(year_row)))*' ' + str(y) + ' ')
            # print(y,m2,dm,dw)
            v = (' ' if m == 0 and year != y else # empty space if the year is not the current year, occurs when the Jan 1st is not the first day of the week
                 '' if m2 != m%12+1 else # first day of the month is not the first day of the week
                 today_char if (y==current_year and m==current_month and dm==current_day) else 
                 first_day[m2] if dm==1 else 
                 regular_day)
            weekdays[(dw+1)%7].append(v) # shift by 1 to make Sunday the first day of the week
    # add empty days to the end of the week if the last day is not Saturday
    for dw in range(1,7):
        if len(weekdays[dw]) < len(weekdays[0]):
            weekdays[dw].append(' ')

    # Day names for the first column (Sunday first)
    day_names = ['S','M','T','W','T','F','S'] # ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    
        # Horizontal display: days as rows, months as columns (original behavior)
    print(f"\n{''.join(year_row)}")
    for i, day_name in enumerate(day_names):
        row = f"{''.join(weekdays[i])}"
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
    parser.add_argument(
        "--vertical", "-v",
        action="store_true",
        help="Display calendar vertically (weeks as rows, weekdays as columns)"
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
        
        display_yearly_calendar(start_year, args.number, args.vertical)
    elif args.year is not None:
        # Show yearly view for specific year
        year = args.year
        display_yearly_calendar(year, 1, args.vertical)
    elif args.current:
        # Show current year
        year = now.year
        display_yearly_calendar(year, 1, args.vertical)
    else:
        # Default: show yearly view for current year
        year = now.year
        display_yearly_calendar(year, 1, args.vertical)
    
    try:
        # Display logic is handled above based on arguments
        pass
    except Exception as e:
        print(f"Error displaying calendar: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 