import ctypes

"""
    A dynamic array is basically an array with variable size.
    The required properties:
        1. create array
        2. append
        3. delete last item
        4. get item
        5. resizing (key factor)
        6. make the array with revised size.
"""

class DynamicArray(object):
    def __init__(self) -> None:
        self.n = 0 # counter variable to indicate actual number of items so far
        self.capacity = 1 # indicator variable to denoting the size of the array. default 1.
        self.A = self.make_array(self.capacity)
    
    def __len__(self):
        return self.n

    def append(self, item):
        if self.n==self.capacity:
            self._resize(2 * self.capacity)
        
        self.A[self.n] = item
        self.n+=1
    
    def get_item(self, idx):
        """
            returning item at index 'idx'
        """
        if idx<0 or idx>self.n:
            return f"{idx} is out of bound"
        
        return self.A[idx]

    def pop(self):
        """
            deleting the last item from the list. to do so, just downgrading the number
            of element by 1.
        """
        if self.n==0:
            return "Cannot delete, array is empty!"
        self.n-=1

    def _resize(self, new_capacity):
        """
            usually, in dynamic array, the array size is doubled if no. of items
            match the capacity. I will create a new array with new_capacity.
            then I will copy the items of the old array to new array and then will
            just re-initiate the new array (like swap) with the old array. so the
            old array will be same size as the new array and will also keep its
            already inserted elements intact. lastly, I will update the capacity of
            old array with new_capacity.
        """
        B = self.make_array(new_capacity)

        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacity = new_capacity

    def make_array(self, new_capacity):
        """
            to make array, I am going to use ctype python
            object and also will multiply the number of object
            with the new_capacity
        """
        return (new_capacity * ctypes.py_object)()

if __name__ == '__main__':
    arr = DynamicArray()
    arr.append(1)
    arr.append(4)
    arr.append(2)
    arr.append(3)
    print("The length of the array is: ", arr.__len__())
    for idx in range(arr.__len__()):
        print(arr.get_item(idx))
    
    arr.pop()
    arr.pop()
    print("After deleting two items, the length of this array is now: ", arr.__len__())
    print("Now, the remaining items are:")
    for idx in range(arr.__len__()):
        print(arr.get_item(idx))