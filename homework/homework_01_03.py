import random

hand_choice_list = ["가위","바위","보"]

user_score = 0
com_score = 0
winner = "?"

def who_is_winner(user,com):
    user_index = hand_choice_list.index(user)
    com_index = hand_choice_list.index(com)
    diff_between_user_and_com = user_index - com_index

    if(diff_between_user_and_com == 1 or diff_between_user_and_com == -2):
        return "user"
    elif(diff_between_user_and_com == -1 or diff_between_user_and_com == 2):
        return "com"
    else:
        return "draw"

def update_score(winner):
    global user_score
    global com_score

    if(winner == "user"):
        user_score += 1
    elif(winner == "com"):
        com_score += 1

while user_score < 3 and com_score < 3:
    user_select = input("{} 중 선택 : ".format(",".join(hand_choice_list)))
    com_select = random.choice(hand_choice_list)

    while user_select not in hand_choice_list:
        print("{} 중에만 고르시오.".format(",".join(hand_choice_list)))
        user_select = input()

    update_score(who_is_winner(user_select,com_select))

    print("my : {} / com : {}".format(user_select,com_select))
    print("my score : {} / com score : {}".format(user_score,com_score))

    if(user_score == 3):
        winner = "User"
    elif(com_score == 3):
        winner = "Computer"

print("{} win!!".format(winner))