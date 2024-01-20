from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

class work_bot():
	def __init__(self):
		self.driver = webdriver.Chrome(ChromeDriverManager().install())
		self.action = webdriver.ActionChains(self.driver)

		self.mail = "hainammar@gmail.com"
		self.pas = "HaiN@MTelecom*2021"

		self.mail_textbox = "/html/body/div/section[2]/div/div/form/div[1]/div/div/input"
		self.pass_textbox = "/html/body/div/section[2]/div/div/form/div[2]/div/div/input"

	def login(self):
		# self.driver.get("https://af.articleforge.com/new_article")
		self.driver.get("file:///C:/Users/duclu/Desktop/python/bot/L1.html")
		#mail
		# self.driver.find_element(by=By.XPATH, value=self.mail_textbox).send_keys(self.mail)
		# sleep(2)
		# self.driver.find_element(by=By.XPATH, value=self.pass_textbox).send_keys(self.pas, Keys.ENTER)
		# sleep(10)

	def setup(self):
		op_lenght1 = "/html/body/div[2]/div[3]/form/div[1]/div/div[2]/div["
		op_lenght2 = "]/div/div/div[2]/div[1]/div/select"

		op_sub1 = "/html/body/div[2]/div[3]/form/div[1]/div/div[2]/div["
		op_sub2 = "]/div/div/div[2]/div[4]/div/textarea"

		op_ai = "/html/body/div[2]/div[3]/form/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div"

		

		#Set Before Run
		for i in range(9):
			#Lenght
			lenght = op_lenght1 + str(i) + op_lenght2
			try: 
				set_lenght = lenght + "/option[3]"
				self.driver.find_element(by=By.XPATH, value=lenght).click()
				sleep(2)
				self.driver.find_element(by=By.XPATH, value=set_lenght).click()
				sleep(1)
				self.driver.find_element(by=By.XPATH, value="/html/body").click()
			except: None
			sleep(2)

		# 	#SubKey
		# 	sub_key = op_sub1 + str(i) + op_sub2
		# 	try: 
		# 		self.driver.find_element(by=By.XPATH, value=sub_key).send_keys("home security systems\nwyze\nblink camera\nring camera")
		# 		sleep(1)
		# 		self.driver.find_element(by=By.XPATH, value="/html/body").click()
		# 	except: None
		# 	sleep(2)

			#WordAI

		# self.driver.find_element(by=By.XPATH, value=op_ai).click()
		# print("ha")

	def run (self):
		op_submit = "/html/body/div[2]/div[3]/form/div[2]/div/div/div[2]/button" # Giu nguyen ko doi	
		op_key1   = "/html/body/div[2]/div[3]/form/div[1]/div/div[2]/div["
		op_key2   = "]/div[2]/div[1]/div[1]/div[1]/input"
		#Key
		for i in range(10):

			#Set Key
			set_key = op_key1 + str(i) + op_key2
			try:
				self.driver.find_element(by=By.XPATH, value=set_key).send_keys("home security systems")
				sleep(2)
			except: None




	#clicrdk Close
	wo = self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/form/div[1]/div/div[2]/div[2]/div/div/div[1]/div/h4").get_attribute("innerHTML")			
	while word == "Close":
		self.driver.find_element(by=By.XPATH, value=).click()


		#Submit
		self.driver.find_element(by=By.XPATH, value=op_submit).click()







botngu = work_bot()
 
botngu.login()
botngu.setup()
botngu.run()