game_list = ["game1.txt", "game2.txt"]

for games in game_list:

    # read and parse move from input file and initialize variables
    moves = []
    red_captures = 0
    red_double_jumps = 0
    black_captures = 0
    black_double_jumps = 0
    red_pieces = 12
    black_pieces = 12
    winner = None

    f = open(games, "r")

    for line in f.readlines():
        point = line.strip().split()
        moves.append((point[0], point[1]))

    # iterate over all moves in the game
    i = 0

    while i in range(len(moves)):
        move = moves[i]
        
        # get the coordinates for red’s previous position
        red_prev_pos = move[0]
        # get the coordinates for red’s next position
        red_next_pos = move[1]
        # determine if:
            #- Red advanced a single space
            #- Red jumped a black piece
            #- Red double-jumped 2 black pieces
        if abs(int(red_prev_pos[0]) - int(red_next_pos[0])) == 1:
            pass
        elif abs(int(red_prev_pos[0]) - int(red_next_pos[0])) == 2:
            red_captures += 1
            black_pieces -= 1
            print("Red jumped a black piece!")    
        elif (abs(int(red_prev_pos[0]) - int(red_next_pos[0])) == 4) or \
            abs(int(red_prev_pos[0]) - int(red_next_pos[0])) == 0:
            red_captures += 2
            black_pieces -= 2
            red_double_jumps += 1
            print("Red double-jumped two black pieces!")

        # check to see if red captured all of black’s pieces
        if black_pieces == 0:
            winner = "Red"
            break

        # get the coordinates for black previous position
        black_prev_pos = moves[i+1][0]
        # get the coordinates for black next position
        black_next_pos = moves[i+1][1]

        # determine if:
            #- Black advanced a single space
            #- Black jumped a black piece
            #- Black double-jumped 2 black pieces
        if abs(int(black_prev_pos[0]) - int(black_next_pos[0])) == 1:
            pass
        elif abs(int(black_prev_pos[0]) - int(black_next_pos[0])) == 2:
            black_captures += 1
            red_pieces -= 1
            print("Black jumped a red piece!")
        elif abs(int(black_prev_pos[0]) - int(black_next_pos[0])) == 4 or \
            abs(int(black_prev_pos[0]) - int(black_next_pos[0])) == 0:
            black_captures += 2
            red_pieces -= 2
            black_double_jumps += 1
            print("Black double-jumped two red pieces!")

        # check to see if black captured all of red’s pieces
        if red_pieces == 0:
            winner = "Black"
            break

        i += 2
    # output the results in the format specified in “Output Format”
    print("")
    print("----- Game Stats -----")
    print("Winner: " + winner)
    print("Total Moves: " + str(len(moves)))
    print("Red Captures: " + str(red_captures))
    print("Red Double-jumps: " + str(red_double_jumps))
    print("Black Captures: " + str(black_captures))
    print("Black Double-jumps: " + str(black_double_jumps))
    print("")