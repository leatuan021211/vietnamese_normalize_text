import re

from settings import SYMBOLS


class SymbolNormalizer(object):

    pattern = re.compile(r"([\s\S])(" + "|".join(map(re.escape, SYMBOLS)) + r")([\s\S])")

    @classmethod
    def normalize(cls, text: str):

        def replace_symbol(match):
            return (
                (match.group(1) if match.group(1) == " " else match.group(1) + " ")
                + SYMBOLS[match.group(2)]
                + (match.group(3) if match.group(3) == " " else match.group(3) + " ")
            )

        return cls.pattern.sub(replace_symbol, text)
