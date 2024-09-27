import re

from settings import LETTERS


class LetterNormalizer(object):

    pattern = re.compile(r"\b(" + "|".join(map(re.escape, LETTERS)) + r")\b")

    @classmethod
    def normalize(cls, text: str):

        def replace_unit(match):
            return LETTERS[match.group(0)]

        return cls.pattern.sub(replace_unit, text)
