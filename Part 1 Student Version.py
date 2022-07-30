def integer_validation(message, error_message = "Integer required"): #to validate if the input is an integer
    while True:
        try:
            credit = int(input(message))
        except ValueError:
            print(error_message)
            continue
        break
    return credit

def range_validation(message, error_message = f"Out of range: enter a credit within the range [0, 20, 40, 60, 80, 100, 120]"):
    #to validate if the input is in the given range
    range = [0, 20, 40, 60, 80, 100, 120]
    while True:
        credit_score = integer_validation(message)
        if credit_score not in range:
            print(error_message)
            continue
        break
    return credit_score


while True:#to validate if the total credit score is equal to 120
    pass_credits = range_validation("Please enter your credits at pass: ")
    defer_credits = range_validation("Please enter your credits at defer: ")
    fail_credits = range_validation("Please enter your credits at fail: ")

    total_credits = pass_credits + defer_credits + fail_credits

    if total_credits != 120:
        print("Total incorrect")
        continue
    break

#to determine the student's progression outcome
if pass_credits == 120:
    print("Progress")
elif pass_credits == 100:
    print("Progress (module trailer)")
elif pass_credits + defer_credits <= 40:
    print("Exclude")
else:
    print("Module Retriever")