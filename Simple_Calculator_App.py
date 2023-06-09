#John Carlo Ablay
#BSCPE 1-5
#Assignment 4: Program 1
#May 6, 2023

import pyfiglet
import emoji
from pyfiglet import Figlet
from termcolor import colored 

design = ("*********************************************************")
subject_name = ("Program: Simple App Calculator")
program_name = Figlet(font='banner3-D')
author_name = ("Programmed by: John Carlo R. Ablay")

design_center = design.center(120)
subject_name_center = subject_name.center(120)
author_name_center = author_name.center(120)



print("\u001b[35;1m", design_center)
print("\u001b[33;1m", subject_name_center)
print("\u001b[33;1m",author_name_center)
print("\u001b[35;1m",design_center)
print(colored(program_name.renderText("O-O-P"), 'green').center(120))

try:
    #PSEUDOCODE
    #Make a menu where user will choose their option of operation
    def menu():
        print("\u001b[34;1m","Please choose an option from the menu.")
        print("\u001b[32;1m","[1] Operation 1:","\u001b[37;1m","Addition")
        print("\u001b[32;1m","[2] Operation 2:","\u001b[37;1m","Subtraction")
        print("\u001b[32;1m","[3] Operation 3:","\u001b[37;1m","Multiplication")
        print("\u001b[32;1m","[4] Operation 4:","\u001b[37;1m","Division")
    menu()
    #Ask the user to choose one of the four math operations

    option = int(input("\nEnter your option: ")) 

    #While True to rerun the program if the user wish to
    while True:
        #If option is out of choices, the program will ask their option again
        while option > 4 or 0 > option:
            print("Invalid option. Please try again!") 
            option = int(input("\nEnter your option: "))
        #if choice is Addition

        if option == 1:
            add_numbers = pyfiglet.figlet_format("Addition",font = "bulbhead" )
            print (add_numbers)
            try:
                #Get two numbers from the user
                add_num_1 = float(input("Please enter first number: "))
                print(emoji.emojize(':plus:'))
                add_num_2 = float(input("Please enter second number: "))
                #Perform the operation
                sum_numbers = add_num_1 + add_num_2
                #Display the result
                print(emoji.emojize(':heavy_equals_sign:'))
                print("\u001b[34;1mThe sum of two numbers is: ",sum_numbers, "\n")
            
            #Add Error Handling
            except ValueError:
                #If the user input a string instead of number
                print("\u001b[31;1mDo not put letters. Input numbers. Try again!")
            

        #if choice is Subtraction
        elif option == 2:
            subtract_numbers = pyfiglet.figlet_format("Subtraction",font = "bulbhead" )
            print (subtract_numbers)
            try:
                #Get two numbers from the user
                sub_num_1 = float(input("Please enter first number: "))
                print(emoji.emojize(':minus:'))
                sub_num_2 = float(input("Please enter second number: "))
                #Perform the operation
                print(emoji.emojize(':heavy_equals_sign:'))
                difference_numbers = sub_num_1 - sub_num_2

                #Display the result
                print("\u001b[34;1mThe difference of two numbers is: ",difference_numbers, "\n")
            
            #Add Error Handling
            except ValueError:
                print("\u001b[31;1mDo not put letters. Input numbers. Try again!")

        #if choice is Multiplication
        elif option == 3:
            mult_numbers = pyfiglet.figlet_format("Multiplication",font = "bulbhead" )
            print (mult_numbers)
            try:
                #Get two numbers from the user 
                mult_num_1 = float(input("Please enter first number: "))
                print(emoji.emojize(':multiply:'))
                mult_num_2 = float(input("Please enter second number: "))
                #Perform the operation
                print(emoji.emojize(':heavy_equals_sign:'))
                product_numbers = mult_num_1 * mult_num_2

                #Display the result
                print("\u001b[34;1mThe product of two numbers is: ",product_numbers, "\n") 
                #Add Error Handling
            except ValueError:
                print("\u001b[31;1mDo not put letters. Input numbers. Try again!")

        #if choice is Division
        else:
            division_numbers = pyfiglet.figlet_format("Division",font = "bulbhead" )
            print (division_numbers)
            try:
                #Get two numbers from the user 
                div_num_1 = float(input("Please enter first number: "))
                print(emoji.emojize(':divide:'))
                div_num_2 = float(input("Please enter second number: "))
                #Perform the operation
                quotient_numbers = div_num_1/div_num_2
                #Display the result
                print(emoji.emojize(':heavy_equals_sign:'))
                print("\u001b[34;1mThe quotient of two numbers is: ",quotient_numbers,"\n")
            
            #Add Error Handling
            except ValueError:
                print("\u001b[31;1mDo not put letters. Input numbers. Try again!")
            except ZeroDivisionError:
                print("\u001b[31;1mYou cannot input 0 on the second number. Try again!")
        
        #Ask the user if they want to try again 
        try_again = input("\u001b[37;1mDo you want to use the program again? \n[Yes] if continue \n[No] if exit \nEnter option: ")
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
            print(emoji.emojize('Have a good day! :grinning_face:'))
            break
        
except ValueError:
    print("\u001b[31;1mDo not put letters. Input numbers. Try again!")
    try_again = input("\u001b[37;1mDo you want to use the program again? \n[Yes] if continue \n[No] if exit \nEnter option: ")
        #If they want to try again
    if try_again == "Yes":
        #Repeat the program
        menu()
        option = int(input("\nEnter your option: ")) 
    #If they do not want to try again
    else:
        #Display Thank you message
        print("\nThank you for using my program! Have a good day!")
        print(emoji.emojize('Have a good day! :grinning_face:'))
          