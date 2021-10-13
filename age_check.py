import datetime

def player_age():
    while True:
        Age = input("How old are you? ")
        try:
            checker = int(Age)
            if checker >= 18 :
                print("Nice to meet you!")
                break
            else:
                print("You're a bit young aren't you?")
        except ValueError:
            print("Amount must be a number, try again")
    return checker
player_age()



#  Variables & Big Catching
age = input('What year where you born? ')
if age.isdigit() is False:
    print('Please enter a number')
    quit()
elif len(age) != 4:
    print('Please enter a valid year!')
    quit()
elif age.isdigit() is True and len(age) == 4:
    int_age = int(age)
current_time = datetime.datetime.now().year
print('You are', current_time - int_age, 'Years old')



 
print("##### Welcome to age calculator ######")
birth_year = int(input("Enter your year of birth: \n"))
birth_month = int(input("Enter your month of birth: \n"))
birth_day = int(input("Enter your day of birth: \n"))
 
current_year = datetime.date.today().year
current_month = datetime.date.today().month
current_day = datetime.date.today().day
 
age_year = current_year - birth_year
age_month = abs(current_month-birth_month)
age_day = abs(current_day-birth_day)
 
print("Your exact age is: ", age_year, "Years", age_month, "months and", age_day, "days")
