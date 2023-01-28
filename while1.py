
is_running = True
number_of_tries = 3
while is_running:
    answer = input("What is the meaning of life?...\n")
    if answer == "42":
        print("Correct! Well done!\n")
        # correct answer, so exit loop - reset is_running
    else:
        print("Sorry that is the wrong answer.... "
              "Try again!\n")

        number_of_tries -= 1

    # check number of tries and break if none left
    if number_of_tries == 0:
        print("You have run out of goes. Sorry.")
        break
x = input("Press any key to exit.")

'''
# assertion test case 1
answer = love then loop executes

# assertion test case 2
answer = 42 results in Correct! Well done!
'''