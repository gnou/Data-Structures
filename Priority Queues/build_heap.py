# python3

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def parent(self, i):
        return (i-1)//2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def sift_up(self, i):
        while i > 0 and self._data[self.parent(i)] > self._data[i]:
            self._swaps.append((self.parent(i), i))
            self._data[i], self._data[self.parent(i)] = self._data[self.parent(i)], self._data[i]
            i = self.parent(i)

    def sift_down(self, i):
        min_index = i
        left_index = self.left_child(i)
        if left_index < len(self._data) and self._data[min_index] > self._data[left_index]:
            min_index = left_index
        right_index = self.right_child(i)
        if right_index < len(self._data) and self._data[min_index] > self._data[right_index]:
            min_index = right_index
        if i != min_index:
            self._swaps.append((i, min_index))
            self._data[i], self._data[min_index] = self._data[min_index], self._data[i]
            self.sift_down(min_index)


    def GenerateSwaps(self):
        length = len(self._data)
        start = length//2
        for i in reversed(range(0, len(self._data)//2)):
            self.sift_down(i)

        # The following naive implementation just sorts
        # the given sequence using selection sort algorithm
        # and saves the resulting sequence of swaps.
        # This turns the given array into a heap,
        # but in the worst case gives a quadratic number of swaps.
        #
        # TODO: replace by a more efficient implementation
        # for i in range(len(self._data)):
        #     for j in range(i + 1, len(self._data)):
        #         if self._data[i] > self._data[j]:
        #             self._swaps.append((i, j))
        #             self._data[i], self._data[j] = self._data[j], self._data[i]

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
