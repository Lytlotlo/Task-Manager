#The function of this program is to help a buisness manage its tasks.
   
#=====importing libraries===========
#I've used the open function to open task.txt and user.txt and retrived
#the lines in the tasks for further use.

with open('tasks.txt', 'r') as task:
    for line in task:
        format_for_task = line
                    
with open('user.txt', 'r') as users:
        login_information = str(users.readlines())
        login_information = login_information.replace("\n", "")
        login_information = login_information

    
#====Login Section====       
#I've used the input function to enter a username and a password.
#If the password and username is not the same as any of the passoword and username in the
#user.txt document, program will prompt you to enter password and username till
#it's correct.

print("Login information is case sensitive.")
username = input("Enter Username:")
password = input("Enter Password:")
user_login = username + (",") + (" ") + password
number_of_tasks = 0
while user_login not in login_information:
    print("Incorrect Username and password. Try again")
    username = input("Enter Username:")
    password = input("Enter Password:")
    user_login = username + (",") + (" ") + password
if user_login in login_information:
        
#presenting the menu to the user and   
# making sure that the user input is coneverted to lower case.
#If the user selects any of the letters below in the menu the program will head
#them to what each of the letters stand for.
#the menu for admin directs the admin to a second menu, where only the admin can
#display statistics and register users.

    menu = input('''Select one of the following Options below:
    m - Menu for admin user(To register user and display statistics.)
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()

#In the menu for admin if the user is not an admin and wants to register a user    
#the program will print "only admin can register users.

    while menu == 'm' and username == "admin":
        admin_menu = input('''        r - Register a user
        s - Display statistics
        :''').lower()
        if admin_menu == 'r':                 
              the_new_username = input("Enter new username:")
              the_new_password = input("Enter new password:")
              the_new_password_confirmation = input("Re-enter new password:")
              while the_new_password != the_new_password_confirmation:
                  print("The new passwords entered do not match. Re-enter the same passowrd.")
                  the_new_password = input("Enter new password:")
                  the_new_password_confirmation = input("Re-enter new password:")
              if the_new_password == the_new_password_confirmation:
                  the_new_username_and_password = "\n" + the_new_username + "," + " " + the_new_password 
                  with open('user.txt', 'a+') as users:
                       users.write(the_new_username_and_password)
                       
                  #Go back to menu    
                  menu = input('''Select one of the following Options below:
m - Menu for admin user(To register user and display statistics.)
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
                               
#This statement (s) counts the number of tasks and users.            
#For every line that the user is not the same as the next line 1 is added so that
#every user is counted.
     
        else:
            count_of_tasks = 0
            count_of_users = 0
            
            with open('tasks.txt', 'r') as task:
                for line in task:
                    count_of_tasks = count_of_tasks + 1
                    
            with open('user.txt', 'r') as users:
                for line in users:
                    count_of_users = count_of_users + 1
                    
            print("Number of tasks:", count_of_tasks)
            print("Number of users:", count_of_users)
            
            #Go back to menu
            menu = input('''Select one of the following Options below:
m - Menu for admin user(To register user and display statistics.)
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
               
    if menu == 'm' and user_login != "admin, adm1n":
            print("Only admin is allowed to select the admin menu.")
            #Go back to menu
            menu = input('''Select one of the following Options below:
m - Menu for admin only(To register user and display statistics.)
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
    
                               
#If the user selects (a) they will be able to add a task.
#I combined the details of the task into the variable new_task in the same format as
#the lines in the task.txt file.
#I used to open the file with 'a' which stands for append and adds the details to the
#file and inserted a \n to to new_task to add the details to a newline.
            
    while menu == 'a':
        username_of_the_person_assigned_to = input("Enter the username of the person the task is assigned to:")
        the_title_of_the_task = input("Enter title of the task:")
        the_description_of_the_task = input("Describe the task:") 
        the_due_date_of_the_task = input("Enter the due date of the task in the format YYYY-MM-DD :")
        the_current_date = input("Enter the current date of the task in the format YYYY-MM-DD:")
        task_completion = "No"
        new_task =  (username_of_the_person_assigned_to
                +(", ")
                + the_title_of_the_task
                +(", ")
                + the_description_of_the_task
                +(", ")
                + str(the_due_date_of_the_task)
                +(", ")
                + str(the_current_date)
                +(", ")
                + task_completion)
        with open('tasks.txt', 'a') as task:
            task.write(str("\n" + new_task))
            task.close()
            #Go back to menu
            menu = input('''Select one of the following Options below:
m - Menu for admin user(To register user and display statistics.)
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
            
           

#If the user selects va, they'll be able to view all the tasks in the task.txt file.
#I used the split, list and format function to edit the tasks so that it is displayed in a
#user friendly manner.
        
    while menu == 'va':
        with open('tasks.txt', 'r') as task:
            for line in task:
                format_for_task = line
                format_for_task = format_for_task.split(",")
                format_for_task = list(format_for_task)
                format_for_task = '''_________________________________________________________________________
Task:                   {}
Assigned to:             {}
Date assigned:          {}
Due date:               {}
Task Complete?          {}
Task description:
{}
_________________________________________________________________________'''.format(format_for_task[1]
                                                                                 , format_for_task[0]
                                                                                 , format_for_task[3]
                                                                                 , format_for_task[4]
                                                                                 , format_for_task[5].replace("\n", "")
                                                                                 , format_for_task[2])
            
               
                
                
                print(format_for_task)
            #Go back to menu
            menu = input('''Select one of the following Options below:
m - Menu for admin user(To register user and display statistics.)
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
            
#If the users select vm they'll be able to view their tasks.
#The first word of the task details is the username.
#I edited the details using the split,list function so that I may get the                
#username in tasks.txt file.
#If the username in tasks.txt is the same as the username entered by user it will print
#task belonging to username.

    while menu == 'vm':
        with open('tasks.txt', 'r') as task:
            for line in task:
                format_my_task = line
                format_my_task = format_my_task.split(",")
                format_my_task = list(format_my_task)
                if username == format_my_task[0]:
                    number_of_tasks = number_of_tasks + 1
                    format_my_task = '''_________________________________________________________________________
Task:                   {}
Assigned to:             {}
Date assigned:          {}
Due date:               {}
Task Complete?          {}
Task description:
{}
__________________________________________________________________________'''.format(format_my_task[1]
                                                                                , format_my_task[0]
                                                                                , format_my_task[3]
                                                                                , format_my_task[4]
                                                                                , format_my_task[5].replace("\n", "")
                                                                                , format_my_task[2])
                
                    print(format_my_task)
                    
            print("Number of tasks =", number_of_tasks)
            #Go back to menu
            menu = input('''Select one of the following Options below:
m - Menu for admin user(To register user and display statistics.)
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
                               
#If user selects 'e' the program will exit because of the exit() function.
    
    while menu == 'e':
        print('Goodbye!!!')
        exit()       
#If user selects none of the choices presented.                
    else:
        print("You have made a wrong choice, Please Try again")

        




