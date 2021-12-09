import os
filename = 'day1/input'

"""cwd = os.getcwd()
files = os.listdir(cwd)
print(f"files in {cwd}: {files}")
"""
def main():
    with open(filename, 'r') as file:
        data = file.readlines()

    count = 0
    for i in range(0, len(data)-1):
        if int(data[i + 1]) > int(data[i]):
            count += 1
    print(count)


if __name__ == "__main__":
    main()