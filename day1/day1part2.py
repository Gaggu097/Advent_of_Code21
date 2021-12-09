filename = 'day1/input'

def main():
    with open(filename, 'r') as file :
        data = file.readlines()
    
    sum_list = []
    count = 0
    for i in range (0, len(data)):
        if i + 2 < len(data):
            sum = int(data[i]) + int(data[i+1]) + int(data[i+2])
        sum_list.append(sum)

    for i in range (len(sum_list)-1):
        if sum_list[i+1] > sum_list[i]:
            count += 1
    print(count)

if __name__ == "__main__":
    main()