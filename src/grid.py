import random

class Grid:
    """Representerar spelplanen. Du kan ändra standardstorleken och tecknen för olika rutor. """
    width = 36
    height = 12
    empty = "."  # Tecken för en tom ruta
    #wall = "■"   # Tecken för en ogenomtränglig vägg
    wall = "|"   # Tecken för en ogenomtränglig vägg
    # Inner wall cordinate
    wall_placement = {
        "hight_wall": (5, 20, 4),   # uper wall
        "r_wall": (4, 10, 20),   # lower wall
        "down_wall": (5, 20, 9),    # the right side wall
        "doors": (17, 7, 10),    # the right side wall
    }
    
    
    def __init__(self):
        """Skapa ett objekt av klassen Grid"""
        # Spelplanen lagras i en lista av listor. Vi använder "list comprehension" för att sätta tecknet för "empty" på varje plats på spelplanen.
        self.data = [[self.empty for y in range(self.width)] for z in range(
            self.height)]

    def get(self, x, y):
        """Hämta det som finns på en viss position"""
        return self.data[y][x]

    def set(self, x, y, value):
        """Ändra vad som finns på en viss position"""
        self.data[y][x] = value

    def set_player(self, player):
        self.player = player

    def clear(self, x, y):
        """Ta bort item från position"""
        self.set(x, y, self.empty)

    def __str__(self):
        """Gör så att vi kan skriva ut spelplanen med print(grid)"""
        xs = ""
        for y in range(len(self.data)):
            row = self.data[y]
            for x in range(len(row)):
                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += "@"
                else:
                    xs += str(row[x])
            xs += "\n"
        return xs


    def make_walls(self):
        """Skapa väggar runt hela spelplanen"""
        for i in range(self.height):
            self.set(0, i, self.wall)
            self.set(self.width - 1, i, self.wall)

        for j in range(1, self.width - 1):
            self.set(j, 0, self.wall)
            self.set(j, self.height - 1, self.wall)


        # get Doors positions
        dx1, dy1, dx2  = self.wall_placement["doors"]
        
        startxhw, stopxhw , yhw = self.wall_placement["hight_wall"]
        # print(str(xw))
        # Horizontal wall (leave an opening)
        for x in range(startxhw, stopxhw):
            if x != dx1:  # Doorway20
                self.set(x, yhw, self.wall)
      
      
        # Vertical wall connected to the horizontal wall
        startydw, stopydw, xdw = self.wall_placement["r_wall"]

        for y in range(startydw, stopydw):
            if y != dy1:  # Doorway
                self.set(xdw, y, self.wall)   
                       
        # Second horizontal wall connected to the vertical wall
        startxrw, stopxrw, yrw = self.wall_placement["down_wall"]
        for x in range(startxrw, stopxrw):
            if x != dx2:  # Doorway
                self.set(x, yrw, self.wall)
    
    # Används i filen pickups.py
    def get_random_x(self):
        """Slumpa en x-position på spelplanen"""
        return random.randint(0, self.width-1)

    def get_random_y(self):
        """Slumpa en y-position på spelplanen"""
        return random.randint(0, self.height-1)


    def is_empty(self, x, y):
        """Returnerar True om det inte finns något på aktuell ruta"""
        return self.get(x, y) == self.empty


