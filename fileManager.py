import codecs
import os
# txt 파일 한정
class FileManager:

    def writeFile(self, fileDirect, fileName, content):
        if not os.path.exists(fileDirect):
            os.makedirs(fileDirect)
        f = codecs.open(fileDirect + fileName, 'w', encoding='utf8')
        f.write(content)
        f.close()

    # 한 줄만 읽음.
    def readLineFile(self, fileDirect, fileName):
        if not os.path.exists(fileDirect):
           raise LookupError(fileDirect)
        f = codecs.open(fileDirect + fileName, 'r', encoding='utf8')
        content = f.readline()
        f.close()
        return content