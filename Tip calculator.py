print("Welcome tto thee tip calculator.")
bill=int(input("what is total bill" ))
percentage=int(input("what percentage tip would you like to give? 10, 12, or 15? "))
total_bill=bill+((percentage/100)*bill)
no_of_people=int(input("How many people to split the bill? "))

each_person_bill=round(total_bill/no_of_people,2)
print(f"Each person should pay: ${each_person_bill}")
