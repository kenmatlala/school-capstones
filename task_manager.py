from datetime import datetime
from time import mktime
from datetime import date
from time import strptime


# ====Login Section====
#  code will allow a user to login.
#  code will read usernames and password from the user.txt file
#  validate your username and password.


def register():
    if menu == 'r':
        pass
        validate = []
        with open('user.txt', 'r', encoding='utf-8') as read_file:
            for line in read_file:
                validate.append(line.split(", ")[0])

        # we request new username to attach to txt file, and for them to place a password and confirm it
        while True:
            new_User = input('Please input new username:\n')

            if new_User not in validate:

                new_User_password = input('Please enter new user Password:\n')
                password_confirmation = input('please reenter password for confirmation:\n')
                # if passwords are not the same it will request user to renter password

                if new_User_password != password_confirmation:
                    print('passwords do not match, please reenter:\n')
                # when all conditions are met it will add new data onto user txt file
                elif new_User_password == password_confirmation:
                    j = ('\n' + new_User + ', ' + new_User_password)
                    with open('user.txt', 'a') as newCredentials:
                        newCredentials.write(j)
                break
            else:
                print("User already exists")


def assignments():
    if menu == 'a':
        pass
        # new var for the storage of data we will need to add to list
        task_assign = input('who is assigned to the task: \n')
        task_title = input('what is the task title: \n')
        task_description = input('write a description of the task: \n')
        # collecting today's date with the date time input
        Today = date.today()
        str_today = Today.strftime("%d %b %Y")
        task_dueDate = input('when is the dask due as (dd mm yyyy \n')
        complete = 'No'
        # taking all the new data and adding it to our text file
        with open('tasks.txt', 'a', encoding='utf-8') as task_info:
            task_info.write('\n' + task_assign + ', ' + task_title + ', ' + task_description + ', '
                            + str_today + ', ' + task_dueDate + ', ' + complete)


# if user selects menu the chain of events must occur
def view_all_tasks():
    if menu == 'va':
        pass
        # we are calling out all the tasks from text file tasks.txt
        with open('tasks.txt', 'r', encoding='utf-8') as task_read:
            for ilink in task_read:
                line = ilink.split(', ')
                # printing out all the saved tasks in the list in readable format
                print(f'''
Task:              {line[1]}
Assigned to:       {line[0]}
Date assigned:     {line[3]}
Due date:          {line[4]}
Task Complete?     {line[5]}
Task description:
 {line[2]}''')


def view_my_tasks():
    if menu == 'vm':
        pass
        # we and the user to view the task once they are done
        # we open the file and if user is the same as the user logged in then we show them all their tasks
        with open('tasks.txt', 'r', encoding='utf-8') as task_read:
            act = 1
            ind = 1
            listing = {}
            new_list = []
            keys = []

            for itask in task_read:
                line = itask.strip("\n").split(', ')
                listing[ind] = line
                ind += 1
            task_read.seek(0)

            for itask in task_read:
                line = itask.split(', ')
                # listing[ind] = line
                if line[0] == UserName:
                    # printing out the saved list in readable format
                    print(f'''
                    ---------Task{act}--------
                            Task:              {line[1]}
                            Assigned to:       {line[0]}
                            Date assigned:     {line[3]}
                            Due date:          {line[4]}
                            Task Complete:     {line[5]}
                            Task description:
                            {line[2]} ''')
                    act += 1

            # The below code is allowing the user to edit the task.
            while True:
                user_input = int(input(f'\n ----------------- NEW MENU ------------------ \n '
                                       'If you wish to edit a file enter task number:\n'
                                       f' Or if you wish to return to menu punch in -1: \n'))
                if user_input == -1:
                    break

                user_choice = input(f'''\n
 ---- SELECT AN OPTION:----
m - Mark the task as complete
e - edit the task.\n''')

                if user_choice.lower() == "m":
                    listing[user_input][5] = "Yes"

                elif user_choice.lower() == "e":
                    new_list_menu = input('-------edit---------\n'
                                          'n - to edit name:\n'
                                          'd - to edit  date:\n')
                    # Checking if the user input is equal to 'n'
                    if listing[user_input][5] == 'Yes':
                        print('Task has already been completed')
                        break
                    elif new_list_menu == 'n':

                        # Opening the file user.txt and reading the file.
                        while True:
                            with open('user.txt', 'r') as usernames:
                                for lines in usernames:
                                    x = lines.strip('\n').split(', ')
                                    keys.append(x[0])

                            name_change = input('Who is the new task assigned to:\n')

                            # The above code is checking if the name change is in the keys. If it is, it will change the
                            # name in the listing.
                            if name_change in \
                                    keys:
                                listing[user_input][0] = name_change
                                break

                    elif new_list_menu == 'd':
                        new_date = input('Please enter new Date dd/month/yyyy: \n')
                        listing[user_input][4] = new_date

                print(keys)

            for key in listing:
                new_list.append(listing[key])

            with open('tasks.txt', 'w', encoding='utf-8') as folder:
                for i_liner in new_list:
                    x = ', '.join(i_liner)
                    folder.write(x + '\n')


def generate_report():
    # variable storages
    num_task_total = 0
    line_list = []
    new_line_list = 0
    dates_completion = []
    overdue = 0
    date_format = '%d %b %Y'

    with open('tasks.txt', 'r', encoding='utf-8') as taskDoc:
        # This is looping through the taskDoc and appending the line to the line_list.
        for line in taskDoc:
            line_list.append(line.strip('\n').split(', '))
            num_task_total += 1

        # This is looping through the line_list and checking if the last item in the list is equal to 'Yes'.
        #  If it is, it will add 1 to the new_line_list.
        for line in line_list:
            if line[-1] == 'Yes':
                new_line_list += 1

        # This is calculating the percentage of tasks that are complete and incomplete.
        incomplete = (num_task_total - new_line_list)
        complete_task_percentage = round((new_line_list / num_task_total) * 100, 2)
        incomplete_task_percentage = round(100 - complete_task_percentage, 2)

        # This is looping through the line_list and appending the date to the dates_completion list.
        for line in line_list:
            dates_completion.append(line[-2])

        # Creating a function for overdue tasks
        for line in line_list:
            xDate = strptime(line[-2], date_format)
            dt = datetime.fromtimestamp(mktime(xDate))
            today_date = datetime.now()
            if line[-1] == 'No' and dt < today_date:
                overdue += 1

        # The above code is creating a string that is formatted with the variables that are defined in the code.
        tsk1 = f'The total number of completed tasks are {num_task_total - incomplete}'
        tsk2 = f'The total amount of uncompleted tasks are {incomplete}'
        tsk3 = f'The total number of tasks overdue are {overdue}'
        tsk4 = f'The total percentage of incomplete tasks are {incomplete_task_percentage}%'
        tsk5 = f'The percentage of tasks that are overdue are {round((overdue / num_task_total) * 100, 2)}%'

        # The below code is opening a file called task_overview.txt and writing the text from the variables tsk1,
        # tsk2, tsk3, tsk4, and tsk5 to the file.
        with open('task_overview.txt', 'w', encoding='utf-8') as text_write:
            text_write.write(f'{tsk1} \n{tsk2} \n{tsk3} \n{tsk4} \n{tsk5}')

            # The below code is printing the tasks that I have to do.
        # print(f'\n \t\t\t------REPORT------\n {tsk1} \n {tsk2} \n {tsk3} \n {tsk4} \n {tsk5}')

        # The above code is creating a dictionary and a list.
        diction = {}
        new_name_listing = []

        # The above code is opening the user.txt file and reading it. It is then stripping the new line character and
        # splitting the string at the comma. It is then appending the first item in the list to the new_name_listing
        # list.
        with open('user.txt', 'r', encoding='utf-8') as user_list:
            for line in user_list:
                me = line.strip('\n').split(', ')
                new_name_listing.append(me[0])

        ind = 0
        # The above code is opening the file tasks.txt and reading it. It is then splitting the file into a list of
        # lists.
        with open('tasks.txt', 'r', encoding='utf-8') as tasks_in:
            for task_key, task in enumerate(tasks_in):
                me = task.strip('\n').split(', ')
                diction[task_key] = me
                ind += 1

        # The above code is writing the total amount of registered users to the file.
        write_val = f"The total Amount Of Registered Users: {len(new_name_listing)}\n"
        # The above code is creating a list of users and then for each user in the list, it is counting the number of
        # tasks that are incomplete and the number of tasks that are complete. It is also counting the number of overdue
        # tasks for each user.
        for us in new_name_listing:
            number_of_tasks_incomplete = 0
            number_of_complete_tasks = 0
            overdue_user = 0
            # The above code is counting the number of tasks that are incomplete and overdue.
            for key in diction:
                if diction[key][0] == us:
                    if diction[key][-1] == "No":
                        number_of_tasks_incomplete += 1

                        xDate = strptime(diction[key][-2], date_format)

                        dt = datetime.fromtimestamp(mktime(xDate))

                        today_date = datetime.now()

                        if diction[key][-1] == 'No' and dt < today_date:
                            overdue_user += 1

                    elif diction[key][-1].lower() == 'yes':
                        number_of_complete_tasks += 1

            num1 = f'\n\t\t\t{us}:\n\n{us} total number of tasks is {number_of_complete_tasks + number_of_tasks_incomplete}\n'
            # Calculating the percentage of tasks completed by each user.
            if number_of_tasks_incomplete == 0 and number_of_complete_tasks == 0:
                num1 += f'{us} has 0% of tasks\n'
            else:
                num1 += f'{us} has {round(((number_of_tasks_incomplete + number_of_complete_tasks) / ind) * 100, 2)}% of total tasks\n'

            # Calculating the percentage of incomplete tasks and adding it to the num1 variable.
            if number_of_tasks_incomplete == 0 and number_of_complete_tasks == 0:
                num1 += f'{us} has 0% incomplete tasks\n'
            else:
                num1 += (
                    f'{us} has {round((number_of_tasks_incomplete / (number_of_complete_tasks + number_of_tasks_incomplete) * 100), 2)}% of his tasks incomplete and must be completed\n')

            # Checking if the number of complete tasks is greater than or equal to 0. If it is, it will pass. If it is
            # not, it will add the percentage of complete tasks to the num1 variable.
            if number_of_complete_tasks >= 0:
                pass
            else:
                num1 += (
                    f'{us} has {round((number_of_complete_tasks / (number_of_complete_tasks + number_of_tasks_incomplete)) * 100, 2)}% of his tasks is complete\n')

            # checking for overdue tasks
            if overdue_user == 0 or number_of_complete_tasks == 0 and number_of_tasks_incomplete == 0:
                num1 += f'{us} has 0% tasks overdue\n'
            else:
                num1 += (
                    f'{us} has {round(((overdue_user / (number_of_complete_tasks + number_of_tasks_incomplete)) * 100), 2)}% of total tasks overdue\n')
            write_val += f"{num1}"

        # storing data in file
        with open('user_overview.txt', 'w', encoding='utf-8') as overview_stuff:
            overview_stuff.write(f'{write_val}\n')


# if admin selects statistics this chain of code will be executed
def statistics():
    print('')
    # new var for storing counts of tasks and users
    taskCount = []
    userCount = []
    # opening task files and checking each 1st var and adding it to count
    with open('tasks.txt', 'r', encoding='utf-8') as task_read:
        for inner in task_read:
            me = inner.strip('\n').split(', ')
            taskCount.append(me)

    # printing out task count
    print('The total amount of tasks is {}'.format(len(taskCount)))

    # opening user files and checking each 1st var and adding it to count
    with open('user.txt', 'r', encoding='utf-8') as task_reader:
        for inner in task_reader:
            me = inner.strip('\n').split(', ')
            userCount.append(me)

    # printing out user count
    print('The total amount of users is {} \n'.format(len(userCount)))
    userover = []
    task_manager = []
    with open('task_overview.txt', 'r', encoding='utf-8') as user:
        for lines in user:
            task_manager.append(lines)

    for lines in task_manager:
        x = lines.strip('\n')
        print(x)

    # The above code is opening the file user_overview.txt and reading the lines in the file.
    with open('user_overview.txt', 'r', encoding='utf-8') as task:
        for lines in task:
            userover.append(lines)

    # The above code is stripping the new line character from the userover file.
    for lines in userover:
        x = lines.strip('\n')
        print(x)


# if user presses 'e' it must exit the program
def exiting():
    if menu == 'e':
        print('Goodbye!!!')
        exit()
    # if user enters the wrong key it must request that they retry
    else:
        print("You have made a wrong choice, Please Try again")


# ---------------------------------------------------------------------------------------------
while True:
    # input variables for logging into programs
    UserName = input('Please enter your user name: \n')
    Password = input('Please enter your Password to log in: \n')
    # a var for storing new text data in list formation
    New_admin = []
    # flag variables
    user_name_flag = False
    password_flag = False
    login_flag = False
    # we are opening the file to collect data from it
    userFile = open('user.txt', 'r', encoding="utf-8")
    for i in userFile:
        New_admin.append(i)

    # if user enters an incorrect admin it must continue requesting that they re-input the correct one
    for i in New_admin:
        n = i.strip("\n").split(', ')
        # conditions for log in
        if UserName == n[0]:
            user_name_flag = True
        if Password == n[1].strip('\n'):
            password_flag = True
        if UserName == n[0] and Password == n[1].strip('\n'):
            login_flag = True
            break

    # if both log in conditions are met break out the loop to menu
    if login_flag:
        print('Access approved \n')
        break
    # if username is incorrect
    if not user_name_flag and password_flag:
        print('Username incorrect! \n Please enter your correct username: \n')
    # if password is incorrect
    elif user_name_flag and not password_flag:
        print('password incorrect \n Please enter correct Password to log in: \n')
    # if both are incorrect
    elif not user_name_flag and not password_flag:
        print(' Both username and password are incorrect please retry')
    # if both are correct but from different lines
    else:
        print("invalid credential")

    userFile.close()

# The below code is a menu that is presented to the user.
while True:
    if UserName == 'admin':
        # presenting the menu to the user and
        # making sure that the user input is converted to lower case.
        menu = input('''\n Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate report
s - statistics
e - Exit
: ''').lower()

    else:
        menu = input('''\n Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
 : ''').lower()

    if menu == 'r':
        register()
    elif menu == 'a':
        assignments()
    elif menu == 'va':
        view_all_tasks()
    elif menu == 'vm':
        view_my_tasks()
    elif menu == 'gr':
        generate_report()
    elif menu == 's':
        statistics()
    elif menu == 'e':
        exiting()
