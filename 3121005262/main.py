import argparse
import os
from source.keywords import extract_keywords
from source.frequency import word_frequency
from source.merge import vector_merge
from source.similar import cosine_similarity


def readfile(para):
    """
    读文件
    :param para: 命令行参数
    :return: 两个字符串的列表
    """
    with open(para.text1Path, 'r', encoding='utf-8') as f1, open(para.text2Path, 'r', encoding='utf-8') as f2:
        ts = [''.join(f1.readlines()), ''.join(f2.readlines())]  # 各合并成一条字符串
    return ts


def writefile(para):
    """
    写文件
    :param para: 命令行参数
    :return: None
    """
    with open(para.resultPath, 'w', encoding='utf-8') as f:
        f.write(format(similarity, '.3f'))


# 获取脚本路径
mainPath = os.path.dirname(__file__)
# 命令行参数
parser = argparse.ArgumentParser()
parser.add_argument("--text1Path", default=mainPath + "/tests/orig.txt",
                    help="The absolute path of the original document of the paper.")
parser.add_argument("--text2Path", default=mainPath + "/tests/orig_0.8_add.txt",
                    help="The absolute path of files in plagiarized papers.")
parser.add_argument("--resultPath", default=mainPath + "/outputs/result0.txt", help="The path of result file.")
args = parser.parse_args()

# 打开目标文件
texts = readfile(args)

# 分词预处理
word_lists = extract_keywords(texts, mainPath)

# 计算词频
wordfreq_dicts = word_frequency(word_lists)

# 合并计算文档向量
doc_vectors = vector_merge(wordfreq_dicts)

# 计算余弦相似度
similarity = cosine_similarity(doc_vectors)

# 结果写入文件
writefile(args)
