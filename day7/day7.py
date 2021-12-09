

filename = 'day7/input'
sample_input = [16,1,2,0,4,2,7,1,2,14]


def get_input():
    with open(filename, 'r') as file:
        data = file.readlines()

    input = data[0].split(',')
    for i in range(0, len(input)):
        input[i] = int(input[i])

    return input


def find_max_value(lst):
    max = 0
    for i in range(0, len(lst)):
        if lst[i] > max:
            max = lst[i]
    return max


def find_min_value(lst):
    min = lst[0]
    j = 0
    for i in range(0, len(lst)):
        if lst[i] < min:
            min = lst[i]
            j = i
    return min, j

def modulo(i):

    return i if i > 0 else -i


def calculate_fuel_cost(lst, position):
    fuel_cost = 0
    for i in range (0, len(lst)):
        #added this here for part 2
        fuel_cost +=  calc_fuel_per_step( modulo((lst[i]) - position))
    return fuel_cost


# day 7 part 2
def calc_fuel_per_step(i):
    fuel_per_step = 0
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        for i in range(1, i+1):
            fuel_per_step = fuel_per_step + i
        return fuel_per_step


def make_fuel_cost_list(lst, positions):
    fuel_cost_lst = []

    for i in range(0, positions):
        fuel_cost = calculate_fuel_cost(lst, i)

        fuel_cost_lst.append(fuel_cost)

    return fuel_cost_lst


def main():
    input = get_input()
    # print(input)

    # first part
    m = find_max_value(sample_input)
    print(m)

    print(calculate_fuel_cost(sample_input, 2))

    sample_fuel_cost_list = make_fuel_cost_list(sample_input, m)

    print(sample_fuel_cost_list)

    best, position = find_min_value(sample_fuel_cost_list)

    print(best, position)
    

    # second part
    print(input)
    mx = find_max_value(input)
    print(mx)
    fuel_cost_lst = make_fuel_cost_list(input, mx)
    print(fuel_cost_lst)
    fuel, position = find_min_value(fuel_cost_lst)
    print(fuel, position)


if __name__ == "__main__":
    main()