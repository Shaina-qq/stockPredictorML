-- 24 points represented in order
board = {}
for i = 1, 24 do board[i] = "." end

-- Function to print the board in ASCII layout
function print_board()
    -- Outer top row
    print(" " .. board[1] .. "-----" .. board[2] .. "-----" .. board[3])
    print(" |           |")
    print(" |  " .. board[4] .. "--" .. board[5] .. "--" .. board[6] .. "  |")
    print(" |  |     |  |")
    print(" " .. board[7] .. "--" .. board[8] .. "     " .. board[9] .. "--" .. board[10])
    print(" |  |     |  |")
    print(" |  " .. board[11] .. "--" .. board[12] .. "--" .. board[13] .. "  |")
    print(" |           |")
    print(" " .. board[14] .. "-----" .. board[15] .. "-----" .. board[16])
end

-- Place a piece function
function place_piece(player, pos)
    if board[pos] == "." then
        board[pos] = player
        return true
    else
        print("Position "..pos.." is occupied!")
        return false
    end
end

-- Simple loop to prototype placing
math.randomseed(os.time())
for turn = 1, 6 do  -- prototype with few moves
    print_board()
    
    -- Human move
    print("Your turn (X). Enter position 1-16:")
    local pos = tonumber(io.read())
    if not place_piece("X", pos) then
        turn = turn - 1  -- retry
    end

    -- Computer move
    local empty = {}
    for i = 1, 16 do
        if board[i] == "." then table.insert(empty, i) end
    end
    local move = empty[math.random(#empty)]
    place_piece("O", move)
    print("Computer placed at "..move)
end

print("Prototype done!")
print_board()
