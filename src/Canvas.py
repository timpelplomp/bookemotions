from PIL import Image, ImageDraw
import os

from src.Text import Text


class Canvas:

    dimensions = None
    colour_space = "RGB"
    background = "white"

    # the folder where pictures reside in
    repository = "images"
    image = None
    text = None
    drawer = None
    rec_height = 2
    scaled_colours = None

    def __init__(self, text, dimensions=(200, 200)):
        self.dimensions = dimensions
        self.text = Text(text)

        if len(self.text.colours) * self.rec_height > dimensions[1]:
            self.scaled_colours = self.scaled_colours
        else:
            self.scaled_colours = text.colours

        self.image = Image.new(self.colour_space, self.dimensions, self.background)
        self.drawer = ImageDraw.Draw(self.image)

    def draw(self):
        # x_offset = 0
        y_pos = 0
        x_pos = 0
        for colour in self.scaled_colours:
            self.drawer.rectangle([(x_pos, y_pos), (self.dimensions[0], y_pos + self.rec_height)],
                                  fill=colour)
            y_pos += self.rec_height + 1

    def save(self, name):
        self.image.save(os.path.join(self.repository, name))

    def __scale_colours(self):
        scaled_colours = []
        return scaled_colours


frame = Canvas("This is a beautiful day. I walk through the valley of death and despair. I hate this town.")
frame.draw()

frame.save("example.png")
