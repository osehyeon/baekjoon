def cover_polyomino_greedy(board):
    result = ""
    i = 0

    while i < len(board):
        if board[i] == '.':
            # If the current position is '.', just add it to the result
            result += '.'
            i += 1
        else:
            # Count consecutive 'X's
            count = 0
            while i < len(board) and board[i] == 'X':
                count += 1
                i += 1

            # If the number of 'X's is not a multiple of 2, it's impossible to cover
            if count % 2 != 0:
                return -1

            # Add 'AAAA' for each group of four 'X's
            result += 'AAAA' * (count // 4)

            # Add 'BB' for any remaining pair of 'X's
            if count % 4:
                result += 'BB'

    return result

# Test cases
print(cover_polyomino_greedy(input()))  
