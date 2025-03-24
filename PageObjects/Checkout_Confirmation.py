from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilis.browserutlits import Browser


class Checkout(Browser):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.sucess_button = By.XPATH, "//button[@class='btn btn-success']"
        self.country = By.ID, "country"
        self.country_option = By.LINK_TEXT, "India"
        self.checkbox = By.XPATH, "//div[@class = 'checkbox checkbox-primary']"
        self.submit = By.CSS_SELECTOR, "input[type='submit']"
        self.success_msg = By.CLASS_NAME, "alert-success"

    def checkout(self):
        self.driver.find_element(*self.sucess_button).click()


    def confiramation(self,country):
        self. driver.find_element(*self.country).send_keys(country)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self. driver.find_element(*self.country_option).click()

        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit).click()

    def validation(self):
        success = self. driver.find_element(*self.success_msg).text
        assert 'Success! Thank you!' in success


