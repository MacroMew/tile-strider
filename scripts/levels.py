"""
LEVEL CREATION GUIDE / MANUEL

To create a level, create a new level variable with the 'levelclass.Level()' function.
First, choose a size. All levels *are* square, void tiles are used to create different shapes.
Tile entries go next in a square grid (in one list), then objects (in one list),
then the background color (RGB format), then the offset (variable is named 'offset').
For each tile entry, the first number in the list is which tile it is and the second number is its state.
For instance, [1, 0] is a floor tile (1) in it's default (and only) state (0).
The first object entry will be the player.
For each object entry, the first number is the column it is in (from the left),
the second number is the row it is in (from the top), and the third number is which object it is.
That is, the object entry will be in the form of [X, Y, Object].
Then add it's physical number minus 1 to your desired difficulty option (A is super easy, B is easy, C is medium,
D is hard, and N is u*n*defined)

TILE INDEX LIST

~~GENERAL TILES
    0 = Pit, 1 = Floor, 2 = Wall, 10 = Red Block, 11 = Blue Block, 9 = Void
~~SPAWN AND GOAL TILES
    7 = Goal, 8 = Spawn
~~ACTIVATORS
    3 = Lever, 12 = Red Lever, 13 = Blue Lever, 4 = Button, 14 = Red Button, 15 = Blue Button
~~ARROWS
    5 = Arrow, 16 = Double Arrow, 17 = Max Arrow
        (state: 0 = up, 1 = right, 2 = down, 3 = left)
~~ROTATORS
    6 = Clockwise Rotator, 18 = Counterclockwise Rotator, 19 = Flip Rotator
        (state: 0 = rotate adjacent, 1 = rotate globally)
The only tiles that have a state other than 0 (a.k.a. default) are Arrow tiles and Rotator tiles.

OBJECT INDEX LIST
    0 = Player, 1 = Crate, 2 = Red Crate, 3 = Blue Crate

//WARNING//

When making a level, be sure to surround the bottom and left sides of your level with something that cannot be
transversed, such as a wall, pit, or void tile. If you do not do this, then the player can clip Out of Bounds
(also called O.o.B. for short) which can let them complete the level in unintentional ways in the best case or crash
the entire game in the worst case.
//WHEN SHARING LEVELS WITH OTHERS, BE SURE TO FOLLOW THE ABOVE WARNING!!!//
"""
import levelclass
import gamedata

offset = gamedata.screen_offset

level1 = levelclass.Level(11, [[9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0],
                               [9, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [9, 0], [9, 0], [9, 0],
                               [9, 0], [2, 0], [1, 0], [1, 0], [1, 0], [2, 0], [3, 0], [2, 0], [9, 0], [9, 0], [9, 0],
                               [2, 0], [2, 0], [1, 0], [0, 0], [1, 0], [2, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 0],
                               [2, 0], [1, 0], [1, 0], [0, 0], [1, 0], [1, 0], [1, 0], [10, 0], [1, 0], [1, 0], [2, 0],
                               [2, 0], [8, 0], [1, 0], [0, 0], [1, 0], [1, 0], [1, 0], [10, 0], [1, 0], [7, 0], [2, 0],
                               [2, 0], [1, 0], [1, 0], [0, 0], [1, 0], [1, 0], [1, 0], [10, 0], [1, 0], [1, 0], [2, 0],
                               [2, 0], [2, 0], [1, 0], [0, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0],
                               [9, 0], [2, 0], [1, 0], [1, 0], [1, 0], [2, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0],
                               [9, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0],
                               [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0]],
                          [[2, 6, 0]], (25, 0, 0), "Level 1: Passing Borders (arrow keys to move, R to restart)", offset)

level2 = levelclass.Level(9, [[2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0],
                              [2, 0], [0, 0], [0, 0], [0, 0], [1, 0], [1, 0], [1, 0], [14, 0], [2, 0],
                              [2, 0], [0, 0], [0, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0],
                              [2, 0], [1, 0], [1, 0], [1, 0], [1, 0], [0, 0], [0, 0], [0, 0], [2, 0],
                              [2, 0], [8, 0], [1, 0], [1, 0], [1, 0], [10, 0], [11, 0], [7, 0], [2, 0],
                              [2, 0], [1, 0], [1, 0], [1, 0], [1, 0], [0, 0], [0, 0], [0, 0], [2, 0],
                              [2, 0], [0, 0], [0, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0],
                              [2, 0], [0, 0], [0, 0], [0, 0], [1, 0], [1, 0], [1, 0], [15, 0], [2, 0],
                              [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0]],
                          [[2, 5, 0], [6, 2, 1], [6, 8, 1]],
                          (50, 0, 50), "Level 2: 2 Blocks, 2 Buttons, 2 Crates", offset)

level3 = levelclass.Level(8, [[9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0],
                              [9, 0], [9, 0], [17, 1], [9, 0], [9, 0], [17, 2], [9, 0], [9, 0],
                              [9, 0], [9, 0], [9, 0], [9, 0], [7, 0], [9, 0], [9, 0], [9, 0],
                              [9, 0], [9, 0], [16, 0], [9, 0], [5, 3], [6, 0], [2, 0], [9, 0],
                              [9, 0], [9, 0], [1, 0], [1, 0], [1, 0], [0, 0], [2, 0], [9, 0],
                              [9, 0], [9, 0], [5, 1], [1, 0], [1, 0], [1, 0], [2, 0], [9, 0],
                              [9, 0], [9, 0], [8, 0], [5, 0], [1, 0], [2, 0], [2, 0], [9, 0],
                              [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0]],
                          [[3, 7, 0]], (0, 50, 0), "Level 3: Roundabout Way", offset)

level4 = levelclass.Level(11, [[9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0],
                               [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [2, 0], [9, 0], [9, 0], [9, 0], [9, 0],
                               [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0],
                               [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [13, 0], [9, 0], [9, 0], [9, 0], [9, 0],
                               [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0],
                               [9, 0], [9, 0], [8, 0], [1, 0], [2, 0], [2, 0], [17, 1], [2, 0], [9, 0], [9, 0], [9, 0],
                               [9, 0], [9, 0], [5, 3], [18, 0], [2, 0], [1, 0], [1, 0], [1, 0], [7, 0], [9, 0], [9, 0],
                               [9, 0], [2, 0], [1, 0], [2, 0], [1, 0], [1, 0], [1, 0], [2, 0], [2, 0], [2, 0], [9, 0],
                               [9, 0], [2, 0], [1, 0], [1, 0], [1, 0], [12, 0], [2, 0], [0, 0], [0, 0], [2, 0], [9, 0],
                               [9, 0], [2, 0], [1, 0], [1, 0], [1, 0], [18, 1], [2, 0], [0, 0], [0, 0], [2, 0], [9, 0],
                               [9, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [9, 0]],
                          [[3, 6, 0], [7, 7, 2], [8, 7, 3]],
                          (25, 50, 0), "Level 4: Global Ground (use U to undo your last move)", offset)

level5 = levelclass.Level(9, [[9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0],
                              [2, 0], [15, 0], [9, 0], [9, 0], [17, 1], [9, 0], [9, 0], [14, 0], [2, 0],
                              [9, 0], [9, 0], [9, 0], [9, 0], [1, 0], [9, 0], [9, 0], [9, 0], [9, 0],
                              [9, 0], [9, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [9, 0], [9, 0],
                              [9, 0], [9, 0], [1, 0], [1, 0], [8, 0], [1, 0], [1, 0], [9, 0], [9, 0],
                              [9, 0], [9, 0], [19, 1], [2, 0], [10, 0], [2, 0], [19, 1], [9, 0], [9, 0],
                              [9, 0], [9, 0], [9, 0], [2, 0], [11, 0], [2, 0], [9, 0], [9, 0], [9, 0],
                              [9, 0], [9, 0], [9, 0], [2, 0], [7, 0], [2, 0], [9, 0], [9, 0], [9, 0],
                              [9, 0], [9, 0], [9, 0], [2, 0], [2, 0], [2, 0], [9, 0], [9, 0], [9, 0]],
                          [[5, 5, 0], [4, 4, 1], [6, 4, 1]], (50, 25, 0), "Level 5: Crate Delivery", offset)

level6 = levelclass.Level(10, [[9, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [9, 0],
                               [9, 0], [2, 0], [8, 0], [5, 3], [5, 3], [5, 2], [5, 3], [5, 3], [2, 0], [9, 0],
                               [9, 0], [2, 0], [5, 2], [5, 0], [1, 0], [5, 1], [1, 0], [5, 0], [2, 0], [9, 0],
                               [9, 0], [2, 0], [1, 0], [5, 0], [1, 0], [17, 2], [1, 0], [1, 0], [2, 0], [9, 0],
                               [9, 0], [2, 0], [5, 2], [5, 0], [1, 0], [1, 0], [16, 0], [16, 2], [2, 0], [9, 0],
                               [9, 0], [2, 0], [1, 0], [1, 0], [17, 0], [1, 0], [5, 0], [1, 0], [2, 0], [9, 0],
                               [9, 0], [2, 0], [16, 1], [1, 0], [5, 0], [1, 0], [5, 0], [1, 0], [2, 0], [9, 0],
                               [9, 0], [2, 0], [5, 0], [1, 0], [5, 2], [1, 0], [5, 0], [1, 0], [2, 0], [9, 0],
                               [9, 0], [2, 0], [5, 0], [5, 3], [1, 0], [1, 0], [5, 0], [7, 0], [2, 0], [9, 0],
                               [9, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [9, 0]],
                          [[3, 2, 0]], (30, 30, 30), "Level 6: The Maze with no Walls", offset)

level7 = levelclass.Level(8, [[9, 0], [2, 0], [9, 0], [9, 0], [9, 0], [2, 0], [2, 0], [2, 0],
                              [2, 0], [5, 2], [4, 0], [9, 0], [8, 0], [1, 0], [17, 2], [2, 0],
                              [9, 0], [2, 0], [9, 0], [9, 0], [9, 0], [2, 0], [3, 0], [2, 0],
                              [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [1, 0], [0, 0], [2, 0],
                              [9, 0], [7, 0], [9, 0], [9, 0], [9, 0], [6, 1], [1, 0], [2, 0],
                              [2, 0], [10, 0], [6, 1], [19, 1], [1, 0], [1, 0], [2, 0], [2, 0],
                              [2, 0], [1, 0], [6, 1], [6, 1], [1, 0], [1, 0], [6, 1], [2, 0],
                              [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0]],
                          [[5, 2, 0], [2, 2, 1]], (0, 0, 50), "Level 7: Count to 3", offset)


level8 = levelclass.Level(10, [[2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0],
                               [2, 0], [0, 0], [0, 0], [5, 2], [5, 3], [14, 0], [5, 3], [2, 0], [0, 0], [2, 0],
                               [2, 0], [0, 0], [0, 0], [0, 0], [16, 3], [0, 0], [5, 2], [0, 0], [0, 0], [2, 0],
                               [2, 0], [0, 0], [0, 0], [0, 0], [2, 0], [0, 0], [0, 0], [0, 0], [0, 0], [2, 0],
                               [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0],
                               [2, 0], [1, 0], [10, 0], [1, 0], [1, 0], [1, 0], [6, 1], [2, 0], [11, 0], [2, 0],
                               [2, 0], [7, 0], [10, 0], [1, 0], [8, 0], [1, 0], [18, 1], [2, 0], [11, 0], [2, 0],
                               [2, 0], [1, 0], [10, 0], [1, 0], [1, 0], [1, 0], [19, 1], [2, 0], [11, 0], [2, 0],
                               [2, 0], [1, 0], [10, 0], [1, 0], [1, 0], [1, 0], [13, 0], [2, 0], [11, 0], [2, 0],
                               [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0]],
                          [[5, 7, 0], [4, 2, 3]], (50, 10, 10), "Level 8: Control Panel", offset)

level9 = levelclass.Level(11, [[9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0],
                               [9, 0], [1, 0], [2, 0], [1, 0], [16, 1], [9, 0], [10, 0], [1, 0], [1, 0], [1, 0], [9, 0],
                               [9, 0], [1, 0], [1, 0], [1, 0], [11, 0], [9, 0], [16, 3], [1, 0], [17, 2], [1, 0], [9, 0],
                               [9, 0], [3, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [4, 0], [9, 0],
                               [9, 0], [9, 0], [9, 0], [16, 0], [1, 0], [1, 0], [1, 0], [3, 0], [9, 0], [9, 0], [9, 0],
                               [9, 0], [9, 0], [9, 0], [1, 0], [1, 0], [2, 0], [2, 0], [2, 0], [9, 0], [9, 0], [9, 0],
                               [9, 0], [9, 0], [9, 0], [8, 0], [1, 0], [10, 0], [11, 0], [7, 0], [9, 0], [9, 0], [9, 0],
                               [9, 0], [3, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [2, 0], [9, 0],
                               [9, 0], [1, 0], [17, 0], [16, 0], [1, 0], [9, 0], [16, 3], [12, 0], [16, 3], [1, 0], [9, 0],
                               [9, 0], [1, 0], [1, 0], [4, 0], [1, 0], [9, 0], [2, 0], [1, 0], [2, 0], [1, 0], [9, 0],
                               [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0]],
                          [[4, 7, 0], [10, 3, 1], [7, 5, 3]], (0, 25, 50), "Level 9: Color Wheel", offset)

level10 = levelclass.Level(11, [[9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0],
                                [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0],
                                [2, 0], [1, 0], [1, 0], [14, 0], [0, 0], [7, 0], [0, 0], [1, 0], [1, 0], [1, 0], [2, 0],
                                [2, 0], [1, 0], [1, 0], [1, 0], [0, 0], [10, 0], [0, 0], [1, 0], [1, 0], [1, 0], [2, 0],
                                [2, 0], [1, 0], [2, 0], [1, 0], [0, 0], [1, 0], [0, 0], [17, 1], [2, 0], [13, 0], [2, 0],
                                [2, 0], [10, 0], [15, 0], [5, 3], [0, 0], [1, 0], [0, 0], [1, 0], [1, 0], [1, 0], [2, 0],
                                [2, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [11, 0], [1, 0], [1, 0], [2, 0],
                                [2, 0], [1, 0], [19, 0], [5, 2], [2, 0], [1, 0], [2, 0], [1, 0], [1, 0], [18, 1], [2, 0],
                                [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [8, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0],
                                [9, 0], [9, 0], [9, 0], [9, 0], [2, 0], [2, 0], [2, 0], [9, 0], [9, 0], [9, 0], [9, 0],
                                [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0]],
                           [[6, 9, 0], [4, 8, 1], [6, 5, 3], [8, 4, 3]], (0, 0, 0),
                           "Level 10: Breakout Room (last level, good luck!)", offset)

level11 = levelclass.Level(9, [[8, 0], [1, 0], [9, 0], [9, 0], [9, 0], [1, 0], [1, 0], [15, 0], [9, 0],
                               [16, 2], [14, 0], [9, 0], [9, 0], [9, 0], [1, 0], [1, 0], [9, 0], [9, 0],
                               [9, 0], [9, 0], [9, 0], [7, 0], [11, 0], [10, 0], [1, 0], [9, 0], [9, 0],
                               [1, 0], [16, 0], [5, 3], [9, 0], [9, 0], [16, 2], [9, 0], [9, 0], [9, 0],
                               [1, 0], [9, 0], [1, 0], [9, 0], [9, 0], [9, 0], [16, 0], [9, 0], [9, 0],
                               [1, 0], [9, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [9, 0], [9, 0],
                               [1, 0], [9, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [9, 0], [9, 0],
                               [1, 0], [1, 0], [1, 0], [9, 0], [1, 0], [1, 0], [1, 0], [9, 0], [9, 0],
                               [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0]],
                           [[1, 1, 0], [6, 7, 1], [5, 6, 2]],
                           (0, 0, 128), "Level 11: Did you really think it was over?", offset)

level12 = levelclass.Level(20, [[9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [2, 0], [9, 0], [2, 0], [2, 0], [2, 0], [9, 0], [2, 0], [9, 0], [9, 0], [9, 0],
                                [9, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [0, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [9, 0],
                                [9, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 0], [10, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [11, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [1, 0], [9, 0],
                                [9, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 0], [10, 0], [10, 0], [2, 0], [2, 0], [2, 0], [2, 0], [11, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [1, 0], [9, 0],
                                [9, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [10, 0], [10, 0], [2, 0], [2, 0], [2, 0], [11, 0], [11, 0], [0, 0], [2, 0], [2, 0], [2, 0], [1, 0], [9, 0],
                                [9, 0], [1, 0], [2, 0], [2, 0], [2, 0], [0, 0], [2, 0], [2, 0], [10, 0], [2, 0], [10, 0], [10, 0], [16, 1], [10, 0], [5, 1], [10, 0], [2, 0], [2, 0], [1, 0], [9, 0],
                                [9, 0], [1, 0], [2, 0], [2, 0], [12, 0], [5, 0], [1, 0], [2, 0], [10, 0], [2, 0], [10, 0], [2, 0], [11, 0], [11, 0], [0, 0], [10, 0], [2, 0], [2, 0], [1, 0], [9, 0],
                                [9, 0], [1, 0], [1, 0], [1, 0], [17, 3], [2, 0], [1, 0], [2, 0], [10, 0], [10, 0], [10, 0], [2, 0], [11, 0], [2, 0], [2, 0], [10, 0], [2, 0], [2, 0], [1, 0], [9, 0],
                                [9, 0], [1, 0], [2, 0], [1, 0], [1, 0], [2, 0], [1, 0], [2, 0], [2, 0], [0, 0], [2, 0], [2, 0], [11, 0], [2, 0], [2, 0], [10, 0], [2, 0], [2, 0], [1, 0], [9, 0],
                                [9, 0], [1, 0], [2, 0], [2, 0], [1, 0], [2, 0], [1, 0], [2, 0], [2, 0], [7, 0], [2, 0], [2, 0], [11, 0], [2, 0], [0, 0], [10, 0], [2, 0], [2, 0], [1, 0], [9, 0],
                                [9, 0], [1, 0], [2, 0], [2, 0], [1, 0], [2, 0], [1, 0], [2, 0], [2, 0], [11, 0], [2, 0], [2, 0], [11, 0], [2, 0], [2, 0], [10, 0], [2, 0], [2, 0], [1, 0], [9, 0],
                                [9, 0], [1, 0], [2, 0], [2, 0], [1, 0], [1, 0], [1, 0], [2, 0], [2, 0], [11, 0], [11, 0], [11, 0], [11, 0], [2, 0], [2, 0], [10, 0], [2, 0], [2, 0], [1, 0], [9, 0],
                                [9, 0], [1, 0], [2, 0], [2, 0], [10, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [10, 0], [10, 0], [2, 0], [2, 0], [1, 0], [2, 0],
                                [9, 0], [1, 0], [10, 0], [10, 0], [17, 2], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [10, 0], [10, 0], [10, 0], [9, 0], [9, 0], [9, 0], [1, 0], [2, 0],
                                [9, 0], [1, 0], [0, 0], [18, 1], [2, 0], [5, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [13, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [1, 0], [2, 0],
                                [9, 0], [1, 0], [5, 0], [1, 0], [1, 0], [9, 0], [16, 3], [9, 0], [16, 3], [2, 0], [2, 0], [2, 0], [10, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [1, 0], [9, 0],
                                [9, 0], [1, 0], [2, 0], [2, 0], [2, 0], [16, 0], [9, 0], [16, 3], [9, 0], [2, 0], [2, 0], [2, 0], [16, 2], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [1, 0], [9, 0],
                                [9, 0], [1, 0], [2, 0], [2, 0], [2, 0], [5, 0], [5, 0], [5, 0], [16, 0], [2, 0], [2, 0], [9, 0], [9, 0], [9, 0], [2, 0], [2, 0], [2, 0], [2, 0], [1, 0], [2, 0],
                                [9, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [8, 0], [2, 0],
                                [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [2, 0], [2, 0], [9, 0]],
                           [[19, 19, 0]],
                           (150, 30, 50), "Level 12: Ant City", offset)

level13 = levelclass.Level(13, [[8, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [6, 1], [9, 0],
                                [16, 0], [1, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [1, 0], [2, 0], [1, 0], [18, 1], [9, 0],
                                [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [1, 0], [2, 0], [2, 0], [19, 1], [9, 0],
                                [1, 0], [16, 2], [1, 0], [1, 0], [1, 0], [9, 0], [9, 0], [1, 0], [1, 0], [1, 0], [2, 0], [1, 0], [9, 0],
                                [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [9, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0], [1, 0], [9, 0],
                                [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [9, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0], [1, 0], [9, 0],
                                [5, 0], [5, 0], [5, 1], [5, 0], [5, 1], [9, 0], [5, 0], [16, 1], [9, 0], [9, 0], [2, 0], [1, 0], [9, 0],
                                [5, 0], [5, 3], [5, 0], [5, 3], [5, 0], [9, 0], [16, 0], [9, 0], [5, 0], [5, 3], [2, 0], [16, 3], [9, 0],
                                [5, 3], [9, 0], [5, 0], [5, 0], [5, 1], [9, 0], [5, 3], [5, 3], [5, 3], [5, 0], [2, 0], [9, 0], [9, 0],
                                [16, 0], [5, 1], [5, 1], [5, 3], [5, 0], [9, 0], [5, 3], [5, 2], [5, 1], [16, 0], [2, 0], [11, 0], [9, 0],
                                [9, 0], [9, 0], [5, 1], [5, 1], [5, 0], [9, 0], [5, 3], [5, 3], [5, 3], [9, 0], [2, 0], [10, 0], [9, 0],
                                [15, 0], [9, 0], [5, 1], [5, 1], [5, 1], [9, 0], [5, 0], [5, 0], [9, 0], [14, 0], [2, 0], [7, 0], [9, 0],
                                [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0]],
                           [[1, 1, 0], [8, 5, 3], [2, 6, 1]],
                           (0, 200, 80), "Final Level: The Trial of the True Strider", offset)

end_lobby = levelclass.Level(15, [[2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0],
                                  [2, 0], [17, 1], [0, 0], [12, 0], [1, 0], [13, 0], [1, 0], [0, 0], [0, 0], [0, 0], [2, 0], [1, 0], [1, 0], [1, 0], [2, 0],
                                  [2, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0],
                                  [2, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [16, 1], [6, 0], [16, 2], [2, 0],
                                  [2, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [6, 0], [5, 0], [6, 0], [2, 0],
                                  [2, 0], [1, 0], [12, 0], [13, 0], [3, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [16, 0], [6, 0], [16, 3], [2, 0],
                                  [2, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0],
                                  [2, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [8, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0],
                                  [2, 0], [1, 0], [14, 0], [15, 0], [4, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0],
                                  [2, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0],
                                  [2, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0],
                                  [2, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0],
                                  [2, 0], [5, 2], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0],
                                  [2, 0], [5, 0], [1, 0], [1, 0], [1, 0], [1, 0], [6, 1], [18, 1], [19, 1], [1, 0], [1, 0], [1, 0], [2, 0], [7, 0], [2, 0],
                                  [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0]],
                             [[8, 8, 0], [5, 2, 2], [7, 2, 3], [9, 12, 1], [10, 11, 2], [11, 10, 3], [11, 4, 1], [3, 14, 1]],
                             (0, 0, 0), "Temple of the One True Strider. (Congrats! You've won!)", offset)

level20 = levelclass.Level(12, [[2, 0], [2, 0], [2, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [2, 0], [2, 0], [2, 0],
                                [2, 0], [15, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [14, 0], [2, 0],
                                [2, 0], [1, 0], [1, 0], [1, 0], [0, 0], [7, 0], [10, 0], [11, 0], [1, 0], [1, 0], [1, 0], [2, 0],
                                [2, 0], [1, 0], [1, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 0], [1, 0], [1, 0], [1, 0], [2, 0],
                                [2, 0], [1, 0], [1, 0], [1, 0], [2, 0], [9, 0], [9, 0], [2, 0], [1, 0], [1, 0], [1, 0], [2, 0],
                                [2, 0], [0, 0], [1, 0], [1, 0], [2, 0], [9, 0], [9, 0], [2, 0], [0, 0], [1, 0], [0, 0], [2, 0],
                                [2, 0], [1, 0], [1, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 0], [1, 0], [1, 0], [1, 0], [2, 0],
                                [2, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0],
                                [2, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0],
                                [2, 0], [2, 0], [2, 0], [1, 0], [1, 0], [8, 0], [1, 0], [1, 0], [1, 0], [2, 0], [2, 0], [2, 0],
                                [9, 0], [9, 0], [2, 0], [2, 0], [9, 0], [9, 0], [9, 0], [9, 0], [2, 0], [2, 0], [9, 0], [9, 0],
                                [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0]],
                           [[6, 10, 0], [4, 5, 3], [10, 4, 1]], (0, 0, 78), "Level EX: Block Castle", offset)

credits_placeholder = levelclass.Level(3, [[2, 0], [2, 0], [2, 0],
                                           [2, 0], [1, 0], [2, 0],
                                           [2, 0], [2, 0], [2, 0]],
                                       [[2, 2, 0]], (0, 0, 0), "The End (Press any key to continue!)", offset)

level50 = levelclass.Level(8, [[2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [9, 0],
                               [2, 0], [8, 0], [1, 0], [10, 0], [11, 0], [7, 0], [2, 0], [9, 0],
                               [2, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0], [9, 0],
                               [2, 0], [3, 0], [2, 0], [12, 0], [0, 0], [0, 0], [2, 0], [9, 0],
                               [2, 0], [4, 0], [18, 0], [17, 1], [1, 0], [1, 0], [2, 0], [9, 0],
                               [2, 0], [1, 0], [1, 0], [19, 0], [1, 0], [6, 1], [2, 0], [9, 0],
                               [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [9, 0],
                               [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0]],
                           [[2, 2, 0], [5, 3, 2]], (0, 0, 0), "TILE TESTING", offset)

level51 = levelclass.Level(5, [[8, 0], [1, 0], [1, 0], [1, 0], [1, 0],
                               [1, 0], [1, 0], [1, 0], [1, 0], [1, 0],
                               [1, 0], [1, 0], [4, 0], [1, 0], [1, 0],
                               [1, 0], [1, 0], [1, 0], [1, 0], [1, 0],
                               [1, 0], [1, 0], [1, 0], [1, 0], [7, 0]],
                           [[1, 1, 0], [3, 3, 1]], (128, 0, 0), "CRATE TESTING", offset)

menu1 = levelclass.Level(6, [[9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0],
                             [9, 0], [7, 0], [9, 0], [9, 0], [7, 0], [9, 0],
                             [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0],
                             [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0],
                             [9, 0], [8, 0], [1, 0], [1, 0], [1, 0], [9, 0],
                             [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0]],
                         [[2, 5, 0]], (20, 20, 20), "Concept Menu 1", offset)

menu2 = levelclass.Level(6, [[9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0],
                             [1, 0], [9, 0], [1, 0], [9, 0], [1, 0], [9, 0],
                             [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0],
                             [8, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0],
                             [9, 0], [1, 0], [9, 0], [1, 0], [9, 0], [1, 0],
                             [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0]],
                         [[1, 4, 0]], (30, 30, 30), "Concept Menu 2", offset)

menu3 = levelclass.Level(6, [[9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0],
                             [1, 0], [9, 0], [1, 0], [9, 0], [1, 0], [9, 0],
                             [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [7, 0],
                             [8, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0],
                             [9, 0], [1, 0], [9, 0], [1, 0], [9, 0], [1, 0],
                             [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0]],
                         [[1, 4, 0]], (40, 20, 20), "Concept Menu 3-1", offset)

menu4 = levelclass.Level(6, [[9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0],
                             [1, 0], [9, 0], [1, 0], [9, 0], [1, 0], [9, 0],
                             [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0],
                             [8, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0],
                             [9, 0], [1, 0], [9, 0], [1, 0], [9, 0], [1, 0],
                             [9, 0], [9, 0], [9, 0], [9, 0], [9, 0], [9, 0]],
                         [[1, 4, 0]], (50, 10, 10), "Concept Menu 3-2", offset)

difficultyA = [0]
difficultyB = [1, 2]
difficultyC = [3, 4, 6, 7, 14]
difficultyD = [5, 8, 9, 10, 11, 12]
difficultyN = [13, 15, 16, 17, 18, 19, 20, 21, 22]