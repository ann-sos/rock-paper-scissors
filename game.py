from random import choice


def is_winner(g_opt, u_option):
    c_option = choice(g_option)
    if u_option == c_option:
        print("There is a draw ({})".format(c_option))
        return "draw"

    u_index = g_opt.index(u_option)
    if u_index != 0:
        new_g = g_opt[u_index+1:] + g_opt[:u_index]
    else:
        new_g = g_opt[u_index+1:]
    winning_half = new_g[0:int(len(new_g) / 2)]
    if c_option in winning_half:
        print("Sorry, but the computer chose {}".format(c_option))
        return "loss"
    else:
        print("Well done. The computer chose {} and failed".format(c_option))
        return "win"


user_name = input("Enter your name: ")
user_rating = 0
print("Hello,", user_name)
played_before = False
for line in open("rating.txt", "r"):
    if user_name in line:
        user_rating = int(line.split(" ")[1])
        played_before = True
        break
g_option = input().split(",")
if g_option[0] == "":
    g_option = ["rock", "paper", "scissors"]
option_num = len(g_option)
print("Okay, let's start")


while True:
    comp_option = choice(g_option)
    user_input = input()
    if user_input == "!exit":
        print("Bye!")
        break
    elif user_input == "!rating":
        print("Your rating: ", user_rating)
        continue
    elif user_input not in g_option:
        print("Invalid input")
        continue
    result = is_winner(g_option, user_input)
    if result == "win":
        user_rating += 100
    elif result == "draw":
        user_rating += 50
    elif result == "loss":
        pass


if played_before:
    with open("rating.txt", "w+") as F:
        for line in open("rating.txt", "r+"):
            if user_name in line:
                F.write(line.replace(line.split(" ")[1], str(user_rating)))
                break
else:
    with open("rating.txt", "a") as F:
        new_score = user_name + " " + str(user_rating)
        F.write(new_score)
