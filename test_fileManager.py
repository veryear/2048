from unittest import TestCase
import os
import codecs
from fileManager import FileManager

class TestFileManager(TestCase):

    def test_writeFile(self):
        # given
        nowDir = os.getcwd()
        fileName = nowDir + '\\test\\testFileManager.txt'
        content = "test"

        # when
        fileManager = FileManager()
        fileManager.writeFile(fileName, content)

        # then
        f = codecs.open(fileName, 'r', encoding='utf8')
        resultContent = f.readline()
        f.close()
        self.assertEqual(resultContent, content)

        # test 후에 파일 삭제 
        # 파일 내용 실제로 보고 싶으면 주석
        os.remove(fileName)
        
    def test_readLineFile(self):
        # given
        nowDir = os.getcwd()
        fileName = nowDir + '\\test\\testFileManager.txt'
        content = "test"

        f = codecs.open(fileName, 'w', encoding='utf8')
        f.write(content)
        f.close()

        # when
        fileManager = FileManager()
        resultContent = fileManager.readLineFile(fileName)

        # then
        self.assertEqual(resultContent, content)

        # test 후에 파일 삭제
        # 파일 내용 실제로 보고 싶으면 주석
        os.remove(fileName)
