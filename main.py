print("***TIP CALCULATOR***")
print()
myBill = float(input("What was the bill?: "))
print()
numberOfPeople = int(input("How many people?: "))
print()
answer = myBill / numberOfPeople
answer = round (answer, 2)
print()
tip = int (input("What percentage are you tipping?: "))
tip = tip/100
print()
answer2 = (answer * tip) + answer
answer2 = round (answer, 2)
print("You owe a total of", answer2)