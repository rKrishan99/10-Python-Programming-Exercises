class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []  # List to hold stack items

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        """Remove and return the top item of the stack."""
        if not self.is_empty():
            popped_item = self.items.pop()  # Remove the last item from the list
            print(f"Popped: {popped_item}")
            return popped_item
        else:
            print("Stack is empty, cannot pop.")
            return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def peek(self):
        """Return the top item of the stack without removing it."""
        if not self.is_empty():
            return self.items[-1]  # Return the last item
        else:
            return None


def is_balanced_parentheses(s):
    """Check if the parentheses in the string are balanced."""
    stack = Stack()  # Create a new stack to hold the opening parentheses
    # Mapping of closing parentheses to their corresponding opening ones
    parentheses_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in parentheses_map.values():  # If it is an opening parenthesis
            stack.push(char)  # Push it onto the stack
        elif char in parentheses_map.keys():  # If it is a closing parenthesis
            if stack.is_empty() or stack.pop() != parentheses_map[char]:
                return False  # Unmatched closing parenthesis
    return stack.is_empty()  # Return True if no unmatched opening parentheses remain


def main():
    """Main program loop to check for balanced parentheses."""
    while True:
        input_str = input("Enter a string of parentheses (or 'exit' to quit): ")
        if input_str.lower() == 'exit':
            print("Exiting the program.")
            break
        if is_balanced_parentheses(input_str):
            print("The parentheses are balanced.")
        else:
            print("The parentheses are not balanced.")


if __name__ == "__main__":
    main()
