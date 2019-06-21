from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

from src.Text import Text


class Canvas:

    colour_space = "RGB"
    background = 0

    # the folder where pictures reside in
    repository = "images"
    dimensions = None
    image = None
    text = None
    drawer = None
    rec_height = 2
    scaled_colours = None
    chosen_colour = ""

    def __init__(self, text, chosen_colour):
        self.text = Text(text, chosen_colour)
        # x is 1 since we scale it later anyway - less memory
        self.dimensions = (1, (len(self.text.colours)) * (self.rec_height + 1))  # len colours - len sentences

        self.scaled_colours = self.text.colours

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

    def save(self, name, to_scale=(200, 200), blur=False):  # default value, later overwritten
        bbox = self.image.getbbox()
        self.image = self.image.crop(bbox)
        self.image = self.image.resize(to_scale)
        if blur:
            self.image = self.image.filter(ImageFilter.GaussianBlur(radius=2))

        self.image.save(os.path.join(self.repository, name))

    def draw_metadata(self, name, metadata, metadata2):
        img = Image.open(os.path.join(self.repository, name))
        font = ImageFont.truetype("Verdana.ttf", 20)
        font2 = ImageFont.truetype("Saga Italic.ttf", 20)
        d = ImageDraw.Draw(img)
        d.text((40, 170), metadata, fill=(255, 255, 255), font=font2, align="left")
        d.text((10, 150), metadata2, fill=(255, 255, 255), font=font, align="left")
        img.save(os.path.join(self.repository, name))


with open("resources/books/Carroll_Alice.txt", "r", encoding="utf-8") as f:
    plaintext = f.read()
frame = Canvas(plaintext, "green")  # chosen_colour can be "green", "blue", "red"
frame.draw()

frame.save("example.png", (300, 300), blur=True)


# TODO: Metadaten auf Leinwand übernehmen als Schleife über Dateien?
# TODO: center and or scale text automatically
filename = []
filename2 = []
entries = os.listdir("resources/books/")
for entry in entries:
    for part in entry.split("."):
        if part != "txt":
            filename2.append(part)
for file in filename2:
    for part in file.split("_"):
            filename.append(part)



print(filename)

frame.draw_metadata("example.png", filename[0]+"", filename[1]+"")


# frame_neg = Canvas("I hate my life", (300, 300))
# frame_neg.draw()
# frame_neg.save("negative.png")
