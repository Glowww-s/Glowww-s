from collections import Counter


# 计算词频
def word_frequency(word_lists):
    return [Counter(word_list) for word_list in word_lists]
