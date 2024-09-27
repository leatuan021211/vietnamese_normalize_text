from utils.normalizer import NumberNomalizer
from utils.normalizer import DateNormalizer
from utils.normalizer import TextNormalizer
from utils.embedding import WordByPhonemesEmbedding

print("-----------------TEST NUMBER----------------")
print(NumberNomalizer.normalize("11112223"))
print(NumberNomalizer.normalize("101"))
print(NumberNomalizer.normalize("1001"))
print(NumberNomalizer.normalize("10001"))
print("------------------TEST DATE-----------------")
print(DateNormalizer.normalize("11/12/2002"))
print(DateNormalizer.normalize("17-02-2003"))
print(DateNormalizer.normalize("ngày 17/02"))
print(DateNormalizer.normalize("tháng 02/2003"))
print("--------------TEXT NORMALIZE----------------")
text = "Sáng nay 11/12/2002, lực... lượng cứu hộ đã mở rộng phạm vi tìm kiếm thêm 11122002 m về phía cánh đồng gần khu vực nhà ở của các hộ dân. Thêm hai nạn nhân vừa được tìm thấy, nâng tổng số người tử vong lên 32."
print(text)
text_normalize = TextNormalizer()
norm_text = text_normalize(text)
print(norm_text)
print("-----------------TEST EMBEDDING----------------")
wbp_embedd = WordByPhonemesEmbedding()
print(len(wbp_embedd(norm_text)))
