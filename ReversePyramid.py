class ReversePyramid:
    def __init__(self, rows):
        self.rows = rows

    def printPyramid(self):
        for i in range(1, self.rows + 1):
            for j in range(1, i):
                print(" ", end="")
            for j in range(self.rows - i, -1, -1):
                print("*", end="")
            for j in range(self.rows - i, 0, -1):
                print("*", end="")
            print()


class ChildReversePyramid(ReversePyramid):
    def __init__(self, r):
        super().__init__(r)


if __name__ == '__main__':
    row = int(input("Enter the number of rows: "))
    print()
    obj = ChildReversePyramid(row)
    obj.printPyramid()
