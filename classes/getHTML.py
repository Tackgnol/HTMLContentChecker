import pyodbc


class getHTML:

    def __init__(self):
        self._server = 'localhost'
        self._database = 'test'
        self._username = 'Adam'
        self._password = 'XXXXX'

    def connectAndGet(self):
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='
                              + self._server
                              + ';DATABASE='
                              + self._database
                              + ';UID='
                              + self._username
                              + ';PWD='
                              + self._password)
        cursor = cnxn.cursor()
        return cursor.execute("SELECT * FROM dbo.RC")
