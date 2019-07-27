from selenium import webdriver
import time

class Instabot:

    def __init__(self, username, password):

        self.driver = webdriver.Chrome()

        # waiting period
        self.wait = 5

        # Username & Password (Don't change this)
        self.username = username
        self.password = password
        # base url
        self.base_url = 'https://www.instagram.com'

        self.driver.get(self.base_url + '/accounts/login')

        # steps (functions below)
        self.login()
        self.verify()
        self.follow()

    def login(self):
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('//div[contains(text(), "Log In")]').click()
        time.sleep(self.wait)
        
        try:
            self.driver.find_element_by_id('slfErrorAlert')
            print("You typed something wrong .")
        except Exception:
            print("You have logged in .")

    def verify(self):
        try:
            self.driver.find_element_by_xpath('//button[contains(text(), "Send Security Code")]').click()
            time.sleep(self.wait)
            print("\nYou need to verify your login !")
            self.code = input("Type your code here : ")
            self.driver.find_element_by_id('security_code').send_keys(self.code)
            self.driver.find_element_by_xpath('//button[contains(text(), "Submit")]').click()
            time.sleep(self.wait)
        except Exception:
            print("No need to verify !")

    def follow(self):
        LISTFILE = open('userlist.txt', 'r')
        for LINE in LISTFILE:
            self.driver.get(self.base_url + '/' + LINE)
            time.sleep(self.wait)
            try:
                print("[+] Following .")
                self.driver.find_element_by_xpath('//button[contains(text(), "Follow")]').click()
            except Exception:
                print("[-] You already followed this person .")
            
        

if __name__ == '__main__':
    # Change ('username' to your username, 'password' to your password)
    bot = Instabot('username', 'password')
