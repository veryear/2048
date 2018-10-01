import codecs
# txt 파일 한정
class FileManager:

    def writeFile(self, fileName, content):
        f = codecs.open(fileName, 'w', encoding='utf8')
        f.write(content)
        f.close()

    # 한 줄만 읽음.
    def readLineFile(self, fileName):
        f = codecs.open(fileName, 'r', encoding='utf8')
        content = f.readline()
        f.close()
        return content