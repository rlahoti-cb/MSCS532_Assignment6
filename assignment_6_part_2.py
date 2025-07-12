
class Array:
    def __init__(self):
        self.data = []

    def insert(self, idx, val):
        self.data.insert(idx, val)

    def delete(self, idx):
        if self._idx_exists(idx):
            return self.data.pop(idx)
        return None

    def access(self, idx):
        if self._idx_exists(idx):
            return self.data[idx]
        return None

    def _idx_exists(self, idx):
        if 0 <= idx < len(self.data):
            return True
        return False

class Matrix:
    def __init__(self, num_rows, num_cols):
        self.data = [[None for _ in range(num_cols)] for _ in range(num_rows)]

    def insert(self, row, col, val):
        self.data[row][col] = val

    def access(self, row, col):
        return self.data[row][col]

    def delete(self, row, col):
        self.data[row][col] = None

class Stack: 
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self._is_empty():
            return self.stack.pop()
        return None

    def _is_empty(self):
        return len(self.stack) == 0

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, val):
        self.queue.append(val)
    
    def dequeue(self):
        if not self._is_empty():
            return self.queue.pop(0)
        return None
    
    def _is_empty(self):
        return len(self.queue) == 0

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, val):
        next_node = Node(val)
        if not self.head:
            self.head = next_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = next_node
    
    def delete(self, val):
        current = self.head
        previous = None
        while current:
            if current.value == val:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False
    
    def traverse(self):
        output = []
        current = self.head
        while current:
            output.append(current.value)
            current = current.next
        return output

def part_2_demonstration():
    array_demo()
    matrix_demo()
    stack_demo()
    queue_demo()
    linked_list_demo()

def array_demo():
    array = Array()
    array.insert(0, "pizza")
    array.insert(1, "cheese stick")
    array.insert(2, "fudge")
    print("Array state after insertions: ", array.data)
    print("Access index 2: ", array.access(2))
    print("Deleted element at index 2: ", array.delete(2))
    print("Array state after deletion: ", array.data)
    print()

def matrix_demo():
    matrix = Matrix(3,3)
    matrix.insert(0, 0, 1)
    matrix.insert(0, 1, 2)
    matrix.insert(1, 2, 3)
    matrix.insert(2, 2, 4)

    print("Matrix state initially: ")
    for row in matrix.data:
        print(row)
    
    print("Access element at row 1 and column 2: ", matrix.access(1, 2))

    matrix.delete(1, 2)
    print("Matrix state after deletion")
    print("Matrix: ")
    for row in matrix.data:
        print(row)
    
    print()

def stack_demo():
    stack = Stack()
    stack.push("first element")
    stack.push("second element")
    stack.push("third element")

    print("Stack state after pushing elements (bottom -> top): ", stack.stack)
    print("Popping top element from stack: ", stack.pop())
    print("Stack state after poping an element:", stack.stack)

    print()

def queue_demo():
    queue = Queue()
    queue.enqueue("first")
    queue.enqueue("second")
    queue.enqueue("third")

    print("Queue state after enqueueing elements (first -> last inserted): ", queue.queue)
    print("Dequeueing an element: ", queue.dequeue())
    print("Queue state after dequeue: ", queue.queue)

    print()

def linked_list_demo():
    linked_list = LinkedList()
    linked_list.insert("1")
    linked_list.insert("2")
    linked_list.insert("3")

    print("Linked list state after insertions: ", linked_list.traverse())
    linked_list.delete("2")
    print("Linked list state after deletion of second node 2: ", linked_list.traverse())

    print()


if __name__ == "__main__":
    part_2_demonstration()