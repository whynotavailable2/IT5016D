from datetime import datetime

score = 0
start_time = datetime.today()
answer_one = (input("What is the capital of New Zealand?\n\n"))
if answer_one.lower() == "wellington":
    score = score + 1
    print("\nThat is correct. Your current score is ", score, "\n\n")
else:
    print("\nThat is incorrect. Your current score is still", score, "\n\n")
answer_two = (input("What is the Maori name for New Zealand?\n\n"))
if answer_two.lower() == "aotearoa":
    score = score + 1
    print("\nThat is correct. Your current score is ", score, "\n\n")
else:
    print("\nThat is incorrect. Your current score is still", score, "\n\n")
answer_three = (input("What is the name of the New Zealand Rubgy team?\n\n"))

if answer_three.lower() == "all blacks":
    score = score + 1
    print("\nThat is correct. Your current score is ", score, "\n\n")
else:
    print("\nThat is incorrect. Your current score is still", score, "\n\n")
answer_four = (input("The colours of the New zealand flag are red, blue and ?????\n\n"))

if answer_four.lower() == "white":
    score = score + 1
print("\nThat is correct. Your current score is ", score, "\n\n")
else:
print("\nThat is incorrect. Your current score is still", score, "\n\n")
answer_five = (input("what is the international dialing code for New Zealand?\n\n"))

if answer_five.lower() == "64":
    score = score + 1
    print("\nThat is correct. Your current score is ", score, "\n\n")
else:
    print("\nThat is incorrect. Your current score is still", score, "\n\n")
print("\nYour final score is ", score, "\n\n")
print("The time taken for you to complete this quiz is....", datetime.today() - start_time)
# Testing
'''
print("My assertions are:"
      "\nanswer_one = wellington output = score = 1"
      "\nanswer_one = Wellington output = score = 1"
      "\nanswer_one = Auckland output = score = 0"
      "\nanswer_two = aotearoa output = score = 2"
      "\nanswer_three = All Blacks output = score = 3"
      "\nanswer_four = white output = score = 4"
      "\nanswer_five = 64 output = score = 5", Your final score is 5)
'''