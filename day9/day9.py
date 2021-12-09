sample9 = 'day9/sample9'

def get_input(name):
    with open(name, 'r') as file:
        data = file.readlines()

    return data


def mk_structure_from_data(data):
    length = len(data)

    for i in range(0, length):
        lst = []
        for j in range(len(data[i])):
            if data[i][j] != '\n':
                lst.append(int(data[i][j]))
        data[i] = lst
    return data


def check_if_lowest(element, adjacents):
    lent = len(adjacents)
    count = 0
    for i in range(0, lent):
        if element < adjacents[i]:
            count += 1
    if count == lent:
        return True
    else:
        return False


def list_low_points(lst):
    lst_length = len(lst)
    low_points = []
    for i in range(0, lst_length):
        lst_lst_length = len(lst[i])
        for j in range(0, lst_lst_length):
            print(lst[i][j])
            adjacents  = []
            if (i-1) >= 0:
                up = lst[i-1][j]
                adjacents.append(up)
            if (i+1) < lst_length:
                down = lst[i+1][j]
                adjacents.append(down)
            if (j-1) >= 0:
                left = lst[i][j-1]
                adjacents.append(left)
            if (j+1) < lst_lst_length:
                right = lst[i][j+1]
                adjacents.append(right)
            
            
            if check_if_lowest(lst[i][j], adjacents):
                low_points.append([lst[i][j], i, j])
            print(adjacents)
        print("*****************************")
    return low_points



def risk_level(low_points):
    sum = 0
    for element in low_points:
        sum += element[0] + 1
    return sum


def find_adjacents(matrix, low_point, x, y):

    pass



def find_basin(matrix, low_points):
    basins = []
    lst_length = len(matrix)
    lst_lst_length = len(matrix[0])

    for element in low_points:
        low_point = element[0]
        x = element[1]
        y = element[2]
        
        adjacents  = [low_point]
        if (x-1) >= 0:
            if matrix[x-1][y] < 9:
                up = [matrix[x-1][y], x-1, y]
                adjacents.append(up)
        if (x+1) < lst_length:
            if matrix[x+1][y] < 9:
                down = [matrix[x+1][y], x+1, y]
                adjacents.append(down)
        if (y-1) >= 0:
            if matrix[x][y-1] < 9:
                left = [matrix[x][y-1], x, y-1]
                adjacents.append(left)
        if (y+1) < lst_lst_length:
            if matrix[x][y+1] != 9:
                right = [matrix[x][y+1], x, y+1]
                adjacents.append(right)
        
        for element in adjacents:
            
            for el in element:
                if type(el) == int:
                    basins.append(el)
                else:
                    basins.append(el)

    print(basins)

    




def main():
    input = get_input(sample9)
    print(input)

    mk_structure_from_data(input)
    
    print(input)

    low_points = list_low_points(input)

    print(low_points)

    total_rick = risk_level(low_points)
    print(total_rick)

    basins = find_basin(input, low_points)



if __name__ == "__main__":
    main()