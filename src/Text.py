from textblob import TextBlob


class Text:
    content = ""
    sentences = []
    sentiments = []
    blob = TextBlob
    colours = []
    colour = ""
    # scaled_colours = None

    def __init__(self, text_string, choosencolour):
        self.colour = choosencolour
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
        rgb_middle = 255/2
        for sentiment in self.sentiments:
            emotion = round(rgb_middle + sentiment.polarity * rgb_middle)
            if self.colour == "red":
                red = emotion
                green = 0
                blue = 0
                self.colours.append((red, green, blue))
            if self.colour == "green":
                green = emotion
                blue = 0
                red = 0
                self.colours.append((red, green, blue))
            if self.colour == "blue":
              blue = emotion
              green = 0
              red = 0
              self.colours.append((red, green, blue))

