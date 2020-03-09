from selenium import webdriver
from time import sleep

class Bot:
    def __init__(self,username,password):
        self.driver = webdriver.Chrome("J:\\Python Projects\\appel\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("https://www.leonard-de-vinci.net/")
        sleep(1)
        self.driver.find_element_by_xpath("//input[@name=\"login\"]").send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div[1]/form[1]/div[5]/span[2]").click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/form/div[2]/div[2]/input').send_keys(password)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/div/form/div[2]/div[4]/span").click()
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[5]/div[1]/a[12]").click()
        sleep(1)
        
        while(self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]').is_displayed()==True):
            self.driver.execute_script("location.reload()")


Bot("hussein.ballouk@edu.devinci.fr","Buse28022000\u0021")