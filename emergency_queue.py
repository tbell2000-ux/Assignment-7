class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency



class MinHeap:
    def __init__(self):
        self.data = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left(self, index):
        return 2 * index + 1

    def _right(self, index):
        return 2 * index + 2

    def heapify_up(self, index):
        while index > 0:
            parent = self._parent(index)
            if self.data[index].urgency < self.data[parent].urgency:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def heapify_down(self, index):
        size = len(self.data)
        while True:
            left = self._left(index)
            right = self._right(index)
            smallest = index

            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        print("Current Queue:")
        for p in self.data:
            print(f"- {p.name} ({p.urgency})")

    def peek(self):
        if not self.data:
            return None
        return self.data[0]

    def remove_min(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()
        root = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return root


# Test your MinHeap class here including edge cases
if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()
    print()

    next_up = heap.peek()
    if next_up:
        print("Next up:", next_up.name, next_up.urgency)
    print()

    served = heap.remove_min()
    if served:
        print("Served:", served.name)
    heap.print_heap()

    print()
    # Edge cases
    print("Removing all remaining patients...")
    while heap.data:
        p = heap.remove_min()
        print("Removed:", p.name)
    print("Heap empty?", not heap.data)