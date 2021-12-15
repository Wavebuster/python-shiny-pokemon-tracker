import csv
import shiny_tracker_methods as stm

print('Welcome to the Shiny Pokemon Tracker! Please select an option.')
user_choice = ''
loop = True

while loop:
    print('To view a list of your currently obtained shinies enter 1.')
    print('To see what percentage of the Pokedex you have obtained shiny enter 2.')
    print('To report a newly obtained shiny enter 3.')
    print('To regenerate the file where your info is stored enter 4.')
    print('To exit enter 0.')
    print('NOTE: option 4 will erase all previous shiny Pokemon entries')
    user_choice = input().lower()

    if user_choice == '1':
        stm.list_shinies()
    elif user_choice == '2':
       stm.percent_shinies()
    elif user_choice == '3':
        stm.add_shiny()
    elif user_choice == '4':
        user_choice = input('Executing this option will rewrite your entire data file, losing all previous progress. Press 1 to continue, or any other key to cancel.')
        if user_choice == '1':
            write_csv()
        else:
            continue
    elif user_choice == '0' or 'q' or 'quit' or 'exit':
        loop = False
    else:
        print("Invalid choice. Please enter the given options, or type 0 or Q to quit.")

    print('\n')