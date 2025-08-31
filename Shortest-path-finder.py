
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



# Search for empty position
def search_for_empty_position(current_row, current_pos):
    min_row = current_row - 1
    max_row = current_row + 1
    
    min_pos = current_pos - 1
    max_pos = current_pos + 1

    

    # Fix O search later
    try:
        # Same row
        if maze[current_row][min_pos] != "#":
            visited_positions.append([current_row, min_pos])
            move_to_position(current_row, min_pos)
            return
        elif maze[current_row][max_pos] != "#":
            visited_positions.append([current_row, max_pos])
            move_to_position(current_row, max_pos)
            return 
        
        # Lower Row
        elif maze[min_row][current_pos] != "#":
            visited_positions.append([min_row, current_pos])
            move_to_position(min_row, current_pos)
            return

        # Upper Row
        elif maze[max_row][current_pos] != "#":
            visited_positions.append([max_row, current_pos])
            move_to_position(max_row, current_pos)
            return
        
        else:
            return
    except:
        return


def move_to_position(row, pos):
    print("Moved")
    print(row, pos)
    

search_for_empty_position(current_row, current_index)


