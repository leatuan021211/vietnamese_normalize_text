import re

from settings import TONES


class ToneNormalizer(object):
    pattern = re.compile(r"(\w*)([áàảãạấầẩẫậắằẳẵặéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ])(\w*)")

    @classmethod
    def normalize(cls, text):

        def replace(match):
            accented = match.group(2)
            base, tone = TONES[accented]
            return f"{match.group(1)}{base}{match.group(3)}{tone}"

        text = cls.pattern.sub(replace, text)
        return text
