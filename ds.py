class Array_Seq:
    def __init__(self):
        self.A = []
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        yield from self.A

    def build(self, X):
        self.A = [a for a in X]
        self.size = len(self.A)

    def get_at(self, i):
        return self.A[i]

    def set_at(self, i, x):
        self.A[i] = x

    def __copy_forward(self, i, n, A, j):
        for k in range(n):
            A[j + k] = self.A[i + k]

    def __copy_backward(self, i, n, A, j):
        for k in range(n - 1, -1, -1):
            A[j + k] = self.A[i + k]

    def insert_at(self, i, x):
        n = len(self)
        A = [None] * (n + 1)
        self.__copy_forward(0, i, A, 0)
        A[i] = x
        self.__copy_forward(i, n - i, A, i + 1)
        self.build(A)

    def delete_at(self, i):
        n = len(self)
        A = [None] * (n - 1)
        self.__copy_forward(0, i, A, 0)
        x = self.A[i]
        self.__copy_forward(i + 1, n - i - 1, A, i)
        self.build(A)
        return x

    def insert_first(self, x):  # O(n)
        self.insert_at(0, x)

    def delete_first(self):  # O(n)
        self.delete_at(0)

    def insert_last(self, x):  # O(n)
        self.insert_at(len(self), x)

    def delete_last(self):  # O(n)
        self.delete_at(len(self) - 1)


class Dynamic_Array_Seq(Array_Seq):
    def __init__(self, r=2):
        super().__init__()
        self.size = 0
        self.r = r
        self._compute_bounds()
        self._resize(0)

    def __len__(self):
        return self.size

    def __iter__(self):
        for i in range(len(self)):
            yield self.A[i]

    def build(self, X):
        for a in X: self.insert_last(a)

    def _compute_bounds(self):
        self.upper = len(self.A)
        self.lower = len(self.A) // (self.r * self.r)

    def _resize(self, n):
        if (self.lower < n < self.upper): return
        m = max(n, 1) * self.r
        A = [None] * m
        self.__copy_forward(0, self.size, A, 0)
        self.A = A
        self._compute_bounds()

    def insert_last(self, x):  # O(1)
        self._resize(self.size + 1)
        self.A[self.size] = x
        self.size += 1

    def delete_last(self):  # O(1)
        self.A[self.size - 1] = None
        self.size -= 1
        self._resize(self.size - 1)

    def insert_at(self, i, x):
        self.insert_last(None)
        self.__copy_backward(i, self.size - (i + 1), self.A, i + 1)
        self.A[i] = x

    def delete_at(self, i):
        x = self.A[i]
        self.__copy_forward(i + 1, self.size - (i + 1), self.A, i)
        self.delete_last()
        return x

    def insert_first(self, x):
        self.insert_at(0, x)

    def delete_first(self):
        return self.delete_at(0)


class Linked_List_Node:

    def __init__(self, x):
        self.item = x
        self.next = None
        self.prev = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

    def prev_node(self, i):
        if i == 0: return self
        assert self.prev
        return self.prev.prev_node(i - 1)


class Linked_List_Seq:

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def build(self, X):
        for a in reversed(X):
            self.insert_first(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):  # O(1)
        new_node = Linked_List_Node(x)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete_first(self):  # O(1)
        x = self.head.item
        self.head = self.head.next
        self.size -= 1
        return x

    def insert_at(self, i, x):
        if i == 0:
            self.insert_first(x)
            return
        new_node = Linked_List_Node(x)
        node = self.head.later_node(i - 1)
        new_node.next = node.next
        node.next = new_node
        self.size += 1

    def delete_at(self, i):
        if i == 0:
            return self.delete_first()
        node = self.head.later_node(i - 1)
        x = node.next.item
        node.next = node.next.next
        self.size -= 1
        return x

    def insert_last(self, x):
        self.insert_at(len(self), x)

    def delete_last(self):
        return self.delete_at(len(self) - 1)


class Doubly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __reviter__(self):
        node = self.tail
        while node:
            yield node.item
            node = node.prev

    def build(self, X):
        for a in reversed(X):
            self.insert_first(a)

    def insert_first(self, x):
        new_node = Linked_List_Node(x)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        if self.size == 1:
            new_node.next = self.tail
            self.head = new_node
            self.tail.prev = new_node
            self.size += 1
            return
        new_node.next = self.head
        self.head = new_node
        new_node.next.prev = new_node
        self.size += 1

    def insert_last(self, x):
        new_node = Linked_List_Node(x)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        if self.size == 1:
            self.head.next = new_node
            self.tail = new_node
            self.size += 1
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def delete_first(self):
        if self.size == 0:
            return
        x = self.head.item
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return x
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1
        return x

    def delele_last(self):
        if self.size == 0:
            return
        x = self.tail.item
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return x
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1
        return x

    def swap_ends(self):
        if self.size == 0 or self.size == 1:
            return
        x = self.delele_last()
        y = self.delete_first()
        self.insert_last(y)
        self.insert_first(x)

    def shift_left(self, k):
        if self.size == 0:
            return
        for i in range(k):
            x = self.delete_first()
            self.insert_last(x)
