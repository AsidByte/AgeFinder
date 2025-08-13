name = (input("What is your name: "))

birth_year = int (input("Enter your birth year: "))

year = int(input("Enter the year in which you want to know your age: "))

year_1 = str(year-birth_year)

current_year = (2025)

comment_1 = (" you were ")
comment_2 = (" you are ")
comment_3 = (" you will become ")

if year < current_year: print (name + comment_1 + year_1 +(" Years old") )
elif year == current_year: print (name + comment_2 + year_1 +(" Years old") ) 
else: print(name + comment_3 + year_1 +(" Years old") )
