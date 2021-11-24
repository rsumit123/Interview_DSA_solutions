class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        n = self.head
        if n is not None:
            while n != None:
                print(n.data)
                n = n.next

    def print_middle(self):
        p1 = self.head
        p2 = self.head

        while p2 and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next

        print(p1.data)

    def count_nodes(self):
        count = 0
        temp = self.head
        while (temp is not None):
            temp = temp.next
            count += 1
        return count

    def swap_kth_nodes(self, k):
        n = self.count_nodes()
        if k > n:
            print("unexpected k value")
        else:
            b_node = self.head
            b_node_prev = None
            i = 0
            while i < k-1:
                b_node_prev = b_node
                b_node = b_node.next
                i+=1

            print("Data kth node", b_node.data)
            print("Data k-1th node", b_node_prev.data)

            i = 0
            e_node = self.head
            e_node_prev = None
            while i < n-k:
              e_node_prev = e_node
              e_node = e_node.next
              i+=1
            print("Data kth node end", e_node.data)
            print("Data k-1th node end", e_node_prev.data)

            e_node_prev.next,b_node_prev.next = b_node_prev.next, e_node_prev.next
            e_node.next,b_node.next = b_node.next, e_node.next

            self.print_ll()

            


l1 = LinkedList()
l1.head = Node("first")
e = Node(data=str(1))
l1.head.next = e
for i in range(2, 11):
    n = Node(data=str(i))
    e.next = n

    e = n

l1.print_ll()
# print(l1.count_nodes())
print(l1.swap_kth_nodes(6))
# l1.print_middle()

# print("hi")
# print("Is it visible yes it is definitely")
