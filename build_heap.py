# python3


def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n // 2, -1, -1):
        j = i
        while True:
            l = 2 * j + 1
            r = 2 * j + 2
            if l < n and data[l] < data[j]:
                j = l
            elif r < n and data[r] < data[j]:
                j = r
            else:
                break
        if i != j:
            swaps.append((i, j))
            data[i], data[j] = data[j], data[i]
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    # input from keyboard
    text = input("I or F:")
        if "I" in text:
            n = int(input())
            data = list(map(int, input().split()))
            assert len(data) == n
        elif "F" in text:
            f = input()
            test ='./tests/'
            file = test+f
            with open(file, 'r') as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))
                assert len(data) == n
        else:
            print("Invalid input. Please enter I or F")
            return

 
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) <= 4 * n

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        
        print(i, j)


if __name__ == "__main__":
    main()
