def selectionSort(numbers):
   for fillslot in range(len(numbers)-1,0,-1):
       largestNumber=0
       for location in range(1,fillslot+1):
           if numbers[location]>numbers[largestNumber]:
               largestNumber = location

       temp = numbers[fillslot]
       numbers[fillslot] = numbers[largestNumber]
       numbers[largestNumber] = temp

numbers = [12,11,10,9,8,7,2,1,4,6,5,3]
selectionSort(numbers)
print(numbers)
