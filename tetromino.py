#!/usr/bin/python

class Tetromino():

    def __init__(self, state, letter):
        # assert that there are rows
        assert len(state) > 0
        # assert rows and columns form a rectangle
        assert len({len(row) for row in state}) == 1
        self.state = state
        self.letter = letter

    @staticmethod
    def ITetromino():
        return Tetromino(
            [
                ['I'],
                ['I'],
                ['I'],
                ['I']
            ],
            'I'
        )

    @staticmethod
    def OTetromino():
        return Tetromino(
            [
                ['O', 'O'],
                ['O', 'O']
            ],
            'O'
        )

    @staticmethod
    def TTetromino():
        return Tetromino(
            [
                ['T', 'T', 'T'],
                [' ', 'T', ' ']
            ],
            'T'
        )

    @staticmethod
    def STetromino():
        return Tetromino(
            [
                [' ', 'S', 'S'],
                ['S', 'S', ' ']
            ],
            'S'
        )

    @staticmethod
    def ZTetromino():
        return Tetromino(
            [
                ['Z', 'Z', ' '],
                [' ', 'Z', 'Z']
            ],
            'Z'
        )

    @staticmethod
    def JTetromino():
        return Tetromino(
            [
                [' ', 'J'],
                [' ', 'J'],
                ['J', 'J']
            ],
            'J'
        )

    @staticmethod
    def LTetromino():
        return Tetromino(
            [
                ['L', ' '],
                ['L', ' '],
                ['L', 'L']
            ],
            'T'
        )

    def __str__(self):
        return "\n".join(["".join(x) for x in self.state])

    def __getitem__(self, key):
        return self.state[key]

    def width(self):
        return len(self.state[0])

    def height(self):
        return len(self.state)

    def rotate_right(self):
        self.state = list(zip(*self.state[::-1]))
        return self

    def rotate_left(self):
        self.state = list(reversed(list(zip(*self.state))))
        return self

    def flip(self):
        self.state = [row[::-1] for row in self.state[::-1]]
        return self

if __name__ == '__main__':
    t = Tetromino.LTetromino()
    print(t)
    print()
    t.rotate_right()
    print(t)
    print()
    t.rotate_right()
    print(t)
    print()
    t.rotate_left()
    print(t)
    print(t.height())
    print(t.width())
    t.flip()
    print(t)