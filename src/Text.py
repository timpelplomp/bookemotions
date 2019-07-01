from textblob import TextBlob


class Text:
    content = ""
    sentences = []
    sentiments = []
    blob = TextBlob
    colours = []
    colour = ""
    # scaled_colours = None

    def __init__(self, text_string, chosen_colour="green"):
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

    def print_sentattrs(self, when_break = None):
        for i, sentiment in enumerate(self.sentiments):
            print("polarity: " + str(sentiment.polarity) + " for: " + str(self.sentences[i]))
            if when_break:
                if i == when_break:
                    break


example_sent = "The lake was deep and dark."
example_subj = "I found the lake deep and dark. I love fish."
example_text = Text(example_subj)
print(example_text.sentiments)

with open("resources/books/Carroll_Alice.txt", "r") as f:
    alice_text = f.read()

with open("resources/books/Shakespeare_Hamlet.txt", "r") as f:
    hamlet_text = f.read()
example_alice_text = Text(alice_text)
example_alice_text.print_sentattrs(when_break=3)
example_hamlet_text = Text(hamlet_text)
example_hamlet_text.print_sentattrs(when_break=40)
