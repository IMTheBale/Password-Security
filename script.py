password_length = 6
counter = 1
permutations = 1

while counter <= password_length:
    permutations *= counter
    counter += 1
print(f"The possible combination of a {password_length}-character password is: {permutations}")

attempts = 5
max_lock = permutations/attempts
max_lock = int(max_lock)
print(f"The maximum number of times the account might be locked is {max_lock} times.")

locks = 0
total_lock_time = 0
lock_time_multiplier = 5
for i in range(max_lock):
    locks += 1
    total_lock_time += lock_time_multiplier * locks
    print(f"Your account is locked for {lock_time_multiplier*locks} minutes")
    
print(f"Assuming the hacker only got the password right with the last possible combination, your account would have been locked for {total_lock_time} minutes in total.")