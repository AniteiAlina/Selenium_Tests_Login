from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


DRIVER_PATH = "/Users/tester/Desktop/chromedriver_mac64\chromedriver.exe"
URL_TO_TEST = "https://www.demo.guru99.com/V4/"
USER = "mngr504868"
PASSWORD = "zehyjyv"


class Login():
    
    def loginUtilizator(self, utilizator, parola):
        print("Incep testarea")
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(URL_TO_TEST)
        
        time.sleep(10)
        
        iframe = driver.find_element(By.ID, "gdpr-consent-notice")
        driver.switch_to.frame(iframe)
        
        acceptAll = driver.find_element(By.ID, "save")
        acceptAll.click()
        
        time.sleep(10)
        
        userName = driver.find_element(By.NAME, "uid")
        userName.send_keys(utilizator)
        
        userPassword = driver.find_element(By.NAME, "password")
        userPassword.send_keys(parola)
        
        
        loginBtn = driver.find_element(By.NAME, "btnLogin")
        time.sleep(10)
        loginBtn.click()
        time.sleep(10)
        
        test = 0
        try:
            actualTitle = driver.title
        except:
            print("Test Case PASSED")
            test = 1
            
        assert test == 1, "Test failed should not login"
            
        time.sleep(10)
        
        driver.close()
    
    def loginTest(self):
        print("Incep testarea")

        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(URL_TO_TEST)
        
        time.sleep(10)
        
        iframe = driver.find_element(By.ID, "gdpr-consent-notice")
        driver.switch_to.frame(iframe)
        
        acceptAll = driver.find_element(By.ID, "save")
        acceptAll.click()
        
        time.sleep(10)
        
        userName = driver.find_element(By.NAME, "uid")
        userName.send_keys(USER)
        
        userPassword = driver.find_element(By.NAME, "password")
        userPassword.send_keys(PASSWORD)
        
        loginBtn = driver.find_element(By.NAME, "btnLogin")
        loginBtn.click()
        
        actualTitle = driver.title
        
        assert actualTitle == "Guru99 Bank Manager HomePage", "FAILED actual title"
                
        time.sleep(10)
        
        driver.close()
        
    def loginTestUserNOK(self):
        self.loginUtilizator("userNOk", PASSWORD)
    
    def loginTestPasswordNOK(self):
        self.loginUtilizator(USER, "passwordNOK")
    
    def loginTestUserAndPasswordNOK(self):
        self.loginUtilizator("userNOK", "passwordNOK")
    
    def loginTestEmptyUser(self):
        self.loginUtilizator("", PASSWORD)
    
    def loginTestEmptyPassword(self):
        print("Incep testarea")
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(URL_TO_TEST)
        
        time.sleep(10)
        
        iframe = driver.find_element(By.ID, "gdpr-consent-notice")
        driver.switch_to.frame(iframe)
        
        acceptAll = driver.find_element(By.ID, "save")
        acceptAll.click()
        
        time.sleep(10)
        
        userName = driver.find_element(By.NAME, "uid")
        userName.send_keys(USER)
        
        userPassword = driver.find_element(By.NAME, "password")
        userPassword.send_keys("")
        
        
        loginBtn = driver.find_element(By.NAME, "btnLogin")
        loginBtn.click()
        
        time.sleep(10)
        
        find = 0
        try:
            driver.find_element(By.ID, "message18")
            find = 1
        except:
            find = 0
            
        assert find == 1, "Message Password empty not found"
                
        driver.close()
    
        
logintest = Login()
logintest.loginTest()
logintest.loginTestUserNOK()
logintest.loginTestPasswordNOK()
logintest.loginTestUserAndPasswordNOK()
logintest.loginTestEmptyUser()
logintest.loginTestEmptyPassword()