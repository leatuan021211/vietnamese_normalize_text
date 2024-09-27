import re

from settings import ACRONYMS


class AcronymNormalizer(object):

    pattern = re.compile(r"\b(" + "|".join(map(re.escape, ACRONYMS)) + r")\b")

    @classmethod
    def normalize(cls, text: str):
        def replace_unit(match):
            return ACRONYMS[match.group(0)]

        return cls.pattern.sub(replace_unit, text)
