import numpy as np


# 合并计算文档向量
def vector_merge(wordfreq_dicts):
    keyword_lists = [wordfreq_list.keys() for wordfreq_list in wordfreq_dicts]  # 关键词列表
    key_merge = list(set(keyword_lists[0]) | set(keyword_lists[1]))  # 合并的key序列
    doc_dicts = [{k: wordfreq_dict.get(k, 0) for k in key_merge} for wordfreq_dict in wordfreq_dicts]  # 合并的文档向量计数
    assert (doc_dicts[0].keys() == doc_dicts[1].keys()), "合并文档向量key不一致"  # 检测合并向量一致性
    return doc_dicts
