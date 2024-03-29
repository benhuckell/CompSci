
from abc import abstractmethod


class Sorting:

    @abstractmethod
    def bubble_sort_backwards(nums):

        index = savedIndex = 1

        while index < len(nums):
            savedIndex = index

            while (nums[index] < nums[index-1] and index > 0):
                nums[index], nums[index-1] = nums[index-1], nums[index]

                index -= 1

            index = savedIndex+1
        
        return nums

    @abstractmethod
    def bubble_sort(nums):
        n = len(nums)

        for i in range(n-1):
            
            for j in range(n-i-1):

                if(nums[j]>nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        
        return nums

    @abstractmethod
    def selection_sort(nums):
        
        n = len(nums)
        for i in range(n-1):
            #find the min element
            minIndex = i
            for j in range(i,n):
                if(nums[j] < nums[minIndex]):
                    minIndex = j

            #swap min with i'th
            nums[minIndex], nums[i] = nums[i], nums[minIndex]

        return nums


    @abstractmethod
    def merge_sort(nums):
        Sorting.merge_sort_recursion(nums,0,len(nums)-1)
        return nums

    @abstractmethod
    def merge_sort_recursion(nums, leftIndex, rightIndex):
        if(leftIndex == rightIndex): #base case
            return

        splitIndex = (leftIndex + rightIndex) // 2
        Sorting.merge_sort_recursion(nums, leftIndex, splitIndex)
        Sorting.merge_sort_recursion(nums, splitIndex+1, rightIndex)
        Sorting.merge(nums,leftIndex,splitIndex,rightIndex)

        return nums
    
    
    @abstractmethod
    def merge(nums, leftIndex, splitIndex, rightIndex):

        #Create a copy of nums
        tempArr = []
        for i in range(len(nums)):
            tempArr.append(nums[i])

        # Define temporary counter variables so as to not overwrite our original left/right index trackers
        tempLeft = leftIndex
        tempRight = splitIndex + 1
        current = leftIndex

        # merge and overwrite nums
        while(tempLeft <= splitIndex and tempRight <= rightIndex):
            if(tempArr[tempLeft] <= tempArr[tempRight]):
                nums[current] = tempArr[leftIndex]
                tempLeft += 1
            else:
                nums[current] = tempArr[tempRight]
                tempRight += 1

            current += 1

        # Copy rest of left half array if it exists
        for i in range(tempLeft, splitIndex+1):
            nums[current] = tempArr[i]
            current += 1

        return

    
    @abstractmethod
    def quick_sort(nums):
        Sorting.quick_sort_recursive(nums,0,len(nums)-1)
        return nums

    @abstractmethod
    def quick_sort_recursive(nums,left,right):

        if(left < right):

            pivotIndex = Sorting.partition(nums,left,right)

            Sorting.quick_sort_recursive(nums,left,pivotIndex-1)
            Sorting.quick_sort_recursive(nums,pivotIndex+1,right)

        return nums
            

    @abstractmethod
    def partition(nums,left,right):

        pivot = nums[right]

        i = left - 1

        for j in range(left,right+1):
            if(nums[j] < pivot):
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            
        #swap pivot with element at i
        nums[right], nums[i+1] = nums[i+1], nums[right]
        
        return i+1

    @abstractmethod
    def counting_sort(nums):

        maxVal = 0
        for i in range(len(nums)):
            maxVal = max(maxVal, nums[i])

        count = [0]*(maxVal+1)
        for i in range(len(nums)):
            count[nums[i]] += 1

        for i in range(1,len(count)):
            count[i] += count[i-1]

        index = 0
        current = 0
        while index <= maxVal:
            if(current < count[index]):
                nums[current] = index
                current += 1
            index += 1
            
        return nums

    @abstractmethod
    def counting_sort_digit(nums,exp):

        # get least significant digit
        count = [0]*10
        for i in range(len(nums)):
            newVal = nums[i]//exp
            digit = newVal % 10
            count[digit] += 1

        # Create continuous count array
        for i in range(1,len(count)):
            count[i] += count[i-1]

        # Create a duplicate empty array to nums
        output = [0]*len(nums)

        # Populate output based on where each value should go (from looking at count array)
        i = len(nums)-1
        while i >= 0:
            index = (nums[i]//exp)%10
            output[count[index]-1] = nums[i]
            count[index] -= 1
            i -= 1

        # Copy output back to nums
        for i in range(len(output)):
            nums[i] = output[i]

        return nums


    @abstractmethod
    def radix_sort(nums):

        # Find max value so that we know the max number of digits
        maxValue = max(nums)

        exp = 1
        while maxValue / exp > 1:
            Sorting.counting_sort_digit(nums,exp)
            exp *= 10

        return nums


if __name__ == "__main__":
    arr = [72,5,1,4,1,3,2]
    sortedArr = Sorting.radix_sort(arr)
    print(sortedArr)