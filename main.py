from classes.getHTML import getHTML
from classes.fileSystem import fileSystem
from classes.fileChecker import fileChecker

server = getHTML()
files = fileSystem()
checker = fileChecker()

try:
    files.removeDirectoryRecursively('Succeeded')
    files.removeDirectoryRecursively('Failed')
    files.removeDirectoryRecursively('toBeJudged')
except:
    pass
files.newDir('Succeeded')
files.newDir('Failed')
files.newDir('toBeJudged')
rows = server.connectAndGet()

for row in rows:
    fileDir = files.newHTML(row.ProductInfo, row.RichContent)
    errors = checker.checkFile(files.currentPath() + '/' + fileDir)
    if len(errors) > 0:
        files.cutFile(files.currentPath() + '/' + fileDir, 'Failed')
        files.logFile(row.ProductInfo, errors)
    else:
        files.cutFile(files.currentPath() + '/' + fileDir, 'Succeeded')

checker.kill()
print('All done')
