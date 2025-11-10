class MinStack:

    # The idea is to store pairs. The space complexity will be O(n), where n is the number of pairs. Stack operations
    # will remain O(1) in time complexity. Given the constraint that stack operations will ALWAYS be called on
    # non-empty stacks (EXCEPT PUSH), there is no need for stack size validation for those.
    # To calculate the minimum, I will take advantage of Python's built-in min() function.

    def __init__(self):

        # Stack Member
        self.stack = []
        

    def push(self, val: int) -> None:

        # If the stack is not empoty
        if len(self.stack) > 0:

            # Retrieve the current minimum before pushing
            current_min = self.getMin()

            # Push into the stack the pair of given value and the calculated minimum
            self.stack.append((val, min(current_min, val)))
        
        # Otherwise the stack is not empty and just push it with the value
        else:

            # Push into the stack a pair of both the values
            self.stack.append((val, val))

    def pop(self) -> None:

        # Pop from the stack
        self.stack.pop()

    def top(self) -> int:

        # Peek the top of the stack, and return the value (Value element is stored on the LHS aka [0] of the pair)
        return self.stack[-1][0]

    def getMin(self) -> int:

        # Peek the top of the stack, and return the current minimum (Minimum element is stored on the RHS aka [1] of the pair)
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()