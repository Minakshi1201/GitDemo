from selenium.webdriver.common.by import By

from utilis.browserutlits import Browser


class LoginPage(Browser):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.user_name = By.ID, "username"
        self.password = By.ID, "password"
        self.button = By.ID, "signInBtn"



    def login(self,username,password):
        self.driver.find_element(*self.user_name).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.button).click()

