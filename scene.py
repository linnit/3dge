from settings import *
from world import World
from world_objects.hud import Hud
from world_objects.voxel_marker import VoxelMarker


class Scene:
    def __init__(self, app) -> None:
        self.app = app
        self.world = World(self.app)
        self.voxel_marker = VoxelMarker(self.world.voxel_handler)
        self.hud = Hud(self.world)

    def update(self):
        self.world.update()
        self.voxel_marker.update()
        self.hud.update()

    def render(self):
        self.world.render()
        self.voxel_marker.render()
        self.hud.render()
