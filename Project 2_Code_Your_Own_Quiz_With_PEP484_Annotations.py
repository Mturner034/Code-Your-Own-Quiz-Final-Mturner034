
blanks = ["__1__", "__2__", "__3__", "__4__", "__5__"]

easy_answers = ["browser", "HTML", "moon", "flat", "crazy"]
medium_answers = ["elon musk", "tesla", "spacex", "spacex", "mars"]
hard_answers = ["singularity", "theory", "man", "intelligence", "technology"]

easy_quiz =   """We use a __1__ to view web pages. The language used to code webpages is called __2__. People used to think the __3__ was made of cheese. There are a group of people that still believe the earth is __4__ and they are what we call __5__."""
medium_quiz = """The name of the man who founded SpaceX is __1__. He also founded two other companies called __2__, and __3__. The ultimate goal of __4__ is to make humans a multi-plantary species by colonizing __5__."""
hard_quiz =   """The technological __1__ is a __2__ that predicts __3__ merging with artificial __4__ due to the exponential __5__ of technology."""

welcome = "\nYou have chosen chosen a {dummy} level. Let us begin your voyage in to the goblin bridges of Middle Earth.\n"

def getuserlevel():
      """getuserlevel() with PEP 484 type annotations.

    Input:
          (None)
    Behavior:
        User is welcomed to the quiz with greeting message and story.
        User is asked to choose difficulty.
        Checks user answer.
        If correct difficulty is not chosen, asks user again to choose.
        If correct difficuly is chosen, corresponding quiz and answers list launched.      
    Return:
        answers (list): The corresponding answers list
        quiz (str): The corresponding quiz

    """
    levels = ["easy", "medium", "hard"]
    chosen_level = raw_input("\nPlease choose a level between easy, medium, and hard.\n>")
    while chosen_level not in levels: 
      chosen_level = raw_input("That is not a level choice.Please choose a level between easy, medium, and hard.")
    if chosen_level == "easy":
        print welcome.format(dummy=chosen_level)
        return easy_quiz, easy_answers             
    elif chosen_level == "medium":
        print welcome.format(dummy=chosen_level)
        return medium_quiz, medium_answers
    elif chosen_level == "hard":
        print welcome.format(dummy=chosen_level)
        return hard_quiz, hard_answers
    else:
        print "Invalid input."

def what_is_your_name():
     """what_is_your_name(0 function) with PEP 484 type annotations.

    Input:
        name: Asks for user name.
    Behavior:
        Function launches greeting message. Asks the user for their name.
    Return:
        Greeting message and asks for name.

    """
  name = raw_input("Welcome.\n \nThe year is 2037.\n \nA malicious computer virus has wiped out the world's financial and electric systems.\n \nYou have been summoned to complete a quiz to save mankind.\n \nThe completion of quiz will be your chance, to give mankind hope,\ninspire millions, and lead human civilization\ninto a new age of prosperity and enlightenment.\n \nBefore we begin, what is your name?\n> ")
  return name 

def run_quiz():
    """run_quiz  with PEP 484 type annotations:

    Input:
        (None) 
    Behavior:
        Checks user input for name and quiz. 
        Checks if user answer is wrong, the same quiz is returned.
        User asked to enter answer again.
        If answer is correct, the quiz is returned and the blank is filled in with correct answer.
        User is asked to enter answer for next blank.
        Loop runs until all answers are completed.
        Completed quiz prints.
        User is congratulated.         
    Return:
        None.

    """
    name = what_is_your_name()
    quiz, answers = getuserlevel()
    index = 0
    limit = len(answers)
    while index < limit:
        print quiz
        user_answer = raw_input("Please enter your answer for {}\n".format(index+1))
        while user_answer != answers[index]:
            print "Wrong"
            user_answer = raw_input("\nPlease enter your answer again {}\n".format(index+1))
        quiz = quiz.replace(blanks[index], user_answer)
        index += 1
    print quiz 
    print "\nThe prophecy has been fulfilled. You have implemented the cure. You have saved all of mankind. You have been rewarded $10,000,000.\n"
run_quiz()