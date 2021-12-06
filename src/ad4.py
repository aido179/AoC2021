from typing import List


# with open('src/data/ad4.txt') as file:
#     data = file.read().strip().split("\n")

with open('src/data/ad4.txt') as file:
    data = file.read().strip().split("\n")

class Board:
    def __init__(self, rows):
        rows_split = [list(map(lambda v: int(v), r.strip().replace("  ", " ").split(" "))) for r in rows]
        rows_int = rows_split
        self.rows = rows_int
        self.row_counts = [0]*len(self.rows)
        self.cols = list(zip(*rows_int[::-1]))
        self.col_counts = [0]*len(self.cols)
        # self.marks = [[0]*len(self.cols)]*len(self.rows) # use [row][col] indexing
        self.marks = [[0 for i in range(len(self.cols))] for i in range(len(self.rows))]
        self.last_num = 0

    def check_num(self, num):
        self.last_num = num
        row_pos = -1
        col_pos = -1
        for i, row in enumerate(self.rows):
            if num in row:
                row_pos = i
                self.row_counts[i]+=1
        for i, col in enumerate(self.cols):
            if num in col:
                col_pos = i
                self.col_counts[i]+=1
        if row_pos >= 0:
            self.marks[row_pos][col_pos] = 1

    def is_complete(self):
        if any([r >= len(self.rows[0]) for r in self.row_counts]):
            return True
        if any([c >= len(self.cols[0]) for c in self.col_counts]):
            return True
        return False

    def get_score(self):
        score = 0
        for i, row in enumerate(self.rows):
            for j, num in enumerate(row):
                if self.marks[i][j] == 0:
                    score += self.rows[i][j]
        return score * self.last_num

    def print_marks(self):
        for i, col in enumerate(self.marks):
            line = ""
            for j, num in enumerate(col):
                line += f" {num}"
            print(line)

    def print_board(self):
        for i, row in enumerate(self.rows):
            line = ""
            for j, num in enumerate(row):
                line += f" {num}"
            print(line)

# Create boards
nums = [int(n) for n in data[0].split(",")]

def populate_boards(data:List[str]) -> List[Board]:
    boards = []
    board_buffer = []
    for row in data[1:]:
        if row != "":
            board_buffer.append(row)
        if row == "" and len(board_buffer) != 0:
            boards.append(Board(board_buffer.copy()))
            board_buffer = []
    if len(board_buffer) != 0:
        boards.append(Board(board_buffer.copy()))
    return boards

boards = populate_boards(data)
# pull out numbers
def get_winning_board(nums, boards):
    for n in nums:
        for i, b in enumerate(boards):
            b.check_num(n)
            if b.is_complete():
                return b

winning_board = get_winning_board(nums, boards)
winning_board.print_marks()
winning_board.print_board()
print(f"Part 1 {winning_board.get_score()}")

# Part 2
boards = populate_boards(data)
def get_last_winning_board(nums, boards):
    boards_buffer = boards.copy()
    for n in nums:
        removals = []
        for i, b in enumerate(boards_buffer):
            b.check_num(n)
            if b.is_complete() and len(boards_buffer) == 1:
                return boards_buffer[0]
            if b.is_complete() and len(boards_buffer) > 1:
                removals.append(i)
        for index in sorted(removals, reverse = True):
            del boards_buffer[index]


losing_board = get_last_winning_board(nums, boards)
losing_board.print_marks()
losing_board.print_board()
print(losing_board.last_num)
print(f"Part 2 {losing_board.get_score()}")
