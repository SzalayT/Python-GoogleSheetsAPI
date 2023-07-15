import gspread


gc = gspread.service_account(filename='creds.json')

sh = gc.open("InvestmentTracker")


