class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, x, y, grid):
        # Inside the walls (assuming walls are on the border)
        min_x = 1
        max_x = grid.width - 2
        min_y = 1
        max_y = grid.height - 2
        next_x = self.pos_x + x
        next_y = self.pos_y + y
        print(f"Next position: ({next_x}, {next_y})")
        print(grid.wall_placement)
 
        # en masssa if-statser BLÄ

        if min_x <= next_x <= max_x and min_y <= next_y <= max_y:
            # get Doors positions
            dx1, dy1, dx2  = grid.wall_placement["doors"]
            startxhw, stopxhw , yhw = grid.wall_placement["hight_wall"]
            startxdw, stopxdw, ydw = grid.wall_placement["down_wall"]
            startydw, stopydw, xrw = grid.wall_placement["r_wall"]
            
            # if yhw == next_y and startxhw <= next_x < stopxhw and next_x != dx1 or ydw == next_y:
            if yhw == next_y and startxhw <= next_x <= stopxhw and next_x != dx1 or ydw == next_y and startxdw <= next_x <= stopxdw and next_x != dx2 or startydw <= next_y < stopydw and xrw == next_x and next_y !=dy1:
                return False
               
            return True

        # return true  - if all the min and max i match                                   
        #return min_x <= next_x <= max_x and min_y <= next_y <= max_y

