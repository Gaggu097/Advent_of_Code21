init_state = [3, 4, 3, 1, 2]
DAYS = 80

filename = "day6/input"

def stuff(inputs):
    print("Initial state: ", inputs)
    for day in range(1, DAYS + 1):
        for i in range(0, len(inputs)):
            # print(init_state[i])

            if inputs[i] == 0:
                inputs[i] = 6
                inputs.append(8)
            
            else:
                inputs[i] -= 1
        if day == 1:
            print(f"After {day} day ", inputs)   
        else:
            print(f"After {day} days ", inputs)
    
    print(len(inputs))

    

def main():
    with open(filename, 'r') as file:
        data = file.readlines()

    #print(data)

    input = data[0].split(',')
    #print(input)
    for i in range(0, len(input)):
        input[i] = int(input[i])
        
    #print(input)

    """print("Initial state: ", init_state)
    for day in range(1, DAYS + 1):
        for i in range(0, len(init_state)):
            # print(init_state[i])

            if init_state[i] == 0:
                init_state[i] = 6
                init_state.append(8)
            
            else:
                init_state[i] -= 1
        if day == 1:
            print(f"After {day} day ", init_state)   
        else:
            print(f"After {day} days ", init_state)
    
    print(len(init_state))"""

    stuff(input)


if __name__ == "__main__":
    main()

