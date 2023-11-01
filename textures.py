import pygame as pg
import moderngl as mgl


class Texture:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx

        # load textures
        self.texture_0 = self.load("frame.png")
        self.texture_array_0 = self.load("texture_array.png", is_tex_array=True)

        # assign texture units
        self.texture_0.use(location=0)
        self.texture_array_0.use(location=1)

    def load(self, filename, is_tex_array=False):
        texture = pg.image.load(f"assets/{filename}")
        texture = pg.transform.flip(texture, flip_x=True, flip_y=False)

        if is_tex_array:
            num_layers = (
                3 * texture.get_height() // texture.get_width()
            )  # 3 textures per layer
            texture = self.app.ctx.texture_array(
                size=(
                    texture.get_width(),
                    texture.get_height() // num_layers,
                    num_layers,
                ),
                components=4,
                data=pg.image.tostring(texture, "RGBA"),
            )
        else:
            texture = self.ctx.texture(
                size=texture.get_size(),
                components=4,
                data=pg.image.tostring(texture, "RGBA", False),
            )
        texture.anisotropy = 32.0

        texture.build_mipmaps()
        # texture.filter = (mgl.NEAREST, mgl.NEAREST)
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)

        return texture
