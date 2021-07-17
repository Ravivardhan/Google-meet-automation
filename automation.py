#https://meet.google.com/xaa-xboq-mqt
from datetime import datetime
# import required modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

meetings=[["09:20","https://meet.google.com/dcu-adqm-yds","10:10"],
		  ["10:10","https://meet.google.com/mev-sbax-uqp","11:10"],
			["11:10","https://meet.google.com/bka-bxfc-gvx","12:10"]
		  ]

# create chrome instamce
opt=Options()
opt.add_experimental_option("debuggerAddress","localhost:8989")
driver=webdriver.Chrome(executable_path="D:\\API\\chromedriver.exe",chrome_options=opt)


# go to google meet
def join_meeting(link):
	driver.get(link)
	time.sleep(3)

	try:
		dismiss=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span')))
		driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span').click()
	except ConnectionError as c:
		print(c)
	#driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span').click()
	try:
		dismiss=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span')))
		driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span').click()
	except ConnectionError as c:
		print(c)
def end_meeting():
	#driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[9]/div[2]/div[2]/div').click()
	try:
		dismiss=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[9]/div[2]/div[2]/div')))
		driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[9]/div[2]/div[2]/div').click()
	except ConnectionError as c:
		print(c)
join=True

while join:

	for i in meetings:
		now = datetime.now()

		current_time = now.strftime("%H:%M")
		if i[0]==current_time:
			join_meeting(i[1])

			end=True
			while end:
				now = datetime.now()

				current_time = now.strftime("%H:%M")
				if current_time==i[2]:
					end_meeting()
					end=False


















'''while join:
	now = datetime.now()

	current_time = now.strftime("%H:%M")

	if current_time==meetings[0]:

		join_meeting(str(meetings[1]))
		time.sleep(5)
		end=True
		while end:
			now=datetime.now()
			current_time=now.strftime("%H:%M")
			if current_time==meetings[2]:
				end_meeting()
				end=False

		join=False
'''