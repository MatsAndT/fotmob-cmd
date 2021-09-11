import xlwt

class Excel():
    line = 1
    row = 7

    def __init__(self, date):
        self.filename = f"{date}.xlsx"
        self.wb = xlwt.Workbook()
        self.sheet = self.wb.add_sheet(date)

        self.setUp()

    def setUp(self):
        self.sheet.write(0,0, "name")
        self.sheet.write(0,1, "primaryId")
        self.sheet.write(0,2, "time")
        self.sheet.write(0,3, "away")
        self.sheet.write(0,4, "away_score")
        self.sheet.write(0,5, "home")
        self.sheet.write(0,6, "home_scroe")

    def addMatches(self, name, primaryId, matche):
        self.sheet.write(self.line,0, name)
        self.sheet.write(self.line,1, primaryId)
        self.sheet.write(self.line,2, matche["time"])
        self.sheet.write(self.line,3, matche["away"]["longName"])
        self.sheet.write(self.line,4, matche["away"]["score"])
        self.sheet.write(self.line,5, matche["home"]["longName"])
        self.sheet.write(self.line,6, matche["home"]["score"])
    
    def addTitle(self, title):
        self.sheet.write(0, self.row, title)
    
    def moveRow(self):
        self.row += 1

    def addCol(self, data):
        self.sheet.write(self.line, self.row, data)
        self.row += 1

    def resetRow(self):
        self.line += 1
        self.row = 7

    def save(self):
        self.wb.save(self.filename)
