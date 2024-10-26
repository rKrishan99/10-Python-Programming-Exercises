class Queue:
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []  # List to hold the elements of the queue

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """Remove and return the front item of the queue. If the queue is empty, return None."""
        if self.is_empty():
            print("Queue is empty, cannot dequeue.")
            return None
        dequeued_item = self.items.pop(0)  # Remove the first item
        print(f"Dequeued: {dequeued_item}")
        return dequeued_item

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

    def peek(self):
        """Return the front item of the queue without removing it."""
        if not self.is_empty():
            return self.items[0]
        return None

    def display(self):
        """Display the current items in the queue."""
        if self.is_empty():
            print("The queue is currently empty.")
        else:
            print("Current queue:", " -> ".join(self.items))


def ticketing_system():
    """Simulate a ticketing system where customers join a queue and are served in order."""
    queue = Queue()  # Create a new Queue instance

    while True:
        print("\nOptions:")
        print("1. Join the queue")
        print("2. Serve a customer")
        print("3. Display current queue")
        print("4. Check queue size")
        print("5. Exit")
        action = input("Choose an action (1-5): ").strip()

        if action == '1':
            customer_name = input("Enter the customer's name: ")
            queue.enqueue(customer_name)  # Add customer to the queue

        elif action == '2':
            queue.dequeue()  # Serve the next customer in the queue

        elif action == '3':
            queue.display()  # Show current queue

        elif action == '4':
            print(f"Queue size: {queue.size()}")  # Display the number of customers in the queue

        elif action == '5':
            print("Exiting the ticketing system.")
            break

        else:
            print("Invalid action. Please choose a valid option.")


if __name__ == "__main__":
    ticketing_system()
