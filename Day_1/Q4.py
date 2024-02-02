# Write a program to output how many sunday did you spent it


# from datetime import datetime, timedelta


#     # Get user input for birthday
# birthday_str = input("Enter your birthday (YYYY-MM-DD): ")

#     # Convert input string to a datetime object
# birthday = datetime.strptime(birthday_str, '%Y-%m-%d')

#     # Get the current date
# today = datetime.now()

#     # Calculate the number of Sundays
# sunday_count = sum(1 for day in range((today - birthday).days + 1) 
#                        if (birthday + timedelta(days=day)).weekday() == 6)

#     # Display the result
# print(f"You have lived {sunday_count} Sundays since your birthday.")



# totalday = 0
# sunday = 0

# date = int(input("Day: "))
# month = int(input("Month: "))
# year = int(input("Year: "))
# day = input("What is today's day(M/Tu/W/Th/F/Sa/Su): ").upper()
# while day not in ["M", "TU", "W", "TH", "F", "SA", "SU"]:
#     day = input("What is today's day(M/Tu/W/Th/F/Sa/Su): ").upper()

# date2 = int(input("What is today's date: "))
# month2 = int(input("What is today's Month: "))
# year2 = int(input("What is right now year?: "))

# days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# totalday += sum(days_in_month[month2+1:]) + date2
# totalday += sum(days_in_month[month+1:]) + (days_in_month[month] - date + 1)

# totalday += (year2 - year - 1) * 365
# totalday += sum(1 for i in range(year + 1, year2) if (i % 400 == 0) or (i % 4 == 0 and (i % 100 != 0)))

# if (year % 400 == 0) or (year % 4 == 0 and (year % 100 != 0)) and month < 3 and date != 29:
#     totalday += 1

# if (year2 % 400 == 0) or (year2 % 4 == 0 and (year2 % 100 != 0)) and month2 >= 2 and not(month2 == 2 and date2 == 29):
#     totalday += 1

# sunday += totalday // 7
# sunday += 1 if day != "SU" else 0

# print(sunday)





from datetime import datetime, timedelta


    # Get user input for birthday
birthday_str = input("Enter your birthday (YYYY-MM-DD): ")

    # Convert input string to a datetime object
birthday = datetime.strptime(birthday_str, '%Y-%m-%d')

    # Get the current date
today = datetime.now()

    # Calculate the number of Sundays
sunday_count = sum(1 for day in range((today - birthday).days +1) 
                       if (birthday + timedelta(days=day)).weekday() == 6)

    # Display the result
print(f"You have lived {sunday_count} Sundays since your birthday.")











