def insertionSort(numbers):
   for num in range(1,len(numbers)):

     currentvalue = numbers[num]
     position = num

     while position>0 and numbers[position-1]>currentvalue:
         numbers[position]=numbers[position-1]
         position = position-1

     numbers[position]=currentvalue

numbers = [11,12,10,9,8,7,2,1,4,6,5,3]
insertionSort(numbers)
print(numbers)