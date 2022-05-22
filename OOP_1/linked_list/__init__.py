class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
        def __init__(self):
            self.head = None

        def insert_at_begining(self, data):
            node = Node(data,self.head)
            self.head = node

        def insert_at_end(self,data):
            if self.head == None:
                self.head = Node(data,None)
                return
            itr = self.head
            while itr.next:
                itr = itr.next

            itr.next = Node(data,None)

        def insert_values(self,data_list):
            for data in data_list:
                self.insert_at_end(data)

        def get_length(self):
            count = 0
            itr = self.head
            while itr:
                count += 1
                itr = itr.next
            return count

        def remove(self,index):
            if index<0 or index>=self.get_length():
                raise Exception("Invalid index")
            if index == 0:
                self.head = self.head.next
            count= 0
            itr = self.head
            while itr:
                if count == index-1:
                    itr.next = itr.next.next
                itr = itr.next
                count += 1


        def print(self):
            if self.head is None:
                print("Empty Linked List")

            itr = self.head
            llstr = " "
            while itr:
                llstr += str(itr.data)+"--->"
                itr = itr.next
            print(llstr)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_begining(10)
    ll.insert_at_begining(20)
    ll.insert_at_begining(30)
    ll.insert_at_begining(40)
    ll.insert_at_end(50)
    ll.insert_values(["Taslim","Tian"])
    ll.print()
    ll.remove(2)
    ll.print()

