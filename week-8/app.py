from collections import defaultdict

BOARD_SIZE = 8

graph = {}

board = [[i] for i in range(1, BOARD_SIZE * BOARD_SIZE + 1)]

moves = [
    # Top right
    (1, 2),
    (2, 1),

    # Bottom right
    (2, -1),
    (1, -2),

    # Bottom left
    (-1, -2),
    (-2, -1),

    # Top left
    (-2, 1),
    (-1, 2)
]

quit()


def legas_moves_from_coord(row, col):

    moves = (
        # Top right
        (1, 2),
        (2, 1),

        # Bottom right
        (2, -1),
        (1, -2),

        # Bottom left
        (-1, -2),
        (-2, -1),

        # Top left
        (-2, 1),
        (-1, 2)
    )

    if row != 1:
        coord = (row * 8) - 8 + col
    else:
        coord = col

    if coord in range(1, 65):
        return True
    else:
        return False


print(legas_moves_from_coord(9, 8))


def legal_moves_from(row, col, board_size):
    for row_offset, col_offset in MOVE_OFFSETS:
        move_row, move_col = row + row_offset, col + col_offset
        if 0 <= move_row < board_size and 0 <= move_col < board_size:
            yield move_row, move_col


def add_edge(graph, a, b):

    graph[a].add(b)
    graph[b].add(a)


def build_graph(board_size):

    graph = defaultdict(set)

    for row in range(board_size):

        for col in range(board_size):

            for to_row, to_col in legal_moves_from(row, col, board_size):
                add_edge(graph, (row, col), (to_row, to_col))

    return graph
