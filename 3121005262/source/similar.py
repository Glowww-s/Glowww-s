import numpy as np


# 计算余弦相似度
def cosine_similarity(doc_dicts):
    a = np.array(list(doc_dicts[0].values()))
    b = np.array(list(doc_dicts[1].values()))
    cos_sim = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    assert (0 <= cos_sim <= 1), "相似度的值超出上下限，算法出错。"
    return cos_sim
