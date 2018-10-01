import codecs
import os
# txt 파일 한정
class FileManager:

    def writeFile(self, fileDirect, fileName, content):
        fullFileName = fileDirect + '\\' + fileName
        if not os.path.exists(fileDirect):
            os.makedirs(fileDirect)
        f = codecs.open(fullFileName, 'w', encoding='utf8')
        f.write(content)
        f.close()

    # 한 줄만 읽음.
    def readLineFile(self, fileDirect, fileName):
        fullFileName = fileDirect + '\\' + fileName
        try:
            f = codecs.open(fullFileName, 'r', encoding='utf8')
            content = f.readline()
            f.close()
        except Exception:
            raise LookupError(fullFileName)

        return content