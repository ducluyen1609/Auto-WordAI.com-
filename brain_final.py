import json
import  os
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class work_bot():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.action = webdriver.ActionChains(self.driver)

        with open('database.json', 'r') as file: data = json.load(file)
        self.user_database  = data['user_database']
        self.xpath_database = data['xpath_database']
        file.close()

    def process_text(self, text):
        os.system("cls")
        print(text)

    # tìm div để vượt qua xác thực
    def v_try(self, data, key):
        div_number = 0
        while True:
            condition = self.xpath_database[data][0] + str(div_number) + self.xpath_database[data][1]

            try: 
                if key != None: self.driver.find_element(by = By.XPATH, value = condition).send_keys(key)
                if key == "delete1": self.driver.find_element(by = By.XPATH, value = condition).send_keys(Keys.CONTROL, "a", Keys.DELETE)
                if key == "get_text": return (self.driver.find_element(by = By.XPATH, value = condition).get_attribute("innerHTML"), condition)+
                else: self.driver.find_element(by = By.XPATH, value = condition).click()

                if not key == "get_text": return condition
                break

            except: div_number += 1
        sleep(2)
    #tránh bot bấm linh tinh
    def click_out(self):
        sleep(2)
        self.v_try(data = "Out_Button", key = None)
        sleep(2)

    # Test File
    def test(self):
        self.driver.get(self.user_database["Test_File"])
        
    # login vào trang web
    def login(self):
        print("SignIn")
        self.driver.get(self.user_database["Url"])
        self.driver.find_element(by=By.XPATH, value = self.xpath_database["Email_Textbox"]).send_keys(self.user_database["Email"])
        sleep(2)
        self.driver.find_element(by=By.XPATH, value = self.xpath_database["Password_Textbox"]).send_keys(self.user_database["Password"], Keys.ENTER)
        sleep(5)
        Button = self.driver.find_element(by = By.XPATH, value = self.xpath_database["Close_Sign"])
        self.driver.execute_script("arguments[0].click();", Button)


    # Article_Length
    def set_article_length(self):
        print("Article Length")
        Set_Article_Length = self.v_try(data = "Article_Length", key = None) + "/option[3]"
        self.driver.find_element(by = By.XPATH, value = Set_Article_Length).click()
        self.click_out()

    # Sub Keywords
    def sub_key_words(self):
        print("Sub Keyword")
        #ramdom keyword
        self.v_try(data = "Sub_Keywords", key = "home security systems\nwyze\nblink camera\nring camera")
        self.click_out()

    # Main Keywords
    def main_key_words(self):
        print("MainKey")
        file = open("datacamera.txt", 'r')
        texts =  file.readlines()
        main_key = texts[-1]
        file.close()
        sleep(0.5)

        file = open("datacamera.txt", 'w+')
        file.writelines(texts[0:-1])
        file.close()

        self.v_try(data = "Main_Keywords", key = "delete1")
        self.v_try(data = "Main_Keywords", key = main_key)
        self.click_out()

        try:self.driver.find_element(by = By.XPATH, value = self.xpath_database["Submit"]).click()
        except: 
            Button5 = self.driver.find_element(by=By.XPATH, value=self.xpath_database["Submit"])
            self.driver.execute_script("arguments[0].click();", Button5)

    #WordAI - click button bằng js
    def word_ai(self):
        print("WordAI")
        Button1 = self.driver.find_element(by = By.XPATH, value = self.xpath_database["Word_AI"])
        Button2 = self.driver.find_element(by = By.XPATH, value = self.xpath_database["Word_AI_Setting"])

        self.driver.execute_script("arguments[0].click();", Button1)
        sleep(1)
        self.driver.execute_script("arguments[0].value='4';", Button2)

    # Click Close
    def click_close(self):
        while True:
            self.process_text(text="Click Close")
            self.main_key_words()

            while True:
                # click_text = self.v_try(data = "Find_Close", key = "get_text")
                try:
                    self.driver.find_element(by = By.XPATH, value = self.xpath_database["Close_Task"]).click()
                    try:
                        Button0 = self.driver.find_element(by=By.XPATH, value=self.xpath_database["Notice"])
                        self.driver.execute_script("arguments[0].click();", Button0)
                    except:None
                    break
                except: None
            #.get_attribute("innerHTML")
            # print(click_text)
            # while click_text[0] == "Close":
            #     print(click_text)
            #     self.driver.find_element(by = By.XPATH, value = click_text[1]).click()
            #     break

        # self.click_close()



##############################################################################################################################################################################