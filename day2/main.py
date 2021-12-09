import os

filename = "day2/input"

def move (current_x, current_y, current_aim, str, n):
    if str == "forward":
        current_x += n
        current_y += current_aim * n
    elif str == 'down':
        #current_y += n
        current_aim += n
    elif str == 'up':
        #current_y -= n
        current_aim -= n
    return current_x, current_y, current_aim

def main():
    with open(filename, 'r') as file:
        data = file.readlines()
    
    matrix = list()

    for i in range(0, data.__len__()):
        matrix.append(data[i].split())

    x = 0
    y = 0
    aim = 0
    for lst in matrix:
        x, y, aim = move (x, y, aim, lst[0], int(lst[1]))
        print("x: ", x, "y: ", y, "aim: ", aim)
    
    print(x, y)
    print(x * y)

if __name__ == "__main__":
    main()
