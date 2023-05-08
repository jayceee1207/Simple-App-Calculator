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
        try:
            #Get two numbers from the user
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
        try:
            #Get two numbers from the user
            sub_num_1 = float(input("Please enter first number: "))
           
            sub_num_2 = float(input("Please enter second number: "))
            #Perform the operation
        
            difference_numbers = sub_num_1 - sub_num_2

            #Display the result
            print("The difference of two numbers is: ",difference_numbers, "\n")
        
        #Add Error Handling
        except ValueError:
            print("Do not put letters. Input numbers. Try again!")
            
    #if choice is Multiplication
    if option == 3:
        mult_numbers = pyfiglet.figlet_format("Multiplication",font = "bulbhead" )
        print (mult_numbers)
        try:
            #Get two numbers from the user 
            mult_num_1 = float(input("Please enter first number: "))
            mult_num_2 = float(input("Please enter second number: "))
            #Perform the operation
            product_numbers = mult_num_1 * mult_num_2

            #Display the result
            print("The product of two numbers is: ",product_numbers, "\n") 
            #Add Error Handling
        except ValueError:
            print("Do not put letters. Input numbers. Try again!")

#if choice is Division
    if option == 4:
        division_numbers = pyfiglet.figlet_format("Division",font = "bulbhead" )
        print (division_numbers)
        try:
            #Get two numbers from the user 
            div_num_1 = float(input("Please enter first number: "))
            div_num_2 = float(input("Please enter second number: "))
            #Perform the operation
            quotient_numbers = div_num_1/div_num_2
            #Display the result
            print("The quotient of two numbers is: ",quotient_numbers,"\n")
        
        #Add Error Handling
        except ValueError:
            print("Do not put letters. Input numbers. Try again!")
        except ZeroDivisionError:
            print("You cannot input 0 on the second number. Try again!")

    #Ask the user if they want to try again 
    try_again = input("Do you want to use the program again? \n[Yes] if continue \n[No] if exit \nEnter option: ")
    #If they want to try again
    if try_again == "Yes":
        #Repeat the program
        menu()
        option = int(input("\nEnter your option: "))
        continue  
    #If they do not want to try again
    else:
        #Display Thank you message
        print("\nThank you for using my program! Have a good day!")
        break