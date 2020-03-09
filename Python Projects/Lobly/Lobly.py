from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class Bot:
    def __init__(self,username,password):
        options =  webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome("J:\\Python Projects\\appel\\chromedriver_win32\\chromedriver.exe",options = options)        

        self.driver.get("https://www.facebook.com/")
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[1]/input").send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input").send_keys(password)        
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input").click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/form/div/div/div/div/input[2]').send_keys("Buse Tuhan")
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[24]/div/div/div[2]/div/div/div[2]/div/ul/div[1]/li/div/a").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/a").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div/div[2]/a").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[1]/div/div/div[4]/div/div[1]/div/div/div/div/div/div/div/div[2]/div[4]/div/div/div/span/div/div/div[2]/div/div/div/div").send_keys("Hey Cutie ;) Time to spam \u0021"+Keys.ENTER)
        sleep(1)

        for i in range(0,50):
            self.driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[1]/div/div/div[4]/div/div[1]/div/div/div/div/div/div/div/div[2]/div[4]/div/div/div/span/div/div/div[2]/div/div/div/div").send_keys("I lob you yaaa\u003C3"+Keys.ENTER)
            sleep(1)
            #self.driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[1]/div/div/div[4]/div/div[1]/div/div/div/div/div/div/div/div[2]/div[4]/div/div/div/span/div/div/div[2]/div/div/div/div").send_keys("I love you :D "+Keys.ENTER)
            #sleep(1)
            #self.driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[1]/div/div/div[4]/div/div[1]/div/div/div/div/div/div/div/div[2]/div[4]/div/div/div/span/div/div/div[2]/div/div/div/div").send_keys("I live you ;) "+Keys.ENTER)
            #sleep(1)
            #self.driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[1]/div/div/div[4]/div/div[1]/div/div/div/div/div/div/div/div[2]/div[4]/div/div/div/span/div/div/div[2]/div/div/div/div").send_keys("I adore you \u003C3 "+Keys.ENTER) 
            #sleep(1)
            #self.driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[1]/div/div/div[4]/div/div[1]/div/div/div/div/div/div/div/div[2]/div[4]/div/div/div/span/div/div/div[2]/div/div/div/div").send_keys("You are my entire life \u003C3 "+Keys.ENTER) 
            #sleep(1)   

            if (i%10 == 0):
                sleep(10)

        sleep(5)

Bot("housseina.ballouk.9@facebook.com","realracer334")

