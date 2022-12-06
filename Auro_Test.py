
import py7zr
import pandas as pd

dataBase=pd.DataFrame(columns=['bookName', 'Buy', 'Sell'])
import xml.etree.ElementTree as ET
archive = py7zr.SevenZipFile('Orders.7z', mode='r')
archive.extractall(path="")
archive.close()


tree = ET.parse('orders.xml')
root = tree.getroot()


from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)



#def addOrder(self, bookName, operation, price, volume, orderId):
	#self.bookName= bookName
	#self.operation=operation
	#self.price=price
	#self.volume=volume
	#self.orderId = orderId
#def sellOrder(self, bookName, operation, price, volume, orderId):
	#self.bookName= bookName
	#self.operation=operation
	#self.price=price
	#self.volume=volume
	#self.orderId = orderId
#def deleteOrder(self, bookName, orderId):
	#self.bookName = bookName
	#self.orderId= orderId


for child in root:
	if child.tag=='AddOrder':
		if child.attrib['operation']=='BUY':
			#addOrder(child.attrib['book'], child.attrib['price'], child.attrib['volume'], child.attrib['orderId'])
			if child.attrib['book'] not in dataBase['bookName']:
				
		elif child.attrib['operation'] == 'SELL':
			sellOrder
	break




nowNext = datetime.now()
current_time_next = nowNext.strftime("%H:%M:%S")
print("Current Time =", current_time_next)