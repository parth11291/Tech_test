
def print_grid(path):
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for x,y in path:
        grid[x][y] = 'X'
    curr_pos = path[-1]
    grid[curr_pos[0]][curr_pos[1]] ='C'
    for i in range(GRID_SIZE):
        res = ''
        for j in range(GRID_SIZE):
            res = res + str(grid[i][j])
            if j < GRID_SIZE - 1:
                res = res + ','
        print(res)

GRID_SIZE = 10
allowed_moves = ['u','d','l','r','p','e']
current_pos = (0,0)
path = [current_pos]

while True:
	print("Enter the command:")
	move = input()
	
	if move not in allowed_moves:
		print('Unknown Command')
	if move == 'e':
		break

	if move =='u':
		if current_pos[0] - 1 < 0:
			print("Cannot move Upwards")
			continue
		else:
			current_pos = (current_pos[0]-1,current_pos[1])
	
	if move == 'd':
		if current_pos[0] + 1 >= GRID_SIZE:
			print("Cannot move downwards")
			continue
		else:
			current_pos = (current_pos[0]+1,current_pos[1])

	if move =='l':
		if current_pos[1] - 1 < 0:
			print("Cannot move left")
			continue
		else:
			current_pos = (current_pos[0],current_pos[1]-1)

	if move =='r':
		if current_pos[1] + 1 >= GRID_SIZE:
			print("Cannot move left")
			continue
		else:
			current_pos = (current_pos[0],current_pos[1]+1)
	
	if move =='p':
		print_grid(path)
		print(current_pos)
		continue

	path.append(current_pos)
	

	

