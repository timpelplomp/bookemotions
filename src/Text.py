from textblob import TextBlob


class Text:
    content = ""
    sentences = []
    sentiments = []
    blob = TextBlob
    colours = []
    colour = ""
    # scaled_colours = None

    def __init__(self, text_string, chosen_colour):
        self.colour = chosen_colour
        self.content = text_string
        self.blob = TextBlob(self.content)
        self.sentences = self.blob.sentences
        self.fill_sentiments()
        self.fill_colours()

    def fill_sentiments(self):
        self.sentiments = []
        if not self.sentiments:  # wenn die liste leer ist, fahre fort
            for sentence in self.sentences:
                self.sentiments.append(sentence.sentiment)

        else:
            print("was already filled with sentiments")

    def fill_colours(self):
        self.colours = []
        rgb_middle = 255/2
        for sentiment in self.sentiments:
            emotion = round(rgb_middle + sentiment.polarity * rgb_middle)
            red = 0
            green = 0
            blue = 0

            if self.colour == "red":
                red = emotion

            if self.colour == "green":
                green = emotion

            if self.colour == "blue":
                blue = emotion

            self.colours.append((red, green, blue))
