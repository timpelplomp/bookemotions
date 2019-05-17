from textblob import TextBlob


class Text:
    content = ""
    sentences = []
    sentiments = []
    blob = TextBlob
    colours = []
    # scaled_colours = None

    def __init__(self, text_string):
        self.content = text_string
        self.blob = TextBlob(self.content)
        self.sentences = self.blob.sentences
        self.fill_sentiments()
        self.fill_colours()

    def fill_sentiments(self):
        if not self.sentiments:
            for sentence in self.sentences:
                self.sentiments.append(sentence.sentiment)

        else:
            print("was already filled with sentiments")

    def fill_colours(self):
        rgb_middle = 255/2
        for sentiment in self.sentiments:
            red = round(rgb_middle - sentiment.polarity * rgb_middle)
            green = round(rgb_middle - sentiment.subjectivity * rgb_middle)
            blue = 0

            self.colours.append((red, green, blue))
