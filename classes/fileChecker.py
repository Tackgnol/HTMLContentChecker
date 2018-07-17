from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class fileChecker:

    def __init__(self):
        self._browser = webdriver.Chrome(
            executable_path=r"C:\Users\Adam\Documents\ChromeDriver\chromedriver.exe")

    def checkFile(self, dir):

        errors = []
        self._browser.get(dir)
        for entry in self._browser.get_log('browser'):
            errors.append(entry)

        return errors

    def kill(self):
        self._browser.close()
