#!/usr/bin/env python3
"""
Small Calendar - A simple command-line calendar tool
"""

import argparse
import calendar
import sys
from datetime import datetime, date
import itertools


def parse_date(date_string):
    """Parse a date string in YYYY-MM-DD format."""
    try:
        return datetime.strptime(date_string, '%Y-%m-%d').date()
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid date format: {date_string}. Use YYYY-MM-DD format.")


def display_yearly_calendar(year, n=1, vertical=False, mark_date=None):
    """Display a condensed yearly calendar with 7 rows (days of week) and actual number of weeks."""
    weekdays = ['S','M','T','W','T','F','S'] 
    _, today_char, regular_day = ('█', '*', '.')
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
                elif mark_date and y == mark_date.year and m2 == mark_date.month and dm == mark_date.day:
                    weekstring += today_char
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
                year_row.append((len(''.join(weekdays[dw+1])) - len(''.join(year_row)))*' ' + str(y) + ' ')
            # print(y,m2,dm,dw)
            v = (' ' if m == 0 and year != y else # empty space if the year is not the current year, occurs when the Jan 1st is not the first day of the week
                 '' if m2 != m%12+1 else # first day of the month is not the first day of the week
                 today_char if (mark_date and y==mark_date.year and m2==mark_date.month and dm==mark_date.day) else 
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
        default=datetime.now().year,
        help="Year (e.g., 2024, default: current year)"
    )
    parser.add_argument(
        "--number", "-n",
        type=int,
        default=1,
        help="Number of years to display (use with --year to specify start year, default: 1)"
    )
    parser.add_argument(
        "--vertical", "-v",
        action="store_true",
        help="Display calendar vertically (weeks as rows, weekdays as columns)"
    )
    parser.add_argument(
        "--mark-date",
        nargs='?',
        const=datetime.now().date(),
        type=parse_date,
        help="Mark a date for highlighting (default: today's date if no date specified)"
    )
    
    args = parser.parse_args()
    
    # Display the calendar
    display_yearly_calendar(args.year, args.number, args.vertical, args.mark_date)
    
    try:
        # Display logic is handled above based on arguments
        pass
    except Exception as e:
        print(f"Error displaying calendar: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 