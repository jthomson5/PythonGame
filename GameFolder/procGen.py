from typing import Iterator, Tuple
from map import GameMap
import tile_types
import random
import tcod

class RectangularRoom:
    def __init__(self, x: int, y: int, width: int, height:int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    @property
    def center(self) -> Tuple[int, int]:
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return center_x, center_y
    
    @property
    def inner(self) -> Tuple[slice, slice]:     # Return inner area of room as 2D array index
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)
    
def generateDungeon(map_width, map_height) -> GameMap:
    dungeon = GameMap(map_width, map_height)

    room_1 = RectangularRoom(x=20, y=15, width=10, height=15)
    room_2 = RectangularRoom(x=35, y=15, width=10, height=15)

    dungeon.tiles[room_1.inner] = tile_types.floor
    dungeon.tiles[room_2.inner] = tile_types.floor

    for x, y in tunnel(room_2.center, room_1.center):
        dungeon.tiles[x, y] = tile_types.floor

    return dungeon

def tunnel(     # Add tunnel between dungeons
    start: Tuple[int, int], end: Tuple[int, int]
) -> Iterator[Tuple[int, int]]:
     x1, y1 = start
     x2, y2 = end
     if random.random() < 0.5:
         corner_x, corner_y = x2, y1    # Moving horizontally, then vertically
     else:
         corner_x, corner_y = x1, y2    # Moving vertically, then horizontally
    # Generate coordinates for the tunnel
     for x, y in tcod.los.bresenham((x1, y1), (corner_x, corner_y)).tolist():
         yield x, y
     for x, y in tcod.los.bresenham((corner_x, corner_y), (x2, y2)).tolist():
         yield x, y