import time


#Setting up maze
maze = [
    ["#", "#", "#", "#", "#", "#", "#", "O", "#", "#"],
    ["#", " ", "#", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", "#", " ", "#", "#", " ", "#"],
    ["#", "#", "#", " ", " ", " ", "#", " ", " ", "#"],
    ["#", " ", " ", " ", "#", " ", "#", " ", "#", "#"],
    ["#", " ", "#", " ", "#", " ", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", "#", "#", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#", "#"],
    ["#", "#", "#", "#", "#", "X", "#", "#", "#", "#"]
]

current_row = 9
current_index = 5



# Visited positions
visited_positions = []
visited_counter = 0

#Exit_options
tracked_exits_list = []


# Search for empty position
def search_for_empty_position(current_row, current_pos):
    min_row = current_row - 1
    max_row = current_row + 1
    
    min_pos = current_pos - 1
    max_pos = current_pos + 1


    # Fix O search later and moving to visited pos
    try:
        # Current row
        if maze[current_row][min_pos] != "#" and [current_row, min_pos] not in visited_positions:
            visited_positions.append([current_row, min_pos])
            track_exits(current_row, min_row, max_row, current_pos, min_pos, max_pos)
            move_to_position(current_row, min_pos, current_row, current_pos)
            return
        elif maze[current_row][max_pos] != "#" and [current_row, max_pos] not in visited_positions:
            visited_positions.append([current_row, max_pos])
            move_to_position(current_row, max_pos, current_row, current_pos)
            return 
        
        # Lower Row
        elif maze[min_row][current_pos] != "#" and [min_row, current_pos] not in visited_positions:
            visited_positions.append([min_row, current_pos])
            move_to_position(min_row, current_pos, current_row, current_pos)
            return

        # Upper Row
        elif maze[max_row][current_pos] != "#" and [max_row, current_pos] not in visited_positions:
            visited_positions.append([max_row, current_pos])
            move_to_position(max_row, current_pos, current_row, current_pos)
            return
        
        else:
            visited_positions.append([current_row, current_pos])
            backtrack()
            return
    except:
        return


def move_to_position(row, pos, oldrow, oldpos):
    global current_row, current_index    
    


    maze[row][pos] = "X"
    maze[oldrow][oldpos] = " "
    
    current_row = row
    current_index = pos
    time.sleep(1)
    print("")
    for row in maze:
        print(row)
        

def track_exits(current_row, min_row, max_row, current_pos, min_pos, max_pos):
        
        # Current row
        if maze[current_row][min_pos] != "#" and [current_row, min_pos] not in visited_positions:
            tracked_exits_list.append([current_row, current_pos])   
        if maze[current_row][max_pos] != "#" and [current_row, max_pos] not in visited_positions:
            tracked_exits_list.append([current_row, current_pos])
            
        # Lower Row
        if maze[min_row][current_pos] != "#" and [min_row, current_pos] not in visited_positions:
            tracked_exits_list.append([current_row, current_pos])
            
        # Upper Row
        if maze[max_row][current_pos] != "#" and [max_row, current_pos] not in visited_positions:
            tracked_exits_list.append([current_row, current_pos])
        
        print(tracked_exits_list)
        return

def backtrack(current_row, min_row, max_row, current_pos, min_pos, max_pos):
    temporary_backtrack_list = visited_positions



    for i, exit_pos in tracked_exits_list:
        # Okay, i will search for how far back the nearest exit tile is, then i will get how fat that is back in the visited_positionslist, then trace back until that position though the list

    
    



if __name__ == "__main__":
    for row in maze:
        print(row)
    while maze[current_row][current_index] != "O":
        search_for_empty_position(current_row, current_index)




