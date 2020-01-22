class Grid:
    def __init__(self,size):
        self.size = size
        self.path = []
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
        self.allowed_moves = ['u','d','l','r','p','e']
        self.current_pos = (0,0)
    
    def print_grid(self):
        for i in range(self.size):
            res = ''
            for j in range(self.size):
                res = res + str(self.grid[i][j])
                if j < self.size - 1:
                    res = res + ','
            print(res)
            
    def move(self,m):
        if m not in self.allowed_moves:
            print('Unknown Command')
            return True
        
        if m == 'e':
            return False
        
        if m =='u':
            if self.current_pos[0] - 1 < 0:
                print("Cannot move Upwards")
                return True
            else:
                current_pos = (self.current_pos[0]-1,self.current_pos[1])
                
        if m == 'd':
            if self.current_pos[0] + 1 >= self.size:
                print("Cannot move downwards")
                return True
            else:
                current_pos = (self.current_pos[0]+1,self.current_pos[1])
                
        if m =='l':
            if self.current_pos[1] - 1 < 0:
                print("Cannot move left")
                return True
            else:
                current_pos = (self.current_pos[0],self.current_pos[1]-1)

        if m =='r':
            if self.current_pos[1] + 1 >= self.size:
                print("Cannot move left")
            else:
                current_pos = (self.current_pos[0],self.current_pos[1]+1)
        
        if m =='p':
            self.print_grid()
            return True
        
        self.path.append(current_pos)
        self.grid[self.current_pos[0]][self.current_pos[1]] = 'X'
        self.grid[current_pos[0]][current_pos[1]] = 'C'
        self.current_pos = current_pos
        return True

if __name__ == '__main__':
    grid = Grid(10)
    while True:
        print("Enter the move. Valid moves are: " +  grid.allowed_moves.__str__())
        move = input()
        if not grid.move(move):
            break

            