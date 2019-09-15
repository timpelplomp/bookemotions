from textblob import TextBlob
# from textblob.sentiments import NaiveBayesAnalyzer
from textblob.sentiments import PatternAnalyzer
import os
import nltk
nltk.download('movie_reviews')


nltk.download('punkt')


def sent_it(input_dir, output_dir):
    # output_text = PatternAnalyzer.analyze(PatternAnalyzer(), "I hate death.", keep_assessments=True)
    # print(output_text)
    for input_file in os.listdir(input_dir):
        basename = os.path.basename(input_file)
        output_file_path = os.path.join(output_dir, basename)

        with open("input/" + input_file, "r", encoding="utf-8") as i:
            input_text = i.read()
            blob = TextBlob(input_text)

        with open(output_file_path, "a", encoding="utf-8") as f:
            for sentence in blob.sentences:
                output_text = PatternAnalyzer.analyze(PatternAnalyzer(), sentence.string, keep_assessments=True)
                f.write(str(output_text))
                f.write(("\n"))


print(os.listdir(os.getcwd()))
sent_it("input", "output")
