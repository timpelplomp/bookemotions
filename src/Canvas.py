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

    def __init__(self, text, dimensions=(200, 200)):
        self.dimensions = dimensions
        self.text = Text(text)
        self.image = Image.new(self.colour_space, self.dimensions, self.background)
        self.drawer = ImageDraw.Draw(self.image)

    def draw(self):
        x_offset = 0
        y_pos = 0
        for colour in self.text.colours:
            self.drawer.rectangle([(x_offset, y_pos,), (x_offset+2, self.dimensions[1])], fill=colour, width=2)
            x_offset += 2

    def save(self, name):
        self.image.save(os.path.join(self.repository, name))


frame = Canvas("This is a beautiful day. I walk through the valley of death and despair. I hate this town.")
frame.draw()

frame.save("example.png")
