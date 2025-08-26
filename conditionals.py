day_of_week = input("enter the day of week: ").lower()
print(day_of_week)

month_of_year = input("enter the month of year: ").upper()
print(month_of_year)

if day_of_week == "saturday" or day_of_week == "sunday":
    print("i will learn live devops")
else:
    print("just i will practice devops")

num1 = int(input("enter first number: " ))
num2 = int(input("enter second number: " ))

choice = input("enter the operations: (options + , - , * , / , ) ")
if choice == "+":
    sum_of_num = num1 + num2
    print("addition: ", sum_of_num)

elif choice == "-":
    diff_of_num = num1 - num2
    print("substraction: ",diff_of_num)

elif choice == "*":
    prod_of_num = num1 * num2
    print("multiplication: ",prod_of_num)

elif choice == "/":
    div_of__num = num1 / num2
    print("division: ",div_of__num)

elif choice == "%":
    rem_of_num = num1 % num2
    print("remainder: ",rem_of_num)
else:
    print("invalid choice")

    