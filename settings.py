from numba import njit
import os
import numpy as np
import glm
import math


os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "DISABLE"

FPS = 0


WINDOW_WIDTH = 1800
WINDOW_HEIGHT = 1200
WINDOW_ASPECT_RATIO = WINDOW_WIDTH / WINDOW_HEIGHT

# resolution of the screen
WIN_RES = glm.vec2(WINDOW_WIDTH, WINDOW_HEIGHT)

# world generation
SEED = 16

# ray casting
MAX_RAY_DIST = 6

# chunk
CHUNK_SIZE = 48
H_CHUNK_SIZE = CHUNK_SIZE // 2
CHUNK_AREA = CHUNK_SIZE * CHUNK_SIZE
CHUNK_VOL = CHUNK_AREA * CHUNK_SIZE
CHUNK_SPHERE_RADIUS = H_CHUNK_SIZE * math.sqrt(3)

# world
WORLD_W, WORLD_H = 20, 2
WORLD_D = WORLD_W
WORLD_AREA = WORLD_W * WORLD_D
WORLD_VOL = WORLD_AREA * WORLD_H

# world center
CENTER_XZ = WORLD_W * H_CHUNK_SIZE
CENTER_Y = WORLD_H * H_CHUNK_SIZE


# camera
ASPECT_RATIO = WIN_RES.x / WIN_RES.y
FOV_DEG = 50
V_FOV = glm.radians(FOV_DEG)  # vertical fov
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO)  # horizontal fov
NEAR = 0.1
FAR = 2000.0
PITCH_MAX = glm.radians(89.0)

# player
PLAYER_SPEED = 0.01
PLAYER_ROT_SPEED = 0.003
PLAYER_POS = glm.vec3(CENTER_XZ, WORLD_H * CHUNK_SIZE, CENTER_XZ)
MOUSE_SENSITIVITY = 0.002

# colours
BG_COLOR = glm.vec3(0.21, 0.86, 0.95)

# textures
SAND = 1
GRASS = 2
DIRT = 3
STONE = 4
SNOW = 5
LEAVES = 6
WOOD = 7

# terrain levels
SEA_LEVEL = 0
SNOW_LEVEL = 54
STONE_LEVEL = 49
DIRT_LEVEL = 40
GRASS_LEVEL = 8
SAND_LEVEL = 7
