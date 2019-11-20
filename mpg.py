#!/usr/bin/env python3

# display a welcome message
choice = "y"
while choice.lower() == "y":
    print("The Miles Per Gallon application")
    print()
    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_gallon = float(input("Enter cost per gallon:       "))
    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_gallon <= 0:
        print("You need to pay for gas, this is not communism! Please try again.")
    else:
    # calculate and display miles per gallon and etc
        mpg = round((miles_driven / gallons_used), 2)
        tgc = round((gallons_used * cost_gallon), 2)
        cpm = round((miles_driven * cost_gallon), 2)
        print()
    print("Miles Per Gallon:          ", mpg)
    print("Total Gas Cost:         ", tgc)
    print("Cost Per Mile:       ", cpm)
    print()
    choice = input("Would you like to calculate another trip? (y/n):    ")
print()
print("Bye!") #runs when loop ends
