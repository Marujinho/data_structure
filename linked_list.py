class Node():
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return f"{self.value}"
    

class SinglyLinkedList():

    def __init__(self):
        self.head = None

    def __str__(self):
        # Return a string representation of the list
        current = self.head
        values = []
        while current:
            values.append(str(current.value))
            current = current.next_node
        return " -> ".join(values)


    def add_node(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        return

    def search_node(self, value):

        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next_node
        
        return False

    def remove_node():
        return
    


# first element is HEAD [NODE [ value = 123, next=]]
tt = SinglyLinkedList()
tt.add_node(1)
tt.add_node(2)
tt.add_node(3)

gg = tt.search_node(2)

print(gg)