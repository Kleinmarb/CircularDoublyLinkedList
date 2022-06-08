
class CircularDoublyLinkedList:

    class __Node:

        def __init__(self, element):

            self.value = element

            self.next = None
            self.last = None

        def __str__(self):

            return str(self.value)

    def __init__(self, represent=True):

        self.__head = None
        self.__root = None

        self.__len = 0

        self.__repr = represent

    def __iter__(self):

        complete = []

        current = self.__head

        length = 0
        while length < self.__len:

            length += 1

            complete.append(current.value)

            current = current.next

        return iter(complete)

    def __contains__(self, item):

        for value in self:

            if value == item:
                return True

        return False

    def __len__(self):

        return self.__len

    def add(self, *element):

        for value in element:

            if isinstance(value, str) or isinstance(value, bool) or isinstance(value, int) or isinstance(value, float):
                if self.__len > 1:
                    new_node = CircularDoublyLinkedList.__Node(value)

                    new_node.last = self.__root
                    self.__root.next = new_node

                    self.__root = new_node
                    self.__root.next = self.__head

                    self.__len += 1

                elif self.__len == 0:
                    new_node = CircularDoublyLinkedList.__Node(value)

                    self.__head = new_node
                    self.__root = new_node

                    self.__head.last = self.__root
                    self.__head.next = self.__root

                    self.__len += 1

                else:
                    new_node = CircularDoublyLinkedList.__Node(value)

                    self.__head.next = new_node

                    self.__root.next = new_node
                    new_node.last = self.__head

                    self.__root = new_node
                    self.__root.next = self.__head

                    self.__len += 1

            else:
                raise TypeError(f"Unexpected type: {type(value)}. Expected type: str, int, bool, float")

    def extend(self, element: iter):

        try:
            for value in element:

                self.add(value)

        except TypeError:
            raise ValueError(f"Unexpected type: {type(element)}. Expected iter")

    def __iadd__(self, other):

        self.add(other)

        return self

    def insert(self, element, index: int):

        if not isinstance(index, int):
            raise TypeError("Index not", type(int))

        if index < 0 or index > (self.__len + 1):
            raise IndexError("Index out of range")

        elif index == 0 and self.__len == 0:
            self.add(element)

        elif index == 0 and self.__len == 1:
            new_node = CircularDoublyLinkedList.__Node(element)

            self.__head.next = new_node
            self.__head.last = new_node

            new_node.next = self.__head
            new_node.last = self.__head

            self.__head = new_node

            self.__len += 1

        elif index == 0:
            new_node = CircularDoublyLinkedList.__Node(element)

            self.__head.last = new_node
            new_node.next = self.__head

            self.__head = new_node

            self.__head.last = self.__root
            self.__root.next = self.__head

            self.__len += 1

        elif index == 1 and self.__len == 1:
            self.add(element)

        elif index == self.__len:
            new_node = CircularDoublyLinkedList.__Node(element)

            self.__root.next = new_node
            self.__head.last = new_node

            new_node.next = self.__head
            new_node.last = self.__root

            self.__root = new_node

            self.__len += 1

        else:

            current = self.__head

            length = 0
            while True:

                if length == index:
                    new_node = CircularDoublyLinkedList.__Node(element)

                    new_node.next = current
                    new_node.last = current.last

                    current.last.next = new_node
                    current.last = new_node

                    self.__len += 1

                    break

                current = current.next

                length += 1

    def drop(self, element):

        if element != self.__head.value:
            length = 0

            done = False

            current = self.__head
            while self.__len > length:

                if element == self.__root.value and current == self.__root:
                    self.__root.last.next = self.__head
                    self.__root = self.__root.last

                    self.__head.last = self.__root

                    self.__len -= 1

                    done = True

                    break

                elif current.value == element:

                    current.last.next = current.next
                    current.next.last = current.last

                    self.__len -= 1

                    done = True

                    break

                current = current.next
                length += 1

            assert done, f"Value not in DoublyLinkedList."

        else:

            self.__root.next = self.__head.next
            self.__head.next.last = self.__root

            self.__head = self.__head.next

            self.__len -= 1

    def pop(self, index=None):

        if index is None:
            self.__root.last.next = self.__head
            self.__root.next.last = self.__root.last

            self.__root = self.__root.last

            self.__len -= 1

            return

        if not isinstance(index, int):
            raise ValueError(f"Unexpected type: {type(index)}. Expected type int")

        if index >= self.__len:
            raise IndexError("Index out of range")

        if index == 0:
            self.__head.next.last = self.__root
            self.__root.next = self.__head.next

            self.__head = self.__head.next

            self.__len -= 1

        elif index == (self.__len - 1):
            self.pop()

        else:
            length = 0

            current = self.__head

            while True:

                if length == index:
                    current.last.next = current.next
                    current.next.last = current.last

                    self.__len -= 1

                    break

                length += 1

                current = current.next

    def __isub__(self, other):

        self.drop(other)

        return self

    def __getitem__(self, item):

        if not isinstance(item, int):
            raise ValueError(f"Unexpected type: {type(item)}. Expected type int")

        elif item > (self.__len - 1):
            raise IndexError("Index out of range")

        length = 0

        current = self.__head

        while True:

            if length == item:
                return current.value

            length += 1

            current = current.next

    def __setitem__(self, key, value):

        if not isinstance(key, int):
            raise ValueError(f"Unexpected type: {type(key)}. Expected type int")

        elif key > (self.__len - 1):
            raise IndexError("Index out of range")

        length = 0

        current = self.__head

        while True:

            if length == key:
                current.value = value

                break

            length += 1

            current = current.next

    def index(self, element):

        length = 0

        for value in self:

            if element == value:
                return length

            length += 1

    def count(self):

        from collections import Counter

        return Counter(self)

    def clear(self):

        while self.__len != 0:

            self.pop()

    def reverse(self):

        new_list = self.copy()
        self.clear()

        while new_list.__len != 0:

            self.add(new_list.__root.value)
            new_list.pop()

    def sort(self):

        array = [value for value in self]
        array.sort()

        new_list = CircularDoublyLinkedList()

        for value in array:

            new_list.add(value)

        self.clear()

        for value in new_list:

            self.add(value)

    def copy(self):

        new_list = CircularDoublyLinkedList()

        for value in self:

            new_list.add(value)

        return new_list

    def __repr__(self):

        if self.__repr:

            if self.__len > 0:
                current = self.__head

                while True:

                    test = input(f"{str(current)} ")

                    if test == "<" and current == self.__head:
                        current = self.__root

                    elif test == "<":
                        current = current.last

                    elif test == ">":
                        current = current.next

                    elif test == "x":
                        return ""

                    else:
                        raise KeyboardInterrupt("Input unknown")

            else:
                return "Empty"

        else:
            current = self.__head

            string = ""
            while True:

                if current != self.__root:
                    string += f"{current.value}, "

                else:
                    string += str(current.value)

                    break

                current = current.next

            return string
