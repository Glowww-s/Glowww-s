import jieba
from langdetect import detect


# 检测字符串语言
def detect_language(text):
    try:
        assert (detect(text) == 'zh-cn')
    except AssertionError:
        print('ERROR：输入文本语言错误，请检查输入文本是否为中文。')
        exit()


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
    # 检测语言
    [detect_language(text) for text in texts]
    # 分词
    cut_lists = [word_cut(text) for text in texts]
    # 读取停用词表
    stopword_list = get_stopword_list(main_path + '/source/hit_stopwords.txt')
    stopword_list.extend(['\n', ' '])
    # 去除停用词
    word_lists = [clean_stopword(cut_list, stopword_list) for cut_list in cut_lists]
    return word_lists
