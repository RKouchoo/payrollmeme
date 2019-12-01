# tax calculator app

import csv
import os


# resident ratios
# stored as arrays for use
# -100 means 64 bit limit or 1.0E+99
# [minCap, maxCap, ratePercent, neg]
residentBracket1 = [-1, 72, 0.19, 0.19]
residentBracket2 = [72, 361, 0.2342, 3.213]
residentBracket3 = [361, 932, 0.3477, 44.2476]
residentBracket4 = [932, 1380, 0.345, 41.7311]
residentBracket5 = [1380, 3111, 0.39, 103.857]
residentBracket6 = [3111, -100, 0.47, 352.78888]


# holiday ratios
# -100 means 64 bit limit or 1.0E+99
# [minCap, maxCap, ratePercent]
holidayBracket1 = [-1, 37000, 0.15]
holidayBracket2 = [37000, 90000, 0.32]
holidayBracket3 = [90000, 180000, 0.37]
holidayBracket4 = [180000, -100, 0.45]


# CSV Path
csvPath = "import/employee-payroll-data.csv"
csvPath = os.path.join(os.path.dirname(__file__), csvPath)


class TaxCalculator:

	def calcResTax(earnt):
		afterTax = 0

		return afterTax


	def calcHoldayTax(earnt):
		afterTax = 0

		return afterTax


class csvImporter:


	def loadPayRecords(file):
		records = [] # list of lists

		with open(file) as csvFile:
			csvReader = csv.reader(csvFile, delimiter=",")

			count = 0; # so we dont add the array of titles in the csv file.
			for row in csvReader:
				if count > 1:
					records.append(PayRecord(row[0], row[1], row[2], row[3], row[4]))
					
				count += 1


		return records


	def createNewPayRecord(id, hours, rates, visa, yearToDate):
		rec = ""

		return rec


class PayRecord:
	
	global thisRecordID
	global thisHours
	global thisRates


	def __init__(self, recordID, hours, rates):
		thisRecordID = recordID
		thisHours = hours
		thisRates = rates


	def getDetails():
		details
		return details


	def getGross():
		gross
		return gross


	def getTax():
		tax
		return tax


	def getNet():
		net 
		return net
