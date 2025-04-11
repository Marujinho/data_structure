class Binary_search:

    def __init__(self):
        pass

    def iterative_binary_search(self, numbers:list, target:int):
        left,right = 0, len(numbers)-1

        while left < right:
            mid = left + (right - left) // 2

            if target == numbers[mid]:
                return mid
            
            elif target > numbers[mid]:
                left = mid
            else:
                right = mid

        return -1


    def recursive_binary_search(self, numbers:list, target:int, low:int, high:int):
        if low > high:
            return -1

        mid = low + (high - low) // 2

        if numbers[mid] == target:
            return mid

        elif numbers[mid] > target:
            return self.recursive_binary_search(numbers, target, low, mid-1)
        
        else:
            return self.recursive_binary_search(numbers, target, mid+1, high)




