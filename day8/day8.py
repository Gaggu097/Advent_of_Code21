from itertools import permutations
filename = 'day8/input'

sample_output = ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']
sample_signal = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']

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



def map_signal(signal):

    # seven_segments = {"cf": 1,      "acf": 7,"bcdf": 4,"abcdefg": 8,    "acdeg": 2,"acdfg": 3, "abdfg": 5,      "abcefg": 0,"abdefg": 6,"abcdfg": 9,}
    segments = {}
    new_mapping = {}
    element_2 = ''; element_3 = ''; element_4 = ''
    for i in range(0, len(signal)):
        if len(signal[i]) == 2:
            element_2 = signal[i]
        elif len(signal[i]) == 3:
            element_3 = signal[i]
        elif len(signal[i]) == 4:
            element_4 = signal[i]
        for element in signal[i]:
            if element not in segments:
                segments[element] = 1
            else:
                segments[element] += 1
    """ print(signal)
    print(segments)
    print(element_2, element_3, element_4, '\n')"""

    v4 = ''; v6 = ''; v9 = ''
    for k, v in segments.items():
        if v == 4:
            #print(k, v)
            v4 = k
        if v == 6:
            #print(k, v)
            v6 =  k
        if v == 9:
            #print(k, v)
            v9 = k
            """print(element_2)
            print(element_2.replace(k, ''))
            print(element_2)"""
    c8 = element_2.replace(v9, '')
    #print(element_2.replace(v9, ''))
    nine = 'abcdefg'.replace(v4, '')
    eight = 'abcdefg'
    three = nine.replace(v6, '')
    two = eight.replace(v9, '')
    two = two.replace(v6, '')
    five = eight.replace(v4, '')
    five = five.replace(c8, '')
    one = element_2
    seven = element_3
    four = element_4
    six = eight.replace(c8, '')
    d7 = four.replace(v9, '')
    d7 = d7.replace(c8, '')
    d7 = d7.replace(v6, '')
    zero = eight.replace(d7, '')
    #print(zero, one, two, three, four, five, six, seven, eight, nine,)

    new_mapping = {
        zero : 0,
        one : 1,
        two : 2,
        three : 3,
        four: 4,
        five : 5,
        six : 6,
        seven: 7,
        eight: 8,
        nine : 9,
    }
    
    return new_mapping


def decode(signal, output):
    num_lst = [0]*len(signal)
    for i in range(0, len(signal)):
        map = map_signal(signal[i])
        # print(map)
        for j in range(0, 4):
            a = output[i][j]
            perm = permutations(a)
            perm = list(perm)
            lst = []
            for k in range(0, len(perm)):
                ls = ''
                for l in range(0, len(perm[k])):
                    ls += perm[k][l]
                lst.append(ls)
            # print(lst)
            for element in lst:
                if element in map:
                    # print(map[element])
                    num_lst[i] += map[element] * pow(10, 3-j)
    return num_lst

def main():
    input = get_input()

    output, signal = mk_structure_from_data(input)

    # print(output, signal)
    sum_elements = count_unique_digits(output)
    print(sum_elements)
    
    
    lst = decode(signal, output)
    print(lst)
    sum = 0
    for element in lst:
        sum += element

    print(sum)


if __name__ == "__main__":
    main()