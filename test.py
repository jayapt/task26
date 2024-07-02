
# search details from imdb website
from Data import data
from Locators import locator
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class Testsubmit():

    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()

    def test_login(self, boot):
        try:

            self.wait.until(EC.presence_of_element_located((By.XPATH, locator.WebLocators().expandAllLocator))).click()
            self.wait.until(EC.presence_of_element_located((By.NAME, locator.WebLocators().nameLocator))).send_keys(data.WebData().name)
            self.wait.until(EC.presence_of_element_located((By.NAME, locator.WebLocators().fromdob))).send_keys(data.WebData().fromBirthDate)
            self.wait.until(EC.presence_of_element_located((By.NAME, locator.WebLocators().fromdob))).send_keys(data.WebData().toBirthDate)
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator.WebLocators().searchbtnLocator))).click()
            if self.wait.until(EC.presence_of_element_located((By.XPATH, locator.WebLocators().outputLocator))).is_displayed():
                print("Successfully searched")

        except NoSuchElementException as e:
            print(e)