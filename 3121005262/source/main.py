import argparse

# 命令行参数
parser = argparse.ArgumentParser()
parser.add_argument("--text1Path", default="../tests/orig.txt", help="The absolute path of the original document of the paper.")
parser.add_argument("--text2Path", default="../tests/orig_0.8_add.txt", help="The absolute path of files in plagiarized papers.")
parser.add_argument("--resultPath", default="../outputs/result0.txt", help="The path of result file.")
args = parser.parse_args()

print(args.text1Path)
print(args.text2Path)
print(args.resultPath)