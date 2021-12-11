
sample_file11 = 'day11/sample11'


def get_input(filename):
    with open(filename) as file:
        data = file.readlines()

    return data



def make_structure_from_data(data):
    matrix = []
    for line in data:
        lst = []
        
        for i in range(0, len(line)):
            if line[i] != '\n':
                lst.append(int(line[i]))
        matrix.append(lst)
    
    return matrix



def step(matrix):
    for i in range(0, len(matrix)):
        for j in range(9, len(matrix[i])):
           matrix[i][j] += 1
    return matrix



def flash(matrix, x, y):
    if matrix[x][y] > 9:
        
        length = len(matrix)
        height = len(matrix[x])


        # center line x
        matrix[x][y] = 0
        
        if y - 1 >= 0:
                matrix[x][y-1] += 1
        if y + 1 < height:
                matrix[x][y+1] += 1



        # line x - 1
        if x - 1 >= 0:
            matrix[x-1][y] += 1
            if y - 1 >= 0:
                matrix[x-1][y-1] += 1
            if y + 1 < height:
                matrix[x-1][y+1] += 1



        #down line x + 1

        if x + 1 < length:
            matrix[x+1][y] += 1
            if y + 1 < height:
                matrix[x+1][y+1] += 1
            if y - 1 <= 0:
                matrix[x+1][y-1] += 1


    return matrix




def check_flashes(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] > 9:
                matrix = flash(matrix, i, j)

    return matrix



def sample11():
    sample = get_input(sample_file11)
    matrix = make_structure_from_data(sample)
    for i in range(0, 3):
        matrix = step(matrix)
        matrix = check_flashes(matrix)
        for element in matrix:
            print(element)
        print()
    #print(matrix)



def main():
    sample11()


if __name__ == "__main__":
    main()