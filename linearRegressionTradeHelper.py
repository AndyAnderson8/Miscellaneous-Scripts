from datetime import date
import time
import numpy as np
import requests
import time
import math

minimumValue = 0
maximumValue = 91000
minimumDemand = 2

def standardizeDay(date): #yyyy-mm-dd
  return (int(date[0:4]) * 365) + (int(date[5:7]) * 30) + int(date[8:10])

def getStandardizedDate():
  day = date.today()
  day = day.strftime("%YY-%m-%d")
  return standardizeDay(day)

def underlinePrint(string):
  length = len(string)
  underline = ""
  while length > 1:
    underline += "—"
    length -= 1
  print(string)
  print(underline)

def standardizeNumber(individual, total):
  totalCharacterCount = len(str(total))
  individualCharacterCount = len(str(individual))
  difference = totalCharacterCount - individualCharacterCount
  string = ""
  while difference > 0:
    string += "0"
    difference -= 1
  string += str(individual)
  return string
  
def fetchRolimonsData():
  response = requests.get("https://www.rolimons.com/itemapi/itemdetails")
  return response.json()["items"]

def fetchSalesData(assetID):
  response = requests.get("https://economy.roblox.com/v1/assets/" + assetID + "/resale-data")
  data = response.json()
  rawSalesData = list(data.items())[5][1]
  if len(rawSalesData) > 0:
    parsedSalesData = []
    for sale in rawSalesData:
      price = sale["value"]
      date = sale["date"]
      day = standardizeDay(date)
      parsedSalesData.append([day, price])
    averagedSalesData = []
    previousDay = parsedSalesData[0][0]
    totalSalesCount = 0
    totalPriceSum = 0
    for sale in parsedSalesData:
      if sale[0] != previousDay:
        averageSalePrice = totalPriceSum / totalSalesCount
        averagedSalesData.append([previousDay, averageSalePrice])
        previousDay = sale[0]
        totalSalesCount = 1
        totalPriceSum = sale[1]
      else:
        totalSalesCount += 1
        totalPriceSum += sale[1]
    return averagedSalesData
  return -1

def linearRegression(dataArray):
  x = []
  y = []
  for element in dataArray:
    x.append(element[0])
    y.append(element[1])
  x = np.array(x)
  y = np.array(y)
  n = np.size(x)
  m_x = np.mean(x)
  m_y = np.mean(y)
  ss_xy = np.sum(y*x) - n*m_y*m_x
  ss_xx = np.sum(x*x) - n*m_x*m_x
  b_1 = ss_xy / ss_xx
  b_0 = m_y - b_1*m_x
  return [b_0, b_1]

def parseData(assetID, minimumValue, maximumValue, minimumDemand):
  assetID = str(assetID)
  itemRolimonsData = rolimonsData[assetID]
  name = itemRolimonsData[0]
  symbol = itemRolimonsData[1]
  if symbol != "":
    symbol = " (" + symbol + ")"
  rap = itemRolimonsData[2]
  value = itemRolimonsData[4]
  demand = itemRolimonsData[5] #ranked 4 (best) to 0 (worst), also -1 for no data
  #see if theres one for proof based vs rap based cause I only wanna use rap based
  if value >= minimumValue and value <= maximumValue and demand >= minimumDemand:
    itemSalesData = fetchSalesData(assetID)
    equation = linearRegression(itemSalesData)
    expectedRap = equation[1] * getStandardizedDate() + equation[0]
    expectedValue = math.floor(1.28 * expectedRap)
    difference = math.floor(value - expectedValue)
    percentage = math.floor((100 * value) / expectedValue) - 100
    return [assetID, name, symbol, rap, value, demand, expectedValue, difference, percentage]
  return [assetID, name, symbol, rap, value, demand, -1, -1, -1]

def run():
  rolimonsData = fetchRolimonsData()
  assetIDs = list(rolimonsData.keys())
  fullData = []
  itemCount = len(assetIDs)
  count = 0
  underlinePrint("\nAssembling data for " + str(itemCount) + " limiteds...")
  for assetID in assetIDs:
    count += 1
    itemData = parseData(assetID, minimumValue, maximumValue, minimumDemand)
    if itemData[8] != -1:
      print("(" + standardizeNumber(count, itemCount) + "/" + str(itemCount) + ") - Assembled data for " + itemData[1] + itemData[2] + "...")
      fullData.append(itemData)
      time.sleep(1.5)
  fullData.sort(key = lambda x:x[8], reverse = True)
  for item in fullData:
    print("\n(ID: " + str(item[0]) + ") " + item[1] + item[2])
    #print("RAP: " + str(item[3]) + " R$")
    print("Value: " + str(item[4]) + " R$")
    print("Expected Value: " + str(item[6]) + " R$")
    print("Mean Value Difference: " + str(item[7]) + " R$ (" + str(item[8]) + "%)")
  
while True:
  run()
  time.sleep(180)