itemURLs = [
	"https://www.bestbuy.com/site/6439402.p?skuId=6439402",
	"https://www.bestbuy.com/site/6441172.p?skuId=6441172",
	"https://www.bestbuy.com/site/6442484.p?skuId=6442484",
	"https://www.bestbuy.com/site/6442485.p?skuId=6442485",
	"https://www.newegg.com/p/N82E16814126468"
]

#CONTACT INFO
phoneNumber = ""
email = ""

#SHIPPING INFO
firstName = ""
lastName = ""
address = ""
city = ""
state = "" #Two letters only
zipCode = ""

#BILLING INFO
cardNumber = ""
securityCode = ""
expMonth  = "" #Two numbers
expYear = "" #Four numbers

#########################

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
urlRemove = []

print("---------------------------------------------\nAIO GPU BOT v1")

while True:
	for url in itemURLs:
		if url not in urlRemove:
			print("---------------------------------------------\nItem link: " + url)
			driver.get(url)

			if "newegg.com" in url:
				WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[10]/header/div[1]/div[3]/div[1]/form/div/div[1]/input'))) #wait for search bar on new page
				
				itemName = driver.find_element_by_xpath('/html/body/div[10]/div[2]/div[1]/div/div/div[2]/div[1]/div[5]/h1').text
				print("Item name: " + itemName + "\n")

				if len(driver.find_elements_by_xpath('//button[text()="Add to cart "]')) > 0:
					print("Item in stock")

					if len(driver.find_elements_by_xpath('/html/body/div[10]/div[4]/div[1]/div/a')) > 0: #popup killer
						driver.find_element_by_xpath('/html/body/div[10]/div[4]/div[1]/div/a').click()
						
					driver.find_element_by_xpath('//button[text()="Add to cart "]').click() #add to cart

					inCart = False
					while inCart == False:
						time.sleep(.1)
						if len(driver.find_elements_by_xpath('/html/body/div[10]/div[2]/div[2]/div/div/div[2]/div[2]/button[2]')) > 0 or len(driver.find_elements_by_xpath('/html/body/div[10]/div[2]/div[2]/div/div/div/div[3]/button[1]')) > 0:
							inCart = True
					print("Item in cart")

					driver.get("https://secure.newegg.com/shop/cart") #go to cart page
					WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[8]/div[1]/section/div/div/form/div[2]/div[3]/div/div/div[3]/div/button'))) #wait for checkout button
					
					if len(driver.find_elements_by_xpath('/html/body/div[8]/div[1]/div/div/div/div[1]/button/span/i')) > 0: #popup killer
						driver.find_element_by_xpath('/html/body/div[8]/div[1]/div/div/div/div[1]/button/span/i').click()

					driver.find_element_by_xpath('/html/body/div[8]/div[1]/section/div/div/form/div[2]/div[3]/div/div/div[3]/div/button').click() #checkout

					WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div[2]/div/div/div[1]/form[2]/div[2]/div/button'))) #wait for checkout as guest button
					driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div/div[1]/form[2]/div[2]/div/button').click() #continue as guest

					WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/section/div/div/form/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div'))) #wait for new address button
					driver.find_element_by_xpath('/html/body/div[6]/div/section/div/div/form/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div').click() #click new address button
					WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div/div/div/div[3]/button[2]'))) #wait for form to load
					driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/div[2]/form/div[2]/div[1]/input').send_keys(firstName)
					driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/div[2]/form/div[2]/div[2]/input').send_keys(lastName)
					driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/div[2]/form/div[2]/div[6]/input').send_keys(address)
					driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/div[2]/form/div[2]/div[8]/input').send_keys(city)
					driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/div[2]/form/div[2]/div[9]/label[2]/select/option[value()="' + state + '"]').click() #make dictionary if this doesnt work of state to abreviation
					driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/div[2]/form/div[2]/div[10]/input').send_keys(zipCode)
					driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/div[2]/form/div[2]/div[15]/input').send_keys(email)
					driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/div[2]/form/div[2]/div[12]/input').send_keys(phoneNumber)
					driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/div[3]/button[2]').click() #save shipping info

					if len(driver.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/div/label')) > 0: #error with address
						driver.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/div/label').click() #keep inputted
						driver.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/div[3]/button[2]').click() #submit
				
					driver.find_element_by_xpath('/html/body/div[6]/div/section/div/div/form/div[2]/div[1]/div[2]/div[1]/div/div[3]/button').click() #continue to courier info
					print("Shipping information submitted")

					WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/section/div/div/form/div[2]/div[1]/div[2]/div[2]/div/div[3]/button')))
					driver.find_element_by_xpath('/html/body/div[6]/div/section/div/div/form/div[2]/div[1]/div[2]/div[2]/div/div[3]/button').click() #continue to payment info

					WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/section/div/div/form/div[2]/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/div[3]/div/div'))) #wait for new card button
					driver.find_element_by_xpath('/html/body/div[6]/div/section/div/div/form/div[2]/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/div[3]/div/div').click() #click new address button
					WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div[3]/button[2]'))) #wait for form to load
					driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[1]/div[1]/input').send_keys(firstName + " " + lastName) #cardholder name
					driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[1]/div[2]/input').send_keys(cardNumber)
					driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[1]/div[4]/label[2]/select/option[text()="' + expMonth + '"]').click()
					driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[1]/div[5]/label/select/option[text()="' + expYear + '"]').click()
					driver.find_element_by_xpath('/html/body/div[6]/div/div[3]/button[2]').click() #submit
					print("Billing information submitted")
					WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/section/div/div/form/div[2]/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div/label/div[4]/input'))) #wait for ccv form
					driver.find_element_by_xpath('/html/body/div[6]/div/section/div/div/form/div[2]/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div/label/div[4]/input').send_keys(securityCode)
					driver.find_element_by_xpath('/html/body/div[6]/div/section/div/div/form/div[2]/div[1]/div[2]/div[3]/div/div[3]/button').click() #review your order

					WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/section/div/div/form/div[2]/div[3]/div/div/div[4]/div/button'))) #wait for purchase button
					driver.find_element_by_xpath('/html/body/div[6]/div/section/div/div/form/div[2]/div[3]/div/div/div[4]/div/button').click() #complete order
					#add line here for making sure purchase went through on confirmation page
					print("Succesfully purchased!")
					quit()

				else:
					print("Item out of stock, loading next page...")

			elif "bestbuy.com" in url:
				WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/header/div[2]/div[1]/div/div[2]/div/div[1]/div/div/form/input[1]'))) #wait for searchbar on new page

				itemName = driver.find_element_by_xpath('/html/body/div[3]/main/div[2]/div[3]/div[1]/div[1]/div/div/div[1]/h1').text
				print("Item name: " + itemName + "\n")

				if len(driver.find_elements_by_xpath('//button[text()="Add to Cart"]')) > 0:
					print("Item in stock") 
					driver.find_element_by_xpath('//button[text()="Add to Cart"]').click() #add to cart

					inCart = False
					while inCart == False:
						time.sleep(.1)
						if len(driver.find_elements_by_xpath('/html/body/div[2]/div/div/header/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/a/div')) > 0 or len(driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div/div/div/header/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/a/div')) > 0:
							inCart = True

					print("Item in cart")

					driver.get("https://www.bestbuy.com/cart") #go to cart page
					WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div[2]/div[1]/div/div/span/div/div[2]/div[1]/section[2]/div/div/div[3]/div/div[1]/button'))) #wait for checkout button
					driver.find_element_by_xpath('/html/body/div[1]/main/div/div[2]/div[1]/div/div/span/div/div[2]/div[1]/section[2]/div/div/div[3]/div/div[1]/button').click() #checkout

					WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/section/main/div[4]/div/div[2]/button'))) #wait for checkout as guest button
					driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[4]/div/div[2]/button').click() #continue as guest

					WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button'))) #wait for payment button
					driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[1]/label/div/input').send_keys(firstName)
					driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[2]/label/div/input').send_keys(lastName)
					driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[3]/label/div[2]/div/div/input').send_keys(address)
					driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[5]/div/div[1]/label/div/input').send_keys(city)
					driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[5]/div/div[2]/label/div/div/select/option[text()="' + state + '"]').click()
					driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[6]/div/div[1]/label/div/input').send_keys(zipCode)
					driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/section/div[2]/label/div/input').send_keys(email)
					driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/section/div[3]/label/div/input').send_keys(phoneNumber)

					driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button').click() #continue to payment info
					print("Shipping information submitted")

					WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[3]/button'))) #wait for place order button
					driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div/section/div[1]/div/input').send_keys(cardNumber)
					driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div/section/div[2]/div[1]/div/div[1]/label/div/div/select/option[text()="' + expMonth + '"]').click()
					driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div/section/div[2]/div[1]/div/div[2]/label/div/div/select/option[text()="' + expYear + '"]').click()
					driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div/section/div[2]/div[2]/div/div[2]/div/input').send_keys(securityCode)
					driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[4]/button').click() #Place order
					print("Billing information submitted")
					#add line here for making sure purchase went through on confirmation page
					print("Succesfully purchased!")
					quit()

				else:
					print("Item out of stock, loading next page...")

			else:
				print("\nUnsupported site, removing from list")
				urlRemove.insert(0, url)