import re

SEP = ";"
USER = 0
LOG = 1
TIME = 2

# get the logs
def get_logs():
    logs = []
    with open("log.txt", "r") as file:
        for line in file:
            line = line.strip().split(SEP)
            logs.append(line)
    return logs


# get the users
def get_users(logs):
    users = []
    for log in logs:
        user = log[USER]
        if user not in users:
            users.append(user)
    return users

# get the users log times

def get_user_logtimes(logs, users):
    times_logged_in = {}
    for user in users:
        user_login_time = 0
        user_logout_time = 0
        for log in logs:
            if log[USER] == user:
                if log[LOG] == " logged in":
                    user_login_time = log[TIME]
                elif log[LOG] == " logged out":
                    user_logout_time = log[TIME]
        times_logged_in[user] =int(user_logout_time) - int(user_login_time)
    return times_logged_in

# get user for logged most time
def get_user_most_logged_time(logged_times):
    max_time = 0
    user = ""
    for key in logged_times:
        if logged_times[key] > max_time:
            max_time = logged_times[key]
            user = key
    return user

# how many time a user checked their balance

def get_user_balance_check(logs, users):
    balance_check = {}
    for user in users:
        user_balance_check = 0
        for log in logs:
            if log[USER] == user:
                if log[LOG] == " checked their balance":
                    user_balance_check += 1
        balance_check[user] = user_balance_check
    return balance_check

# get the logs where the user performed a payment

def get_user_nr_of_payments(logs, users):
    payments = {}
    for user in users:
        user_nr_of_payments = 0
        for log in logs:
            if log[USER] == user:
                if  " performed a payment" in log[LOG]:
                    user_nr_of_payments += 1
        payments[user] = user_nr_of_payments
    return payments


# get average of user payments

def get_user_average_payment(user_nr_of_payments,users):
    payments_total_nr = 0
    for user in users:
        payments_total_nr += user_nr_of_payments[user]
    return payments_total_nr / len(users)


# get user who spent the most money
def get_user_spent(logs, users):
    spent = {}
    for user in users:
        user_spent = 0
        for log in logs:
            if log[USER] == user:
                if " performed a payment" in log[LOG]:
                    user_spent += int(re.search(r'\d+', log[LOG]).group())  # get the number from the log , used regex, |d+ means one or more digits,.group() returns the matched string
        spent[user] = user_spent
    return spent


# get user who spent the most money
def get_user_spent_most(user_spent):
    max_spent = 0
    user = ""
    for key in user_spent:
        if user_spent[key] > max_spent:
            max_spent = user_spent[key]
            user = key
    return user


# get how much each user received
def get_user_received(logs, users):
    received = {}
    for user in users:
        user_received = 0
        for log in logs:
            if log[USER] == user:
                if " received" in log[LOG]:
                    user_received += int(re.search(r'\d+', log[LOG]).group())
        received[user] = user_received
    return received

# get the user who received the most money
def get_user_received_most(user_received):
    max_received = 0
    user = ""
    for key in user_received:
        if user_received[key] > max_received:
            max_received = user_received[key]
            user = key
    return user


# everyones balance if it was 0 at the beginning
def get_user_balance(logs, users):
    balance = {}
    for user in users:
        user_balance = 0
        for log in logs:
            if log[USER] == user:
                if " performed a payment" in log[LOG]:
                    user_balance -= int(re.search(r'\d+', log[LOG]).group())
                elif " received" in log[LOG]:
                    user_balance += int(re.search(r'\d+', log[LOG]).group())
        balance[user] = user_balance
    return balance


# write the logs to a file
def write_logs_to_file(logs, users, users_logtimes, user_logged_most, 
                       users_balance_check, users_nr_of_payments, 
                       average_payment_per_user, users_spending, 
                       user_whos_spent_most, users_receiving, 
                       user_who_received_most, users_final_balance, filename="users_logs.txt"):
    
    with open(filename, "w") as file:
       
        file.write("User Logs Report\n")
        file.write("****************\n\n")
        
        # users
        file.write("Users:\n")
        for user in users:
            file.write(f"{user}\n")
        file.write("\n")

        # users log times
        file.write("Users log times:\n")
        for user, logtime in users_logtimes.items():
            file.write(f"{user} - {logtime}\n")
        file.write("\n")

        # the user who stayed logged the most  the most
        file.write(f"User who logged the most: {user_logged_most}\n\n")

        # users balance checks
        file.write("Users balance check:\n")
        for user, balance in users_balance_check.items():
            file.write(f"{user} - {balance}\n")
        file.write("\n")

        # number of payments per user
        file.write("Number of payments per user:\n")
        for user, payments in users_nr_of_payments.items():
            file.write(f"{user} - {payments}\n")
        file.write("\n")

        # average payment per user
        file.write(f"Average payment per user: {average_payment_per_user}\n\n")

        # users spending
        file.write("Users spending:\n")
        for user, spending in users_spending.items():
            file.write(f"{user} - {spending}\n")
        file.write("\n")

        # the user who spent the most
        file.write(f"User who spent the most: {user_whos_spent_most}\n\n")

        # users receiving
        file.write("Users receiving:\n")
        for user, receiving in users_receiving.items():
            file.write(f"{user} - {receiving}\n")
        file.write("\n")

        # the user who received the most
        file.write(f"User who received the most: {user_who_received_most}\n\n")

        # users final balance
        file.write("Users final balance:\n")
        for user, balance in users_final_balance.items():
            file.write(f"{user} - {balance}\n")
        file.write("\n")
        
    

logs = get_logs()
users = get_users(logs)
users_logtimes = get_user_logtimes(logs, users)
user_logged_most = get_user_most_logged_time(users_logtimes)
users_balance_check = get_user_balance_check(logs, users)
users_nr_of_payments = get_user_nr_of_payments(logs, users)
average_payment_per_user = get_user_average_payment(users_nr_of_payments, users)
users_spending = get_user_spent(logs, users)
user_whos_spent_most = get_user_spent_most(users_spending)
users_receiving = get_user_received(logs, users)
user_who_received_most = get_user_received_most(users_receiving)
users_final_balance = get_user_balance(logs, users)

write_logs_to_file(logs, users, users_logtimes, user_logged_most, 
                   users_balance_check, users_nr_of_payments, 
                   average_payment_per_user, users_spending, 
                   user_whos_spent_most, users_receiving, 
                   user_who_received_most, users_final_balance)
