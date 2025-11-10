class Solution:
    def isValid(self, s: str) -> bool:
        
        # O(n) Time & Space Complexity
        
        # Idea: Parse through the string, as there are opening brackets such as "({["
        # Push into the stack. If there are closing brackets such as ")}]" then pop and
        # Compare if valid. Cases in which is invalid is if the bracket is not a match,
        # or the stack attempts to pop when empty

        # Base Case: String is only size 1
        if len(s) == 1:
            return False

        # Stack to store opening brackets
        opening_brackets = []

        # For each char in the string
        for c in s:

            # If the char is part of '({['
            if c in '({[':

                # Push into the stack
                opening_brackets.append(c)

            # Otherwise it is part of ')}]' given s consists only of that
            else:

                # Stack is empty, it will attempt to pop nothing.
                if len(opening_brackets) == 0:
                    return False

                # If the stack is not empty, pop the stack
                opening_bracket = opening_brackets.pop()

                # If valid, then continue and skip the next operations
                if opening_bracket == '(' and c == ')':
                    continue
                if opening_bracket == '{' and c == '}':
                    continue
                if opening_bracket == '[' and c == ']':
                    continue

                # Otherwise return False
                return False

        # By reaching the end, ensure that the stack is empty (each opening has its closing)
        return len(opening_brackets) == 0
                