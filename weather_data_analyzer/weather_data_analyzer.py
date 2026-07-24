# Display Project Title
print("=" * 30)
print("              WEATHER DATA ANALYZER")
print("=" * 30)

choice = "Y" # Variable Initialization
while choice == "Y" or choice == "y":  # While Loop - Repeat Program

    # Input Statements
    day1 = float(input("\nEnter Day 1 Temperature: "))
    day2 = float(input("Enter Day 2 Temperature: "))
    day3 = float(input("Enter Day 3 Temperature: "))
    day4 = float(input("Enter Day 4 Temperature: "))
    day5 = float(input("Enter Day 5 Temperature: "))
    day6 = float(input("Enter Day 6 Temperature: "))
    day7 = float(input("Enter Day 7 Temperature: "))

    # Arithmetic Operations
    total = day1 + day2 + day3 + day4 + day5 + day6 + day7
    average = total / 7

    # Finding Highest Temperature
    highest = day1

    if day2 > highest:
        highest = day2

    if day3 > highest:
        highest = day3

    if day4 > highest:
        highest = day4

    if day5 > highest:
        highest = day5

    if day6 > highest:
        highest = day6

    if day7 > highest:
        highest = day7

    # Finding Lowest Temperature
    lowest = day1

    if day2 < lowest:
        lowest = day2

    if day3 < lowest:
        lowest = day3

    if day4 < lowest:
        lowest = day4

    if day5 < lowest:
        lowest = day5

    if day6 < lowest:
        lowest = day6

    if day7 < lowest:
        lowest = day7

    # Output Statements
    print("\n" + "=" * 60)
    print("             WEATHER ANALYSIS REPORT")
    print("=" * 60)
    print("Total Temperature   :", total)
    print("Average Temperature :", round(average, 2))
    print("Highest Temperature :", highest)
    print("Lowest Temperature  :", lowest)
    print("=" * 60)

    # Continue Program
    choice = input("\nAnalyze another week's data? (Y/N): ")

# Exit Message
print("\nThank you for using Weather Data Analyzer!")

