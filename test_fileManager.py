from unittest import TestCase
import os
import codecs
from fileManager import FileManager


class TestFileManager(TestCase):

    def test_writeFile(self):
        # given
        nowDir = os.getcwd() + '\\test'
        fileName = 'testFileManager.txt'
        fullFileName = nowDir + '\\' + fileName
        content = "test"

        # when
        fileManager = FileManager()
        fileManager.writeFile(nowDir, fileName, content)

        # then
        f = codecs.open(fullFileName, 'r', encoding='utf8')
        resultContent = f.readline()
        f.close()
        self.assertEqual(resultContent, content)

        # test 후에 파일 삭제 
        # 파일 내용 실제로 보고 싶으면 주석
        print(fullFileName)
        os.remove(fullFileName)

    def test_readLineFile(self):
        # given
        fileDirect = os.getcwd() + '\\test'
        fileName = 'testFileManager.txt'
        fullFileName = fileDirect + '\\' + fileName
        content = "test"

        if not os.path.exists(fileDirect):
            os.makedirs(fileDirect)
        f = codecs.open(fullFileName, 'w', encoding='utf8')
        f.write(content)
        f.close()

        # when
        fileManager = FileManager()
        resultContent = fileManager.readLineFile(fileDirect, fileName)

        # then
        self.assertEqual(resultContent, content)

        # test 후에 파일 삭제
        # 파일 내용 실제로 보고 싶으면 주석
        os.remove(fullFileName)
