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

residentList = [residentBracket1, residentBracket2, residentBracket3, residentBracket4, residentBracket5, residentBracket6]

# holiday ratios
# -100 means 64 bit limit or 1.0E+99
# [minCap, maxCap, ratePercent]
holidayBracket1 = [-1, 37000, 0.15]
holidayBracket2 = [37000, 90000, 0.32]
holidayBracket3 = [90000, 180000, 0.37]
holidayBracket4 = [180000, -100, 0.45]

holidayList = [holidayBracket1, holidayBracket2, holidayBracket3, holidayBracket4]


# CSV Path
csvPath = "import/employee-payroll-data.csv"
csvPath = os.path.join(os.path.dirname(__file__), csvPath)


printToConsole = True # turn on and off consold printing


class TaxCalculator:


	# takes a pay record and then runs the correct method for tax to be calculated
	def runTaxCheck(records):
		earnt = 0

		worker = 0 # the amount of workers that are present in the CSV file, set a few lines down 
		lastWorker = 0

		workerShifts = [] # a list of lists relating to the workers in order of "worker 1", 2, 3, 4 etc
 		workerInternationalShifts = [] # same list but for international workers

		for record in records:
			records[0].getRecord() = lastWorker

			if worker != lastWorker and lastWorker > worker:
				worker = lastWorker


		workerCount = 1
		temp = []
		iTemp = [] # temp for both types of workers

		while workerCount <= worker: # create a nested list of the worker's jobs and their ID's
			for record in records:
				if record.getRecord() == workerCount:
					if record.getVisa > 0:
						iTemp.append(records)
					else:
						temp.append(record)


			workerInternationalShifts.append(iTemp)		
			workerShifts.append(iTemp)
			temp = []
			iTemp = []

			workerCount += 1 

		# finally after sorting and splitting we calculate net income
		resTaxes = calcResTax(workerShifts)
		holidayTaxes = calcHoldayTax(workerInternationalShifts)

		# now we prepare the data for csv and to be potentially be printed to the console.
		# creates a console sting as well as csv data 

		dosomethingwithdatahere


	def calcResTax(residentList):
		afterTax = 0
		residentNetShifts = []

		for resident in residentList:
			for shift in resident:
				


		return residentNetShifts


	def calcHoldayTax(holidayList):
		afterTax = 0



		return afterTax


	def taxBracketExtrapolator(bracket)
		return [bracket[0], bracket[1]]



class csvImporter:


	def loadPayRecords(file):
		records = [] # list of lists

		with open(file) as csvFile:
			csvReader = csv.reader(csvFile, delimiter=",")

			count = 0; # so we dont add the array of titles in the csv file.
			for row in csvReader:

				if count >= 1:
					records.append(createNewPayRecord(row[0], row[1], row[2], row[3], row[4]))
				count += 1

		return records


	def createNewPayRecord(id, hours, rates, visa, yearToDate):
		international = False
		
		if visa > 0:
			international = True

		return PayRecord(self, id, hours, rates, visa, yearToDate, international)



class csvWriter:

	def writeToCSV(path, writeToConsole):



class PayRecord:
	
	global thisRecordID
	global thisHours
	global thisRates
	global thisVisa
	global thisYearToDate
	global thisInternational


	def __init__(self, recordID, hours, rates, visa, yearToDate, international):
		thisRecordID = recordID
		thisHours = hours
		thisRates = rates
		thisVisa = visa
		thisYearToDate = yearToDate
		thisInternational = international


	def calculateSingleGross():
		return getHours() * getRate()


	def getRecord():
		return thisRecordID


	def getHours():
		return thisHours


	def getRate():
		return thisRates


	def getVisa():
		return thisVisa


	def getYearToDate():
		return thisYearToDate


	def getInternational():
		return international




# main thread

