from selenium.webdriver.common.by import By

from PageObjects.Checkout_Confirmation import Checkout
from utilis.browserutlits import Browser


class ShopPage(Browser):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = By.XPATH, "//a[contains(@href,'shop')]"
        self.card_path = By.XPATH, "//div[@class='card h-100']"
        self.checkout = By.CSS_SELECTOR, "a[class*='btn-primary']"

    def shops(self,name):
        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.card_path)
        for product in products:
            Name = product.find_element(By.XPATH, "div/h4/a").text
            if Name == name:
                product.find_element(By.XPATH, "div/button").click()
    def gotocart(self):
        self.driver.find_element(*self.checkout).click()

        checkout_obj = Checkout(self.driver)
        return checkout_obj
