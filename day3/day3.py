

filename = "day3/input"

def find_most_common(arr):
    count_0 = 0
    count_1 = 0
    for c in arr:
        if c == '0':
            count_0 += 1
        if c == '1':
            count_1 += 1
    return '1' if count_1 > count_0 else '0'


def least_common(lst):
    # EPSILON RATE
    return '0' if lst == '1' else '1'

def count(n, obj):
    count0 = 0
    count1 = 0
    
    for j in range(0, len(obj)):
        if obj[j][n] == '1':
            count1 += 1
        elif obj[j][n] == '0':
            count0 += 1
    return count0, count1

def popi(n, obj, s):
    for j in range(len(obj) -1, -1, -1):
        if obj[j][n] == s:
            obj.pop(j)

def most_common(obj):
    count0 = 0
    count1 = 0
    for n in range (0, len(obj[0])-1):
        if len(obj) == 1:
            break
        count0, count1 = count(n, obj)
        print(count0, count1)
        if count1 == count0:
            popi(n, obj, '0')
        if count0 > count1:
            popi(n, obj, '1')
        if count1 > count0:
            popi(n, obj, '0')
    print(obj)
    return(obj[0])

def leasst_common(obj):
    count0 = 0
    count1 = 0
    for n in range (0, len(obj[0])-1):
        if len(obj) == 1:
            break
        count0, count1 = count(n, obj)
        print(count0, count1)
        if count1 == count0:
            popi(n, obj, '1')
        if count0 > count1:
            popi(n, obj, '0')
        if count1 > count0:
            popi(n, obj, '1')
    print(obj[0])
    return(obj[0])


def main():

    with open(filename, 'r') as file:
        data = file.readlines()
    lst = str(data)
    ogr = (data)
    mst_common = ''
    lst_common = ''

    for i in range(0, len(data[0]) - 1):
        arr = ''
        for j in range(0, len(data)- 1):
            arr += data[j][i]
        obj = find_most_common(arr)
        mst_common += obj
        lst_common += least_common(obj)

    print(mst_common)
    print(lst_common)
    
    mst_dec = int(mst_common, 2)
    lst_dec = int(lst_common, 2)
    
    print(mst_dec, lst_dec)
    print(mst_dec * lst_dec)

    ogr2 = data
    oxygen_gen = int(most_common(ogr), 2)

    print( " oxygen generator: ", oxygen_gen)

    with open(filename, 'r') as file:
        data = file.readlines()
    print(data)
    ogr2 = data
    CO2 = int(leasst_common(ogr2),2)

    print( " co2 rating: ", CO2)
    
    print( oxygen_gen* CO2)


if __name__ == "__main__":
    main()