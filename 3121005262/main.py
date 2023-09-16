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
    try:
        with open(para.text1Path, 'r', encoding='utf-8') as f1, open(para.text2Path, 'r', encoding='utf-8') as f2:
            ts = [''.join(f1.readlines()), ''.join(f2.readlines())]  # 各合并成一条字符串
        return ts
    except FileNotFoundError:
        print("ERROR: 未找到指定文件，请检查参数路径是否存在。")
    except UnicodeDecodeError:
        print("ERROR: 文件编码错误，请检查输入文件是否为txt文本文件。")
    exit()


def writefile(para, result):
    """
    写文件
    :param result: 计算得到的相似度结果
    :param para: 命令行参数
    :return: None
    """
    with open(para.resultPath, 'w', encoding='utf-8') as f:
        f.write(format(result, '.3f'))


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

# 读取目标文件
texts = readfile(args)

# 分词预处理
word_lists = extract_keywords(texts, mainPath)

# 计算词频
wordfreq_dicts = word_frequency(word_lists)

# 合并计算文档向量
doc_dicts = vector_merge(wordfreq_dicts)

# 计算余弦相似度
similarity = cosine_similarity(doc_dicts)

# 结果写入文件
writefile(args, similarity)
