import time
from datetime import date
import os
import shutil

def establish_src():
    parent_dir_path = os.path.dirname(__file__)
    count = 0
    today = date.today()
    subDir = f'{today}_{count}'
    num_csv = 0
    for item in os.listdir(parent_dir_path):
        if '.csv' in item:
            num_csv += 1
            csvFile = item
    if num_csv != 1:
        print('Something is wrong with your CSV file. Make sure it is present. Make sure no other CSV files are present.')
        quit()
    while subDir in os.listdir(parent_dir_path):
        count += 1
        subDir = f'{today}_{count}'
    os.mkdir(f'{parent_dir_path}/{subDir}')
    shutil.move(f'{parent_dir_path}/{csvFile}', f'{parent_dir_path}/{subDir}/{csvFile}')
    time.sleep(1)
    src = f'{parent_dir_path}/{subDir}'
    return (src, csvFile)



def prompt_for_message():
    new_line = '%0a'
    final_confirmation = 'no'
    answers = ['yes', 'y', 'no', 'n']

    while final_confirmation == 'no' or final_confirmation == 'n':
        message = f''
        test_message = f''
        finished = 'no'
        while finished == 'no' or finished == 'n':
            message_text = input(f'Type contents of your message, hit enter for a new line in the message. To represent names, type FIRSTNAME and/or LASTNAME. \n\n{test_message}')
            confirm = input('\nDoes that look correct so far? (yes or no): ')
            while confirm not in answers:
                confirm = input('\nDoes that look correct so far? (yes or no): ')
            while confirm == 'no' or confirm == 'n':
                message_text = input(f'Type contents of your message, hit enter for a new line in the message. To represent names, type FIRSTNAME and/or LASTNAME. \n\n{test_message}')
                confirm = input('\nDoes that look correct so far? (yes or no): ')
            message = message + message_text
            test_message = test_message + message_text
            finished = input('Are you finished typing your message? (yes or no): ')
            while finished not in answers:
                finished = input('Are you finished typing your message? (yes or no): ')
            if finished == 'no' or finished == 'n':
                test_message = test_message + '\n'
                message = message + new_line
        
        print('\n', test_message , sep = '')

        final_confirmation = input('\nDoes your message look correct? (yes or no): ')
        while final_confirmation not in answers:
            final_confirmation = input('\n Does your message look correct? (yes or no): ')
        if final_confirmation == 'no' or final_confirmation == 'n':
            print('\nI apologize, please type your message again.')
        if 'FIRSTNAME' not in message:
            first_name_confirmation = input('No first name registered, did you mean to include a first name in your message? (yes or no): ')
            while first_name_confirmation not in answers:
                first_name_confirmation = input('No first name registered, did you mean to include a first name in your message? (yes or no): ')
            if first_name_confirmation == 'yes' or first_name_confirmation == 'y':
                print('\nSomething went wrong. Retry and make sure you include FIRSTNAME in message!\n')
                final_confirmation = 'no'
                time.sleep(2)
        if 'LASTNAME' not in message:
            last_name_confirmation = input('No last name registered, did you mean to include a last name in your message? (yes or no): ')
            while last_name_confirmation not in answers:
                last_name_confirmation = input('No last name registered, did you mean to include a last name in your message? (yes or no): ')
            if last_name_confirmation == 'yes' or last_name_confirmation == 'y':
                print('\nSomething went wrong. Retry and make sure you include LASTNAME in message!\n')
                final_confirmation = 'no'
                time.sleep(2)

    if 'FIRSTNAME' in message:
        message = message.replace('FIRSTNAME', '{first}')
    if 'LASTNAME' in message:
        message = message.replace('LASTNAME', '{last}')
    print(message)
    return message

        
    
    
