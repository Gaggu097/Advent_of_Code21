from itertools import permutations

filename = 'day8/sample'
sample_lst = ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']



def get_input():
    with open(filename, 'r') as file:
        data = file.readlines()

    return data



def mk_structure_from_data(data):
    # make readable structure of data from file (data)
    output_lst = []
    signal_lst = []
    for i in range(0, len(data)):
        #print(data[i])
        data[i] = data[i].split('|')
        #print(data[i])
        #print("*******************************************************")
    
    
    for i in range(0, len(data)):
        output_lst.append(data[i][1].split())
        signal_lst.append(data[i][0].split())
    return output_lst, signal_lst



def get_digit(strr):
    length = len(strr)
    lst = []
    for i in range(0,length):
        lst.append(strr[i])
    print(lst)
    if length == 2:
        return 1

    elif length == 3:
        return 7
    elif length == 4:
        return 4
    elif length == 7:
        return 8


    elif length == 5:
        """
        5 cdf be
        3 cdf ba
        2 cdf ag
        """
        if 'b' in lst:
            if 'a' in lst:
                return 5
            else:
                return 3
            
        if 'g' in lst:
            return 2
        
    elif length == 6:
        """
        9 cbed fa
        6 cbed fg
        0 cbed ag
        """
        if 'f' in lst:
            if 'a' in lst:
                return 9
            else:
                return 6
        elif 'a' in lst:
            return 0



def get_numeric_value(lst):
    num_lst = []

    for element in lst:
        # print(element)
        n = get_digit(element)
        # print(n)
        num_lst.append(n)
    num = num_lst[0] * 1000 + num_lst[1] * 100 + num_lst[2] * 10 + num_lst[3] * 1
    print(num)
    return num


def count_unique_digits(lst):
    digit_count = [0, 0, 0, 0]
    for i in range(0, len(lst)):
        for j in range(0, len(lst[i])):
            length = len(lst[i][j])
            if length == 2:
                digit_count[0] += 1
            if length == 4:
                digit_count[1] += 1
            if length == 3:
                digit_count[2] += 1
            if length == 7:
                digit_count[3] += 1
    one = digit_count[0]
    four = digit_count[1]
    seven = digit_count[2]
    eight = digit_count[3]

    return one + four + seven + eight



def map_signal(signal_list):
    pass


def main():
    input = get_input()

    output, signal = mk_structure_from_data(input)

    print(output, signal)
    sum_elements = count_unique_digits(output)
    print(sum_elements)

    for element in signal:
        get_numeric_value(element)



if __name__ == "__main__":
    main()