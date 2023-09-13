import argparse
import chardet
import os


def check_charset(file_path):
    """
    用于判断文件的编码方式，从而能够正确读写文件。
    :param file_path: 文件路径
    :return: 文件编码方式
    """
    with open(file_path, "rb") as tf:
        data = tf.read(4)
        charset = chardet.detect(data)['encoding']
    return charset


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
with open(args.text1Path, 'r', encoding=check_charset(args.text1Path)) as f1, open(args.text1Path, 'r', encoding=check_charset(args.text1Path)) as f2:
    texts = [f1.readlines(), f2.readlines()]
