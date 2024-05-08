from typing import Tuple

import numpy as np

# Tile graphics structured type compatible with Console.tiles_rgb.
graphic_dt = np.dtype(      # dtype creates a data type that Numpy can use
    [
        ("ch", np.int32),   # Character in integer format
        ("fg", "3B"),       # Foreground color, 3 unsigned bytes, for RGB colors
        ("bg", "3B"),       # Background color, same as above
    ]
)

# Tile struct used for statically defined tile data.
tile_dt = np.dtype(
    [
        ("walkable", bool),      # True if tile is can be walked over
        ("transparent", bool),   # True if tile doesn't block FOV
        ("dark", graphic_dt),        # Graphics for when tile is not in FOV
    ]
)

def new_tile(
        *,
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:  
    return np.array((walkable, transparent, dark), dtype=tile_dt)    # Helper function for defining individual tiles

floor = new_tile(
    walkable=True, transparent=True, dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
)

wall = new_tile(
    walkable=False, transparent=False, dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
)