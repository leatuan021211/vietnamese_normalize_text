import re

from settings import PHONEMES, FINAL_CONSONANTS, HEAD_CONSONANTS, VOWELS
from utils.normalizer.text import TextNormalizer


class WordByPhonemesEmbedding(object):

    def __init__(self, phonemes=PHONEMES, normalize=TextNormalizer(), spliter=" "):
        self.phonemes = phonemes
        self.normalize = normalize
        self.spliter = spliter

    def _parse_head_constants(self, word):
        pattern = r'^(' + '|'.join(HEAD_CONSONANTS) + ')'
        match = re.match(pattern, word)
        head_consonant = None
        if match:
            head_consonant = r'\b' + match.group(1)
        return re.sub(pattern, '', word), head_consonant
    
    def _parse_vowels(self, word):
        pattern = r'^(' + '|'.join(VOWELS) + ')'
        match = re.match(pattern, word)
        vowel = None
        if match:
            vowel =  match.group(1)
        return re.sub(pattern, '', word), vowel

    def _parse_final_constants(self, word):
        pattern = r'^(' + '|'.join(FINAL_CONSONANTS) + ')'
        match = re.match(pattern, word)
        final_consonant = None
        if match:
            final_consonant =  match.group(1)
        return re.sub(pattern, '', word), final_consonant

    def word2vec(self, word:str):
        embedding_vector = [0] * len(PHONEMES)
        
        word, head_consonant = self._parse_head_constants(word)
        word, vowel = self._parse_vowels(word)
        word, final_consonant = self._parse_final_constants(word)
        
        if len(word) > 0:
            accent_or_break = word[-1]
            embedding_vector[PHONEMES.index(accent_or_break)] = 1
            
        if head_consonant is not None:
            embedding_vector[PHONEMES.index(head_consonant)] = 1
            
        if vowel is not None:
            embedding_vector[PHONEMES.index(vowel)] = 1
            
        if final_consonant is not None:
            embedding_vector[PHONEMES.index(final_consonant)] = 1
            
        return {
            "head_consonant": head_consonant,
            "final_consonant": final_consonant,
            "vowel": vowel,
            "emmbedding_vector": embedding_vector
        }

    def embedding(self, text):
        text = self.normalize.normalize(text)
        words = text.split(self.spliter)

        return [self.word2vec(word)["emmbedding_vector"] for word in words]

    def __call__(self, text):
        return self.embedding(text)
