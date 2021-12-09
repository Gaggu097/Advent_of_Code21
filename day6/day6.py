
filename = 'day6/input'
DAYS = 256

input_sample = [3,4,3,1,2]

def get_input():
    with open(filename, 'r') as file:
        data = file.readlines()

    input = data[0].split(',')
    for i in range(0, len(input)):
        input[i] = int(input[i])

    return input
        
def make_list(input):
    lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, ]
    for item in input:
        if item == 0:
            lst[0] += 1
        elif item == 1:
            lst[1] += 1
        elif item == 2:
            lst[2] += 1
        elif item == 3:
            lst[3] += 1
        elif item == 4:
            lst[4] += 1
        elif item == 5:
            lst[5] += 1
        elif item == 6:
            lst[6] += 1
        elif item == 7:
            lst[7] += 1
        elif item == 8:
            lst[8] += 1
        
    return lst



def calc_population(lst, days):
    for d in range(0, days):
        elements_0 = lst[0]
        for item in range(1, 9):
            lst[item-1] = lst[item]
        lst[8] = elements_0
        lst[6] += elements_0


    return lst


def sum_population(lst):
    sum = 0
    for element in lst:
        sum += element

    return sum

def main():
    input = get_input()
    print(input_sample)

    lst1 = make_list(input)
    print(" 0, 1, 2, 3, 4, 5, 6, 7, 8")
    print(lst1)
    population = calc_population(lst1, DAYS)
    print(population)
    sum = sum_population(lst1)
    print(sum)



if __name__ == "__main__":
    main()