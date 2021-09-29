from art import tprint
import json
import random
import os
import time as t

def save_in_json(user, score) :
    file = "user.json"
    if os.path.exists(file) :
        with open(file, 'r') as r :
            user_dict = json.load(r)
        
        user_dict[score] = user

        new_dict = sorted(user_dict.items(), reverse=True)
        new_dict = dict(new_dict)
        
        with open(file, 'w') as w :
            json.dump(new_dict, w, indent=4)
    else :
        user_dict = {}
        user_dict[score] = user
        with open(file, 'w') as w :
            json.dump(user_dict, w, indent=4)

def top_scorers() :
    file = "user.json"
    with open(file, 'r') as r :
        user_dict = json.load(r)
    i = 1
    for key, value in user_dict.items() :
        if i<4 :
            i = str(i)
            print(i + '. ' + value + ' => ' + key)
        i = int(i)
        i = i+1

def save_user() :
    user = input("\nEnter your name : ")
    return user

def guess_number() :
    print("Guess a number : ")
    while True :
        try :
            user_answer = int(input())
            break
        except :
            os.system('cls')
            print("Guess a number : ")
    return user_answer

def play_again() :
    while True :
        print("Do you want to play again (y/Y or n/N) : ")
        choice = input()
        if choice == 'y' or choice == 'Y' :
            os.system('cls')
            main_game()
        elif choice == 'n' or choice == 'N' :
            print("Thanks for playing...!")
            exit()
        else :
            print("Not a valid input, Try again...!")
            t.sleep(2)

def menu() :
    os.system('cls')
    tprint("NUMBER GUESSING\nGAME")
    print("\nWelcome to number guessing game...\n")
    print("Please go through the rules before starting it => \n")
    print("""    1. You have to enter a range and we choose a random number between this range.
    2. You have to guess that choosen number.
    3. Score starts from 98 points and for each wrong guess 5 points is deducted.
    4. We will give you hints during the guessing of number.
    5. You have to maintain a minimum score of 40 points, if points become less than 40 than you loose.""")

def main_game() :
    menu()
    user = save_user()
    os.system('cls')
    print("\nWelcome {}, Enjoy the game, Best of luck...!\n".format(user))
    print("Enter the starting point of range : ")
    while True :
        try :
            start = int(input())
            break
        except :
            print("It takes only numbers\nEnter Again...!\n")
            t.sleep(2)
            os.system('cls')
            print("\nWelcome {}, Enjoy the game, Best of luck...!\n".format(user))
            print("Enter the starting point of range : ")

    print("Enter the ending point of range : ")
    while True :
        try :
            end = int(input())
            break
        except :
            print("It takes only numbers\nEnter Again...!\n")
            t.sleep(2)
            os.system('cls')
            print("Your starting point of range is : {}".format(start))
            print("Enter the ending point of range : ")
    
    if start > end :
        start, end = end, start
    
    num_list = []
    for num in range(start, end+1) :
        num_list.append(num)
    random_answer = random.choice(num_list)
    os.system('cls')
    print("A number has been choosen from {} to {}\n".format(start, end))

    score = 98
    while True :
        user_answer = guess_number()
        real_score = score
        if real_score > 40 :
            if user_answer < random_answer :
                os.system('cls')
                print("Guess a higher number...!")
                score = score - 5
                print("Your score is {}".format(score))
            elif user_answer > random_answer :
                os.system('cls')
                print("Guess a smaller number...!")
                score = score - 5
                print("Your score is {}".format(score))
            elif user_answer == random_answer :
                os.system('cls')
                print("Congratulations {}, Your answer is correct...!".format(user))
                print("Your score is {}".format(score))
                save_in_json(user, str(score))
                print("Top scorers =>\n")
                top_scorers()
                x = input("Press Enter to continue...!\n")
                os.system('cls')
                play_again()
        elif real_score <= 40 :
            os.system('cls')
            print("You loose the game...!")
            print("Your score is less than 40")
            t.sleep(2)
            os.system('cls')
            play_again()

main_game()