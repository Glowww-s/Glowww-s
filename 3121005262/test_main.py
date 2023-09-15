import main
import unittest
import argparse
import os

mainPath = os.path.dirname(__file__)


class TestMain(unittest.TestCase):
    def test_readfile(self):
        """
        Test readfile funtion
        """
        # 命令行参数
        parser = argparse.ArgumentParser()
        parser.add_argument("--text1Path", default=mainPath + "/tests/tests_module/input1.txt",
                            help="The absolute path of the first test document of the paper.")
        parser.add_argument("--text2Path", default=mainPath + "/tests/tests_module/input2.txt",
                            help="The absolute path of the second test files in plagiarized papers.")
        args = parser.parse_args()
        result = main.readfile(args)
        self.assertEqual(result, ['这是测试文件1。', '这是测试文件2。'])

    def test_writefile(self):
        """
        Test writefile module
        """
        # 命令行参数
        parser = argparse.ArgumentParser()
        parser.add_argument("--resultPath", default=mainPath + "/tests/tests_module/output1.txt",
                            help="The path of test result file.")
        args = parser.parse_args()
        main.writefile(args, 0.9782)
        with open(mainPath + "/tests/tests_module/output1.txt") as f:  # 重新读入文件比较
            result = f.readline()
        self.assertEqual(result, '0.978')

    def test_extract_keywords(self):
        """
        Test extract keywords module
        """
        texts = ['这是测试文本1。', '这是测试文本2。']
        results = main.extract_keywords(texts, mainPath)
        # print(results)
        self.assertEqual(type(results), list)  # 检查输出类型
        self.assertEqual(len(results), 2)  # 检查输出长度
        for result in results:  # 检查输出各元素类型
            self.assertEqual(type(result), list)
            for s in result:
                self.assertEqual(type(s), str)

    def test_word_frequency(self):
        """
        Test word frequency module
        """
        texts = [['这是', '这是', '测试', '文本', '1'], ['这是', '测试', '测试', '文本', '2']]
        results = main.word_frequency(texts)
        self.assertEqual(results,
                         [{'这是': 2, '测试': 1, '文本': 1, '1': 1}, {'这是': 1, '测试': 2, '文本': 1, '2': 1}])

    def test_vector_merge(self):
        """
        Test vector merge module
        """
        texts_freq = [{'这是': 2, '测试': 1, '文本': 1, '1': 1}, {'这是': 1, '测试': 2, '文本': 1, '2': 1}]
        results = main.vector_merge(texts_freq)
        self.assertEqual(results, [{'这是': 2, '测试': 1, '文本': 1, '1': 1, '2': 0},
                                   {'这是': 1, '测试': 2, '文本': 1, '1': 0, '2': 1}])

    def test_cosine_similarity(self):
        """
        Test cosine similarity module
        """
        texts_freq_merge = [{'这是': 2, '测试': 1, '文本': 1, '1': 1, '2': 0},
                            {'这是': 1, '测试': 2, '文本': 1, '1': 0, '2': 1}]
        result = main.cosine_similarity(texts_freq_merge)
        self.assertAlmostEqual(result, 0.7142857143205898)


if __name__ == '__main__':
    unittest.main()
