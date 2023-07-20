import random
import time
from tqdm import tqdm

board3d = []
for x in range(0, 10):
    board3d.append(" " + str(x))
for x in range(10, 28):
    board3d.append(str(x))

def defaut_board():
    for x in range(0, 10):
        board3d[x] = (" " + str(x))
    for x in range(10, 28):
        board3d[x] = (str(x))

win_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6),
            (9,10,11),(12,13,14),(15,16,17),(9,12,15),(10,13,16),(11,14,17),(9,13,17),(11,13,15),
            (18,19,20),(21,22,23),(24,25,26),(18,21,24),(19,22,25),(20,23,26),(18,22,26),(20,22,24),
            (0,9,18),(1,10,19),(2,11,20),(3,12,21),(4,13,23),(5,14,23),(6,15,24),(7,16,25),(8,17,26),
            (0,10,20),(2,10,18),(2,14,26),(8,14,20),(8,16,24),(6,16,26),(6,12,18),(0,12,24),(3,13,23),
            (5,13,21),(1,13,25),(7,13,19),(0,13,26),(2,13,24),(8,13,18),(6,13,20),(4,13,22)]

def draw():
    print()
    print(board3d[1] + '|' + board3d[2] + '|' + board3d[3] + '\t\t' + board3d[10] + '|' + board3d[11] + '|' + board3d[12] + '\t\t' + board3d[19] + '|' +
          board3d[20] + '|' + board3d[21])
    print('--|--|--' + '\t\t' + '--|--|--' + '\t\t' + '--|--|--')

    print(board3d[4] + '|' + board3d[5] + '|' + board3d[6] + '\t\t' + board3d[
        13] + '|' + board3d[14] + '|' + board3d[15] + '\t\t' + board3d[22] + '|' +
          board3d[23] + '|' + board3d[24])
    print('--|--|--' + '\t\t' + '--|--|--' + '\t\t' + '--|--|--')

    print(board3d[7] + '|' + board3d[8] + '|' + board3d[9] + '\t\t' + board3d[
        16] + '|' + board3d[17] + '|' + board3d[18] + '\t\t' + board3d[25] + '|' +
          board3d[26] + '|' + board3d[27])
    print()


def check_win(player_moves):
    for combination in win_combinations:
        if all(move in player_moves for move in combination):
            return True

    return False

def choice_validation(player_choice):
    valid = 1
    if not player_choice.isnumeric():
        valid = 0
    else:
        if int(player_choice) < 1 or int(player_choice) > 27 or board3d[int(player_choice)] == " X" or board3d[int(player_choice)] == " O":
            valid = 0
    return valid

def main():
    first_player = input("Enter The First Player Name : ")
    second_player = input("Enter The Second Player Name : ")
    first_player_moves = []
    second_player_moves = []
    first_player_score = 0
    second_player_score = 0
    print("Shufelling....")
    for i in tqdm(range(20), desc='tqdm() Progress Bar'):
        time.sleep(0.1)
    shuffle = random.randint(0,1)
    if shuffle == 0:
        print(first_player," Will Play First")
        first_player_token = " X"
        second_player_token = " O"
    else:
        print(second_player," Will Play First")
        first_player_token = " O"
        second_player_token = " X"
    for i in range(shuffle,28):
        draw()
        if i%2 == 1:
            choice = input(second_player + ", In Which Cell Do You Want To Put Your " + second_player_token + " ? >> ")
            valid_choice = choice_validation(choice)
            while valid_choice == 0:
                print("not valid...try again")
                choice = input(second_player + ", In Which Cell Do You Want To Put Your " + second_player_token  + " ? >> ")
                valid_choice = choice_validation(choice)
            board3d[int(choice)] = second_player_token
            second_player_moves.append(int(choice) - 1)
            win = check_win(second_player_moves)
            if win == 1:
                draw()
                print(second_player," \033[35mIs The Winner\033[0m")
                second_player_score+=1
                print("The Score Is : ",first_player_score," For",first_player)
                print("The Score Is : ", second_player_score, " For", second_player)
                print()
                con = input("Do You Want To Continue ? [y/n] > ")
                while con != 'y' and con != 'n':
                    print("You Must Enter Only y Or n ")
                    con = input("Do You Want To Continue ? [y/n] > ")
                if con == 'y':
                    print("We Are Starting a new round")
                    first_player_moves = []
                    second_player_moves = []
                    i = 0
                    defaut_board()
                else:
                    print("Thank You For Playing")
                    return first_player, second_player, first_player_score, second_player_score
                    exit()
        else:
            choice = input(first_player + ", In Which Cell Do You Want To Put Your " + first_player_token + " ? >> ")
            valid_choice = choice_validation(choice)
            while valid_choice == 0:
                print("not valid...try again")
                choice = input(first_player + ", In Which Cell Do You Want To Put Your " + first_player_token + " ? >> ")
                valid_choice = choice_validation(choice)
            board3d[int(choice)] = first_player_token
            first_player_moves.append(int(choice) - 1)
            win = check_win(first_player_moves)
            if win == 1:
                draw()
                print(first_player," \033[32mIs The Winner\033[0m")
                first_player_score+=1
                print("The Score Is : ",first_player_score," For",first_player)
                print("The Score Is : ", second_player_score, " For", second_player)
                print()
                con = input("Do You Want To Continue ? [y/n] > ")
                while con != 'y' and con != 'n':
                    print("You Must Enter Only y Or n ")
                    con = input("Do You Want To Continue ? [y/n] > ")
                if con == 'y':
                    print("We Are Starting a new round")
                    first_player_moves = []
                    second_player_moves = []
                    i = 0
                    defaut_board()
                else:
                    print("Thank You For Playing")
                    if first_player_score > second_player_score:
                        winner = first_player
                    elif first_player_score < second_player_score:
                        winner = second_player
                    else:
                        winner = 'tie'
                    return first_player, second_player, first_player_score, second_player_score , winner
                    exit()


P1,P2,P1s,P2s,W = main()

print(P1,P2,P1s,P2s,W)

# collection.insert_one({"first player name": P1,
#                        "second player name": P2,
#                        "first player score": P1s,
#                        "second player score": P2s,
#                        "Winner": W})