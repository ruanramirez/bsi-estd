def fibonacci(number):
    arr = [0, 1]
    if number == 1:
        print('0')
    elif number == 2:
        print('[0,','1]')
    else:
        while(len(arr)< number):
            arr.append(0)
        if(number == 0 or number == 1):
            return 1
        else:
            arr[0] = 0
            arr[1] = 1
            for i in range(2, number):
                arr[i] = arr[i-1] + arr[i-2]
            return sum(arr)

print(fibonacci(7))
