from pyvi.pyvi import ViTokenizer
import csv
import setting

class FileReader(object):
    def __init__(self, filePath):
        self.filePath = filePath

    def read_stopword(self):
        with open(self.filePath, 'r') as f:
            stopwords = set([w.strip().replace(' ', '_') for w in f.readlines()])
        return stopwords

    def load_csv(self):
        dictionary = {}
        with open(self.filePath, 'r') as f:
            reader = csv.DictReader(f)
            for w in reader:
                word = w['word'].replace(' ', '_')
                pos = int(w['Positive'])
                neg = int(w['Negative'])
                dictionary[word] = pos - neg
        return dictionary

class NLP(object):
    def __init__(self, text=None):
        self.text = text
        self.__set_stopwords()

    def __set_stopwords(self):
        self.stopwords = FileReader(setting.STOP_WORDS).read_stopword()

    def segmentation(self):
        return ViTokenizer.tokenize(self.text)

    def split_words(self):
        text = self.segmentation()
        try:
            return [x.strip(setting.SPECIAL_CHARACTER).lower() for x in text.split()]
        except:
            return []

    def get_words_feature(self):
        split_words = self.split_words()
        return [word for word in split_words if word.encode('utf-8') not in self.stopwords]

class Sentiment(object):
    def __init__(self, text=None):
        self.score = 0
        self.text = text
        self.__get_EmoLex()
        self.__get_words_feature()

    def __get_EmoLex(self):
        self.emolex = FileReader(setting.EMO).load_csv()

    def __get_words_feature(self):
        self.words_feature = NLP(text=self.text).get_words_feature()

    def get_score(self):
        for w in self.words_feature:
            if(w in self.emolex.keys()):
                self.score += self.emolex[w]
        return self.score

if __name__ == '__main__':
    text = input('Input: ')
    score = Sentiment(text=text).get_score()
    if(score > 0):
        print('Positive!')
    else:
        if(score < 0):
            print('Negative!')
        else:
            print('Neutral!')
    print(score)