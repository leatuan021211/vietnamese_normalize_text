from utils.normalizer.acronym import AcronymNormalizer
from utils.normalizer.date import DateNormalizer
from utils.normalizer.number import NumberNomalizer
from utils.normalizer.phoneme import PhonemeNormalizer
from utils.normalizer.unit import UnitNormalizer
from utils.normalizer.breaker import BreakNormalizer
from utils.normalizer.letter import LetterNormalizer
from utils.normalizer.symbol import SymbolNormalizer
from utils.normalizer.tone import ToneNormalizer
from utils.normalizer.character import CharacterNormalizer

DEFAULT_PIPELINE = [
    DateNormalizer,
    NumberNomalizer,
    LetterNormalizer,
    AcronymNormalizer,
    SymbolNormalizer,
    UnitNormalizer,
    PhonemeNormalizer,
    ToneNormalizer,
    CharacterNormalizer,
    BreakNormalizer,
]


class TextNormalizer(object):

    def __init__(self, pipeline=DEFAULT_PIPELINE, lower=True):
        self.pipeline = pipeline
        self.lower = lower

    def normalize(self, text):
        if self.lower:
            text = text.lower()

        for processor in self.pipeline:
            text = processor.normalize(text)

        return text

    def __call__(self, text):
        return self.normalize(text)
