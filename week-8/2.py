from collections import defaultdict

# Given the constraints of the knight
# chess piece, we can determine all possible
# moves the knight can make given there is
# sufficient board in the direction of travel
POSSIBLE_MOVES = [
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


def getBoardSize():
    """
    Gets the desired board size from the user
    """
    print('\nWhat size board should be solve?\n')

    return int(input('> '))


def generateGrid(boardSize):
    """
    Generates a list of all possible coordinates for a given board size.
    """

    grid = []

    for row in range(boardSize):

        for col in range(boardSize):

            grid.append((row, col))

    return grid


def generateTree(grids):
    """
    Generates a tree like structure where each key will be a coordinate on the board
    and the value will be a list of legal moves a knight can make from that position
    """

    tree = {}

    for grid in grids:

        xStart = grid[0]
        yStart = grid[1]

        tree[grid] = []

        # for each grid item, we need determine what
        # are the valid moves for this square
        for move in POSSIBLE_MOVES:

            xEnd = xStart + move[0]
            yEnd = yStart + move[1]

            endGrid = (xEnd, yEnd)

            if endGrid in grids:
                tree[grid].append(endGrid)

    return tree


def add_edge(graph, vertexA, vertexB):
    """
    Used to add an edge between two leafs on a given graph
    """

    graph[vertexA].add(vertexB)
    graph[vertexB].add(vertexA)

    return graph


def generateGraph(tree):
    """
    Generate a graph from a given tree of coordinates and moves.
    Each node on the graph cooresponds to the coordinates of a
    specific square on the chess board, and the edges of the node
    coorespond to all square that a knight can reach from that square
    """

    graph = defaultdict(set)

    for square, moves in tree.items():

        for move in moves:

            add_edge(graph, square, move)

    return graph


def first_true(items):
    """
    Iterate through a sequence and return the first item that is true-y
    or return none
    """

    for item in items:
        if item:
            return item

    return None


def generateSolution(boardSize, grid, graph, startPt):
    """
    Perform a depth first search on the given graph
    and return a path that allows the knight to hit every
    square.
    """

    def traverse(path, currentSquare):
        """
        Used to traverse through the graph recursively
        """

        if len(path) + 1 == len(grid):
            # recursive sentinel for total length
            return path + [currentSquare]

        # length of path means we havent hit all the squares
        yet_to_visit = graph[currentSquare] - set(path)

        if not yet_to_visit:
            # no unvisited neighbors, so dead end
            return False

        # try all valid paths from here
        nextMoves = sorted(yet_to_visit)

        return first_true(traverse(path + [currentSquare], vertex)
                          for vertex in nextMoves)

    result = traverse([], startPt)

    if result:
        return result
    else:
        print(f"\nNo Possible path for board size of {boardSize}")
        quit()


# Given we have a board size
boardSize = getBoardSize()

# And giving a starting location
startColumn, startRow = 0, 0

# We can generate a grid of all
# coords on the board
grid = generateGrid(boardSize)

# We can use those grids to generate a tree
# where the each key will be the grid coord
# of each square, and the value will be a list
# of possible moves the knight can make from
# that square.
tree = generateTree(grid)

# Now we can generate a graph of
# possible moves
graph = generateGraph(tree)

# Using DFS, generate a path that completes
# the knights tour
path = generateSolution(boardSize, grid, graph, (startColumn, startRow))

if (boardSize != 5):

    print(
        f"\nOne possible path to complete the knights tour on a {boardSize} x {boardSize} board is the following path:")
    print('\n', path)
    quit()

fiveGridDisplay = """

    ╔════╤════╤════╤════╤════╗
    ║ 00 │ 01 │ 02 │ 03 │ 04 ║
    ╠════╪════╪════╪════╪════╣
    ║ 05 │ 06 │ 07 │ 08 │ 09 ║
    ╟────┼────┼────┼────┼────╢
    ║ 10 │ 11 │ 12 │ 13 │ 14 ║
    ╟────┼────┼────┼────┼────╢
    ║ 15 │ 16 │ 17 │ 18 │ 19 ║
    ╟────┼────┼────┼────┼────╢
    ║ 20 │ 21 │ 22 │ 23 │ 24 ║
    ╚════╧════╧════╧════╧════╝

    """


def animateBoard(move):

    global fiveGridDisplay

    if move[1] == 0:
        # first row
        num = "0" + str(move)[1]

        fiveGridDisplay = fiveGridDisplay.replace(num, "..")

    elif move[1] == 1:

        num = "0" + str(5+move[0])

        fiveGridDisplay = fiveGridDisplay.replace(num, "..")

    elif move[1] == 2:

        num = str(10+move[0])

        fiveGridDisplay = fiveGridDisplay.replace(num, "..")

    elif move[1] == 3:

        num = str(15+move[0])

        fiveGridDisplay = fiveGridDisplay.replace(num, "..")

    elif move[1] == 4:

        num = str(20+move[0])

        fiveGridDisplay = fiveGridDisplay.replace(num, "..")

    return fiveGridDisplay


print('\n')

moveNumber = 0

for move in path:

    print(f"Move Number: {moveNumber}")

    print(animateBoard(move))

    moveNumber = moveNumber + 1
