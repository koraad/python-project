def integer_validation(message, error_message="Integer required"):  # to validate if the input is an integer
    while True:
        try:
            credit = int(input(message))
        except ValueError:
            print(error_message)
            continue
        break
    return credit


def range_validation(message, error_message=f"out of range: enter a credit within the range [0, 20, 40, 60, 80, 100, 120]"):
    # to validate if the input is in the given range
    range = [0, 20, 40, 60, 80, 100, 120]
    while True:
        credit_score = integer_validation(message)
        if credit_score not in range:
            print(error_message)
            continue
        break
    return credit_score


count_progress = 0  # total number of progress outcomes
count_trailing = 0  # total number of trailing outcomes
count_retriever = 0  # total number of retriever outcomes
count_exclude = 0  # total number of exclude outcomes

total_students = 1  # total number of outcomes

print("Staff Version with Histogram")

credit_scores_progress = []
credit_scores_trailing = []
credit_scores_retriever = []
credit_scores_exclude = []

while True:  # to calculate progression outcomes for multiple students

    while True:  # to validate if the total credit score is equal to 120
        pass_credits = range_validation("Please enter your credits at pass: ")
        defer_credits = range_validation("Please enter your credits at defer: ")
        fail_credits = range_validation("Please enter your credits at fail: ")

        total_credits = pass_credits + defer_credits + fail_credits

        if total_credits != 120:
            print("Total incorrect")
            continue
        break

    # to determine the student's progression outcome
    if pass_credits == 120:
        print("Progress")
        credit_scores_progress.append([pass_credits, defer_credits, fail_credits])
        count_progress += 1
    elif pass_credits == 100:
        print("Progress (module trailer)")
        credit_scores_trailing.append([pass_credits, defer_credits, fail_credits])
        count_trailing += 1
    elif pass_credits + defer_credits <= 40:
        print("Exclude")
        credit_scores_exclude.append([pass_credits, defer_credits, fail_credits])
        count_exclude += 1
    else:
        print("Module Retriever")
        credit_scores_retriever.append([pass_credits, defer_credits, fail_credits])
        count_retriever += 1

    while True:  # to validate the input is "y" or "q"
        next_call = input('''
Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results:
        ''')
        possible_options = ["y", "q"]
        if next_call.lower() not in possible_options:
            print("Invalid input: Please only enter 'y' or 'q'")
            continue
        break

    if next_call.lower() == "y":
        total_students += 1
        continue
    elif next_call.lower() == "q":

        progress_stars = count_progress * "*"
        trailing_stars = count_trailing * "*"
        retriever_stars = count_retriever * "*"
        exclude_stars = count_exclude * "*"

        print(f'''
---------------------------------------------------------------
Horizontal Histogram
Progress {count_progress} : {progress_stars}
Trailer {count_trailing} : {trailing_stars}
Retriever {count_retriever} : {retriever_stars}
Excluded {count_exclude} : {exclude_stars}
{total_students} outcomes in total.
----------------------------------------------------------------        

        ''')

        for scores in credit_scores_progress:
            print(f"Progress - {scores}")
        for scores in credit_scores_trailing:
            print(f"Progress (module trailer) - {scores}")
        for scores in credit_scores_retriever:
            print(f"Module retriever - {scores}")
        for scores in credit_scores_exclude:
            print(f"Exclude - {scores}")

        break