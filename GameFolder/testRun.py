import tcod
from engine import Engine
from input import EventHandler
from map import GameMap
from entity import Entity
from procGen import generateDungeon

def main():
    screen_width = 80       # Set width and height of screen
    screen_height = 50

    map_width = 80
    map_height = 45

    tileset = tcod.tileset.load_tilesheet(      # Font
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()      # Event handler init

    player = Entity(int(screen_width/2), int(screen_height/2), "@", (255, 255, 255))
    npc = Entity(int(screen_width/2 - 5), int(screen_height/2), "@", (255, 255, 0))
    entities = {npc, player}
    game_map = generateDungeon(map_width, map_height)
    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)


    with tcod.context.new_terminal(     # Creates terminal
        screen_width,
        screen_height,
        tileset = tileset,
        title = "Jasons Rougelike",
        vsync = True
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order = "F")   # Creates console, order F changes from [y,x] to [x,y]
        while True:
            root_console.print(x =player.x, y = player.y, string = player.char, fg = player.color)  # Print things to console
            engine.render(console=root_console, context=context)

            events = tcod.event.wait() # press w

            engine.handle_events(events)
                      
if __name__ == "__main__":
    main()