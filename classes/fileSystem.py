
import os
import shutil


class fileSystem:

    def newDir(self, newDir):
        if not os.path.exists(newDir):
            os.makedirs(newDir)

    def newHTML(self, name, html):
        f = open('toBeJudged/' + name + '.html', 'w')
        f.write(html)
        f.close()
        return 'toBeJudged/' + name + '.html'

    def logFile(self, name, errors):
        f = open('Failed/' + name + '.txt', 'w')
        for error in errors:
            f.write(str(error) + '\n')
        f.close()

    def currentPath(self):
        return os.getcwd()

    def cutFile(self, dirFrom, dirTo):
        shutil.copy(dirFrom, dirTo)
        os.remove(dirFrom)

    def removeDirectoryRecursively(self, dir):
        shutil.rmtree(dir)
