import re

from settings import UNITS


class UnitNormalizer(object):

    pattern = re.compile(r"\b(" + "|".join(map(re.escape, UNITS)) + r")\b")

    @classmethod
    def normalize(cls, text):

        def replace_unit(match):
            return UNITS[match.group(0)]

        return cls.pattern.sub(replace_unit, text)
