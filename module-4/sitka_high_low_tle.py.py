import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

FILENAME = 'sitka_weather_2018_simple.csv'

def load_weather(filename):
    """Load dates, highs, and lows from the CSV file.
    Tries to resolve columns by header names; falls back to typical indices.
    Returns (dates, highs, lows). Skips rows with bad/missing data.
    """
    dates, highs, lows = [], [], []

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Try to find columns by name; fall back to common indices.
        # Typical 'simple' CSV has: DATE at index 2, TMAX at 5, TMIN at 6.
        def col_idx(name, default=None):
            try:
                return header_row.index(name)
            except ValueError:
                return default

        date_i = col_idx('DATE', 2)
        tmax_i = col_idx('TMAX', 5)
        tmin_i = col_idx('TMIN', 6)

        for row in reader:
            try:
                current_date = datetime.strptime(row[date_i], '%Y-%m-%d')
                high = int(row[tmax_i])
                low = int(row[tmin_i])
            except (ValueError, IndexError):
                # Skip rows with missing data
                continue
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

    return dates, highs, lows

def plot_highs(dates, highs):
    # Plot daily high temperatures (RED).
    fig, ax = plt.subplots()
    
    ax.plot(dates, highs, color ='red')
    plt.title("Daily HIGH temperatures - 2018", fontsize=24)
    plt.xlabel('Date', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

def plot_lows(dates, lows):
    # Plot daily low temperatures (BLUE).
    fig, ax = plt.subplots()

    ax.plot(dates, lows, color='blue')  # explicitly blue per your requirement
    plt.title("Daily LOW temperatures - 2018", fontsize=24)
    plt.xlabel('Date', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

def print_menu():
    print("\nSitka Weather (2018) — Menu")
    print("Type one of the following and press Enter:")
    print("  highs  → show daily high temperatures")
    print("  lows   → show daily low temperatures (blue)")
    print("  exit   → quit the program")

def main():
    # Load data once, reuse for each plot request.
    try:
        dates, highs, lows = load_weather(FILENAME)
    except FileNotFoundError:
        print(f"Could not find '{FILENAME}'. Place the CSV next to this script and try again.")
        sys.exit(1)

    if not dates:
        print("No usable data found in the CSV. Please check the file and try again.")
        sys.exit(1)

    print_menu()
    while True:
        choice = input("\nYour selection (highs/lows/exit): ").strip().lower()

        if choice == 'highs':
            plot_highs(dates, highs)
        elif choice == 'lows':
            plot_lows(dates, lows)
        elif choice == 'exit':
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Sorry, please type 'highs', 'lows', or 'exit'.")
            # Reprint the menu after an invalid choice:
            print_menu()

if __name__ == "__main__":
    main()
