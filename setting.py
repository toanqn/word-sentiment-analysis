import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
STOP_WORDS = os.path.join(DIR_PATH, 'stopwords-vi.txt')
SPECIAL_CHARACTER = '0123456789%@$.,=+-!;/()*"&^:#|\n\t\''
EMO = os.path.join(DIR_PATH, 'VnEmoLex.csv')