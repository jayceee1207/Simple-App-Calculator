#John Carlo Ablay
#BSCPE 1-5
#Assignment 4: Program 1
#May 6, 2023

import pyfiglet 
#PSEUDOCODE
#Make a menu where user will choose their option of operation
def menu():
    print("Please choose an option from the menu.")
    print("[1] Operation 1:","Addition")
    print("[2] Operation 2:","Subtraction")
    print("[3] Operation 3:","Multiplication")
    print("[4] Operation 4:","Division")
menu()
#Ask the user to choose one of the four math operations
option = int(input("\nEnter your option: ")) 

#While True to rerun the program if the user wish to
while True:
#If option is out of choices, the program will ask their option again
    while option > 4:
        print("Invalid option. Please try again!") 
        option = int(input("\nEnter your option: "))
#if choice is Addition
    if option == 1:
        add_numbers = pyfiglet.figlet_format("Addition",font = "bulbhead" )
        print (add_numbers)
    #Get two numbers from the user
    try:
        add_num_1 = float(input("Please enter first number: "))
        add_num_2 = float(input("Please enter second number: "))
        #Perform the operation
        sum_numbers = add_num_1 + add_num_2
        #Display the result
        print("The sum of two numbers is: ",sum_numbers, "\n")
    #Add Error Handling
    except ValueError:
        #If the user input a string instead of number
        print("Do not put letters. Input numbers. Try again!")
        
   

#if choice is Subtraction
    if option == 2:
            subtract_numbers = pyfiglet.figlet_format("Subtraction",font = "bulbhead" )
            print (subtract_numbers)
    #Get two numbers from the user
    #Perform the operation
    #Display the result
#Add Error Handling
    #If the user input a string instead of number

#if choice is Multiplication
    #Get two numbers from the user
    #Perform the operation
    #Display the result
#Add Error Handling
    #If the user input a string instead of number

#if choice is Division
    #Get two numbers from the user
    #Perform the operation
    #Display the result
#Add Error Handling
    #If the user input a string instead of number
    #If the user input zero (0) in the second number

#Ask the user if they want to try again 
#If they want to try again
    #Repeat the program
    #Continue the program
#If they do not want to try again
    #Display Thank you message
    #Stop the program