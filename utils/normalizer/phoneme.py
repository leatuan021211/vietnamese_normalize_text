import re

from settings import SAME_PHONEMES


class PhonemeNormalizer(object):

    pattern = re.compile(r"(" + "|".join(map(re.escape, SAME_PHONEMES)) + r")")

    @classmethod
    def normalize(cls, text: str):

        def replace_symbol(match):
            return SAME_PHONEMES[match.group(0)]

        return cls.pattern.sub(replace_symbol, text)
