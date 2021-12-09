filename = 'day4/sample'


def get_sample():
    with open(filename) as file:
        data = file.readlines()
    
    r_bingo = data[0]
    r_bingo = r_bingo.split(',')
    for i in range(0, len(r_bingo)):
        r_bingo[i] = int(r_bingo[i])
    boarda = [data[i: i+6] for i in range(1, len(data), 6)]


    for i in range(0, len(boarda)):
        for j in range(1, len(boarda[i])):
            boarda[i][j] = boarda[i][j].strip('\n').split()
        boarda[i].pop(0)
    
    for i in range(0, len(boarda)):
        for j in range(0, len(boarda[i])):
            for k in range(0, len(boarda[i][j])):
                boarda[i][j][k] = int(boarda[i][j][k])
    return r_bingo, boarda



def make_marker_board(number_of_boards):
    marker_board = [[[0]*5]*5]*number_of_boards
    return marker_board

def check_winner_row(lst):
    checker = [1,1,1,1]
    for x in range(len(lst)):
        for y in range(len(lst[x])):
            if checker in lst[x][y]:
                print ('yers')




def main():
    r_bingo, boards = get_sample()
    n = (len(boards))
    marker_board = make_marker_board(n)

    """for element in r_bingo:
        for x in range(0, len(boards)):
            for y in range(0, len(boards[x])):
                for z in range(0, len(boards[x][y])):
                    if element == boards[x][y][z]:
                        print('yes')
                        marker_board[x][y][z] = 1
        for element in marker_board:
            print(element)
        print("**********************")"""

    check = [[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],]

    check_winner_row(check)

if __name__ == "__main__":
    main()