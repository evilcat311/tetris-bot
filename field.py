#!/usr/bin/python

from tetromino import Tetromino

class TetrisException(Exception):
    pass

class Field():

    WIDTH = 10
    HEIGHT = 22

    def __init__(self, state=None):
        if state:
            self.state = state
        else:
            self.state = [[' ' for cols in range(Field.WIDTH)]
                          for rows in range(Field.HEIGHT)]

    def __str__(self):
        BAR = '   ' + '-' * (Field.WIDTH * 2 + 1) + '\n    ' + \
            ' '.join(map(str, range(Field.WIDTH))) + '\n'
        return BAR + '\n'.join([
            '{:2d} |'.format(i) + ' '.join(row) + '|'
                for i, row in enumerate(self.state)]) + '\n' + BAR

    def _test_tetromino(self, tetromino, row, column):
        """
        Tests to see if a tetromino can be placed at the specified row and
        column. It performs the test with the bottom left corner of the
        tetromino at the specified row and column.
        """
        assert column >= 0
        assert column + tetromino.width() <= Field.WIDTH
        assert row - tetromino.height() + 1 >= 0
        assert row < Field.HEIGHT
        for ti, si in list(enumerate(range(row - tetromino.height() + 1,
                                           row + 1)))[::-1]:
            for tj, sj in enumerate(range(column, column + tetromino.width())):
                if tetromino[ti][tj] != ' ' and self.state[si][sj] != ' ':
                    return False
        return True

    def _place_tetromino(self, tetromino, row, column):
        """
        Place a tetromino at the specified row and column.
        The bottom left corner of the tetromino will be placed at the specified
        row and column. This function does not perform checks and will overwrite
        filled spaces in the field.
        """
        assert column >= 0
        assert column + tetromino.width() <= Field.WIDTH
        assert row - tetromino.height() + 1 >= 0
        assert row < Field.HEIGHT
        for ti, si in list(enumerate(range(row - tetromino.height() + 1,
                                           row + 1)))[::-1]:
            for tj, sj in enumerate(range(column, column + tetromino.width())):
                if tetromino[ti][tj] != ' ':
                    self.state[si][sj] = tetromino[ti][tj]

    def drop(self, tetromino, column):
        """
        Drops a tetromino in the specified column.
        The leftmost column of the tetromino will be aligned with the specified
        column.
        """
        assert isinstance(tetromino, Tetromino)
        assert column >= 0
        assert column + tetromino.width() <= Field.WIDTH
        for row in range(Field.HEIGHT)[::-1]:
            if self._test_tetromino(tetromino, row, column):
                self._place_tetromino(tetromino, row, column)
                return
        raise TetrisException('Unable to place Tetromino: \n{}'.format(
            tetromino))

    def has_no_gaps(self):
        """
        Check each column one by one to make sure there are no gaps in the
        column.
        """
        for col in range(Field.WIDTH):
            if "".join([row[col] for row in self.state]).lstrip().count(' '):
                return False
        return True

    def height(self):
        """
        Returns the height of the highest placed tetromino in the field.
        """
        for i, row in enumerate(self.state):
            if ''.join(row).strip():
                return Field.HEIGHT - i


if __name__ == '__main__':
    f = Field()
    f.drop(Tetromino.LTetromino(), 0)
    print(f.has_no_gaps())
    print(f.height())
    f.drop(Tetromino.LTetromino(), 2)
    print(f.has_no_gaps())
    f.drop(Tetromino.STetromino(), 2)
    print(f.height())
    print(f.has_no_gaps())
    t = Tetromino.LTetromino().flip()
    f.drop(t, 0)
    f.drop(Tetromino.TTetromino().flip(), 0)
    print(f)