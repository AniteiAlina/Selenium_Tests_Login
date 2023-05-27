from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Login():
    def loginTest(self):
        driver = webdriver.Chrome("/Users/tester/Desktop/chromedriver_mac64\chromedriver.exe")
        driver.get("https://www.demo.guru99.com/V4/")
        time.sleep(10)


        iframe = driver.find_element(By.ID, "gdpr-consent-notice")
        driver.switch_to.frame(iframe)

        acceptAll  =  driver.find_element(By.ID, "save")
        acceptAll.click()

    
        time.sleep(10)

        userName = driver.find_element(By.NAME, "uid")
        userName.send_keys("mngr504868")
        time.sleep(5)

        userPassword = driver.find_element(By.NAME, "password")
        userPassword.send_keys("zehyjyv")
        time.sleep(5)

        loginBtn = driver.find_element(By.NAME, "btnLogin")
        loginBtn.click()
        time.sleep(5)

        actualTitle = driver.title

        assert actualTitle == "Guru99 Bank Manager HomePage, FAIILED actual title"

      
        time.sleep(10)

        driver.close()



    def loginTestUserNOK():
        pass
    

    



        

logintest = Login()
logintest.loginTest()
#logintest.loginTestUserNOK()
#logintest.loginTestPasswordNOK()
