"""Test Caseler;

-Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
-Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
-Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
-Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
 Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class test_SauceDemo:
    
    def test_empty_login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() 
        usernameInput=driver.find_element(By.ID,"user-name")
        usernameInput.send_keys('')
        passwordInput=driver.find_element(By.ID,"password")
        passwordInput.send_keys('')
        loginButton=driver.find_element(By.ID,'login-button')
        loginButton.click()
        errorMesagge = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMesagge.text == "Epic sadface: Username is required"
        print(f"test sonucu: {testResult}")
        sleep(5)

    def test_empty_password_login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        usernameInput = driver.find_element(By.ID,'user-name')
        usernameInput.send_keys("locked_out_user")
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("")
        loginButton = driver.find_element(By.ID,'login-button')
        loginButton.click()
        errorMessage = driver. find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"test sonucu: {testResult}")
        sleep(5)

    def test_invalid_login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() 
        usernameInput=driver.find_element(By.ID,'user-name') 
        usernameInput.send_keys('locked_out_user') 
        passwordInput=driver.find_element(By.ID,'password')
        passwordInput.send_keys('secret_sauce')
        loginButton=driver.find_element(By.ID,'login-button')
        loginButton.click() 
        errorMessage=driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')
        testResult=errorMessage.text=='Epic sadface: Sorry, this user has been locked out.'
        print(f"test sonucu:{testResult}")  
        sleep(3) 

    def test_valid_login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() 
        usernameInput=driver.find_element(By.ID,'user-name')
        usernameInput.send_keys('standard_user') 
        passwordInput=driver.find_element(By.ID,'password')
        passwordInput.send_keys('secret_sauce')
        loginButton=driver.find_element(By.ID,'login-button')
        loginButton.click()
        sayfa = driver.current_url == "https://www.saucedemo.com/inventory.html"
        print(f"test sonucu(ana sayfaya geçildi mi): {sayfa}")
        urunler = driver.find_elements(By.CLASS_NAME,"inventory_item_description")
        testResult = len(urunler) == 6
        print(f"test sonucu(6 ürün listelendi mi):{testResult}")
        sleep(3)
    
    

        
        

testClass=test_SauceDemo()
#testClass.test_empty_login()
#testClass.test_empty_password_login()
#testClass.test_invalid_login()
testClass.test_valid_login()

