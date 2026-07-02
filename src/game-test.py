from src.grid import Grid
from src.player import Player
from src import pickups
import curses



# TODO: flytta denna till en annan fil
class GameState:
    """Samla spelets variabler i en klass."""
    def __init__(self):
        self.g = Grid()

        # Start player in the center of the grid - dive with and height to get center
        center_x = self.g.width // 2
        center_y = self.g.height // 2
        self.player = Player(center_x, center_y)

        self.score = 0
        self.inventory = []

        self.g.set_player(self.player)
        self.g.make_walls()
        pickups.randomize(self.g)

# TODO: flytta denna till en annan fil
def print_status(game_grid, state):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {state.score} points.")
    print(game_grid)

    

def start(state):
    command = "a"

    # Direction dictionary
    directions = {
        "w": (0, -1),   # up
        "a": (-1, 0),   # left
        "s": (0, 1),    # down
        "d": (1, 0)     # right
    }

    # Loop until the user presses Q or X
    while command not in ["q", "x"]:
        
        if command == "i":
            #print([item.name for item in pickups.inventory])
            #pickups.pickup_print_list()
            pickups.pickup_print_list2()
            
        print_status(state.g, state)
        command = input("Use WASD to move, Q/X to quit. ")
        command = command.casefold()[:1]

        # Handle movement
        if command in directions:
            dx, dy = directions[command]
            
            if state.player.can_move(dx, dy, state.g):
                # Check what's on the destination tile
                maybe_item = state.g.get(
                    state.player.pos_x + dx,
                    state.player.pos_y + dy
                )
                
                # Move the player
                state.player.move(dx, dy)

                # Pick up item if there is one
                if isinstance(maybe_item, pickups.Item):
                    
                    pickups.get_item_score(maybe_item)
                    state.score += maybe_item.value
                    print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
                    state.g.clear(state.player.pos_x, state.player.pos_y)
                else:
                    print(f"The floor is lava - You will lose -1 point")
                    state.score -= 1
                    state.g.clear(state.player.pos_x, state.player.pos_y)

                    
    
    # Executed when the loop ends
    print("Thank you for playing!")
    
# __name__ skapas av Python och sätts till "__main__" om man startar game.py
# direkt. Detta är för att undvika att start-funktionen körs om man importerar
# saker från game.py i en annan fil, till exempel vid testning.
if __name__ == "__main__":
    game_state = GameState()
    start(game_state)
