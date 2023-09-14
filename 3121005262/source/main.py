import argparse
import os
from keywords import extract_keywords
from frequency import word_frequency
from merge import vector_merge
from similar import cosine_similarity

# 获取脚本路径
mainPath = os.path.dirname(__file__)
# 命令行参数
parser = argparse.ArgumentParser()
parser.add_argument("--text1Path", default=mainPath + "/../tests/orig.txt",
                    help="The absolute path of the original document of the paper.")
parser.add_argument("--text2Path", default=mainPath + "/../tests/orig_0.8_add.txt",
                    help="The absolute path of files in plagiarized papers.")
parser.add_argument("--resultPath", default=mainPath + "/../outputs/result0.txt", help="The path of result file.")
args = parser.parse_args()

# 打开目标文件
with open(args.text1Path, 'r', encoding='utf-8') as f1, open(args.text2Path, 'r', encoding='utf-8') as f2:
    texts = [''.join(f1.readlines()), ''.join(f2.readlines())]  # 各合并成一条字符串

# 分词预处理
word_lists = extract_keywords(texts, mainPath)

# 计算词频
wordfreq_dicts = word_frequency(word_lists)

# 合并计算文档向量
doc_vectors = vector_merge(wordfreq_dicts)

# 计算余弦相似度
similarity = cosine_similarity(doc_vectors)

