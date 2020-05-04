# SWDV 610 - Data Structures
# Week 7 Review
# Wyatt Castaneda

"""
Three missionaries and three cannibals come to a river and find a boat that holds two people. 
Everyone must get across the river to continue on the journey. However, if the cannibals ever 
outnumber the missionaries on either bank, the missionaries will be eaten.

Find a series of crossings that will get everyone safely to the other side of the river.
Record your program running and submit your code and recording.

In addition to coding this task, you must post a video running and explaining your code.  
This allows for you to demonstrate what is occurring in the code as it is happening and how it 
is organized.  You must also run your code in the video to explain the output and why the 
program produced that output.

@link https://www.cs.dartmouth.edu/~devin/cs76/01_cannibals/cannibals.html
"""

bank1 = {'cannibals': 3, 'missionaries': 3}
bank2 = {'cannibals': 0, 'missionaries': 0}
boat = {'cannibals': 0, 'missionaries': 0}


def show_current_scene(bank1=bank1, bank2=bank2, boat=boat, step=1):

    scene = """
    Step {}
    --------------------------------------
                   Bank 1   Boat   Bank 2  
    --------------------------------------
    cannibals    | {}         {}     {} 
    missionaries | {}         {}     {}
    """

    scene = scene.format(step, bank1['cannibals'], boat['cannibals'], bank2['cannibals'],
                         bank1['missionaries'], boat['missionaries'], bank2['missionaries'])

    print(scene)


def cross_bank(b1=bank1, b2=bank2, bo=boat, step=1):

    if all(x == 0 for x in b2.values()):

        # bank2 is empty, initial condition
        show_current_scene(b1, b2, bo, step)
        b1['cannibals'] -= 1  # 1 cannibal leaves bank1
        bo['cannibals'] += 1  # gets on boat

    step += 1
    b1['missionaries'] -= 1  # 1 missionary leaves bank1
    bo['missionaries'] += 1  # gets on boat
    show_current_scene(b1, b2, bo, step)

    if all(x == 0 for x in b1.values()):  # bank1 is empty
        # 1 cannibal and 1 missionary on the boat
        step += 1
        b2['cannibals'] += 1  # 1 cannibal steps out on bank2
        b2['missionaries'] += 1  # 1 missionary steps out on bank2
        bo['cannibals'], bo['missionaries'] = 0, 0  # All leave the boat
        show_current_scene(b1, b2, bo, step)
        return  # final condition is met

    step += 1
    bo['missionaries'] -= 1  # 1 missionary leaves the boat
    b2['missionaries'] += 1  # 1 missionary added to bank 2
    show_current_scene(b1, b2, bo, step)

    step += 1
    bo['cannibals'] += 1  # 1 cannibal gets on board
    b1['cannibals'] -= 1  # 1 cannibal leaves the bank1
    show_current_scene(b1, b2, bo, step)

    step += 1
    bo['cannibals'] -= 1  # 1 cannibal get off the boat
    b2['cannibals'] += 1  # 1 cannibal added to bank 2
    show_current_scene(b1, b2, bo, step)

    cross_bank(b1, b2, bo, step)  # another series of crossings


cross_bank()
