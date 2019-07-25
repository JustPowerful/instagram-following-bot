from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

class Instabot:

    def __init__(self, username, password):

        # setting the option class
        self.options = Options()

        # driver
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=self.options)

        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.driver.get(self.base_url + '/accounts/login')
        self.login()

    def login(self):
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('//div[contains(text(), "Log In")]').click()
        time.sleep(3)
        
        try:
            self.driver.find_element_by_id('slfErrorAlert')
            print("You typed something wrong .")
        except Exception:
            print("You have logged in .")
            self.follow()

    def follow(self):
        LISTFILE = open('userlist.txt', 'r')
        for LINE in LISTFILE:
            self.driver.get(self.base_url + '/' + LINE)
            try:
                print("[+] Following .")
                self.driver.find_element_by_xpath('//button[contains(text(), "Follow")]').click()
            except Exception:
                print("[-] You already followed this person .")
            time.sleep(3)
        

        

if __name__ == '__main__':
    bot = Instabot('temuser', 'temppass')