import re

from settings import PHONEMES
from utils.normalizer.text import TextNormalizer


class WordByPhonemesEmbedding(object):

    def __init__(self, phonemes=PHONEMES, normalize=TextNormalizer(), spliter=" "):
        self.phonemes = phonemes
        self.normalize = normalize
        self.spliter = spliter

    def word2vec(self, text):

        embedding_vector = [0] * len(self.phonemes)

        for idx in range(0, len(self.phonemes)):

            if text == "":
                return embedding_vector

            if self.phonemes[idx] in text:
                embedding_vector[idx] = 1
                text = re.sub(self.phonemes[idx], "", text)

        return embedding_vector

    def embedding(self, text):
        text = self.normalize.normalize(text)
        words = text.split(self.spliter)

        return [self.word2vec(word) for word in words]

    def __call__(self, text):
        return self.embedding(text)
