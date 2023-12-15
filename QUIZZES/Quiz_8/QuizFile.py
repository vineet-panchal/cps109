# Quiz File
# Iguana vs. Snakes (epic): https://youtu.be/el4CQj-TCbA?t=83

# Do not modify the GridClassFile.py
import GridClassFile

# The only thing you should need to modify is this function below!
# Given a grid state, decide on the best move for the iguana
# Note that the iguana moves first (then the snakes)
# Return either "up", "down", "left", or "right"

# To win, the iguana ('I') must reach the goal ('G')
# The iguana will always spawn at the centre of the grid
# Snakes will always move in the direction of the iguana.
# Snakes will always move in the direction of the iguana.
# If a snake touches the iguana you lose ('X'). If the iguana touches the goal you win ('W').
def generate_iguana_move(my_grid_environment):
    # Hints: you may find the following useful:
    

    # # my_grid_environment.goal gives the goal position [x, y]
    goal = my_grid_environment.goal
    # print(goal)
    # # my_grid_environment.iguana_pos gives the iguana position [x, y]
    iguana_pos = my_grid_environment.iguana_pos
    # print(iguana_pos)
    
    # moves = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    # # moves (x, y): up, down, left, right
    

    # calculate the vector towards the goal
    
    # Solution 1
    # goal_vector = [goal[0] - iguana_pos[0], goal[1] - iguana_pos[1]]

    #     # move in the direction of the vector
    # move = ''
    # if goal_vector[0] > 0:
    #     move = 'right'
    # elif goal_vector[1] > 0:
    #     move = 'down'
    # elif goal_vector[0] < 0:
    #     move = 'left'
    # elif goal_vector[1] < 0:
    #     move = 'up'

    # return move
    
    # Solution 2
    # calculate the vector towards the goal
    goal_vector = [goal[0] - iguana_pos[0], goal[1] - iguana_pos[1]]

        # move in the direction of the vector
    move = ''
    if goal_vector[1] > 0:
        move = 'down'
    elif goal_vector[0] < 0:
        move = 'left'
    elif goal_vector[1] < 0:
        move = 'up'
    elif goal_vector[0] > 0:
        move = 'right'

    return move
    

    # return "UP" # TODO: Replace this with some more winning decision!

# Optional bonus: Can you devise an algorithm for if the iguana moves 2 tiles at a time?
#def generate_iguana_move_bonus(my_grid_environment):
    #return "up"

if __name__ == "__main__":
    print("Initializing escape simulation")
    generate_metrics = True # Change this to True to generate your average performance!

    my_grid = GridClassFile.GridEnvironment(size=9, num_snakes=5, do_print=True)

    my_grid.print_grid("start")

    either_exit = False
    while not either_exit:
        
        iguana_move = generate_iguana_move(my_grid)
        my_grid.run_round(iguana_move)

        if (my_grid.iguana_escaped):
            print("The iguana has escaped! (win)")
            either_exit = True
        elif (my_grid.iguana_ded):
            print("The snakes are victorious... (loss)")
            either_exit = True

    # Bonus: Try to devise an algorithm for if the iguana has a speed of 2!
    '''
    my_grid_2 = GridClassFile.GridEnvironment(size=9, num_snakes=5)

    my_grid_2.print_grid("start")

    either_exit = False
    while not either_exit:
        
        iguana_move = generate_iguana_move(my_grid_2)
        my_grid_2.run_round(iguana_move, 2)

        if (my_grid_2.iguana_escaped):
            print("The iguana has escaped! (win)")
            either_exit = True
        elif (my_grid_2.iguana_ded):
            print("The snakes are victorious... (loss)")
            either_exit = True
    '''

    # Metrics generation
    if (generate_metrics):
        num_victories = 0
        num_losses = 0
        for i in range(1000):
            my_grid = GridClassFile.GridEnvironment(size=9, num_snakes=5, do_print=False)

            #my_grid.print_grid("start")

            either_exit = False
            while not either_exit:

                iguana_move = generate_iguana_move(my_grid)
                my_grid.run_round(iguana_move)

                if (my_grid.iguana_escaped):
                    #print("The iguana has escaped! (win)")
                    num_victories += 1
                    either_exit = True
                elif (my_grid.iguana_ded):
                    #print("The snakes are victorious... (loss)")
                    num_losses += 1
                    either_exit = True
        print("Wins:", num_victories, "Losses:", num_losses, "Win Ratio:", num_victories/num_losses, "Win Percent:", round(num_victories/1000.0, 4))
    
    
