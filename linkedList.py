class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
# Creating head of the Linked list
head = Node(1)
print("The value at head is", head.value)