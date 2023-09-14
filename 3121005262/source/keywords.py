import jieba


# 使用jieba进行分词
def word_cut(text):
    word_list = jieba.lcut(text)
    return word_list


# 读取停用词列表
def get_stopword_list(file):
    with open(file, 'r', encoding='utf-8') as f:
        stopword_list = [word.strip('\n') for word in f.readlines()]
    return stopword_list


# 清除停用词
def clean_stopword(word_list, stopword_list):
    result = [word for word in word_list if word not in stopword_list]
    return result


# 提取关键词
def extract_keywords(texts, main_path):
    # 分词
    cut_lists = [word_cut(text) for text in texts]
    # 读取停用词表
    stopword_list = get_stopword_list(main_path + '/hit_stopwords.txt')
    stopword_list.extend(['\n', ' '])
    # 去除停用词
    word_lists = [clean_stopword(cut_list, stopword_list) for cut_list in cut_lists]
    return word_lists
