def bubbleSort(numbers):
    count = 0
    for num in range(len(numbers)-1,0,-1):
        for i in range(num):
            if numbers[i]>numbers[i+1]:
                temp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp
        count += 1
        print(count)

numbers = [11,12,10,7,3,2,5,4,6,8,9,6,1]
bubbleSort(numbers)
print(numbers)