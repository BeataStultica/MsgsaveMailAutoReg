import os
import random
import secrets
import string
import time
import zipfile
from time import sleep
from random import choice

import requests
from faker import Faker

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from proxy_auth import manifest_json, background_js, plugin_file
from csv import writer

# 2Captcha API key here
API_2_CAPTCHA = ''


class Proxies:
    proxy_list = []
    @staticmethod
    def load_proxies(file_path: str):
        """
        Reads a text file with proxies
        :param file_path: Path to proxy file with proxies in <user>:<pas>@<ip>:<port> format each on one line
        """
        lst = []
        if file_path:
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    lst = [x for x in file.read().split('\n') if x.strip()]
            else:
                print('File: {}. Does not exist.'.format(file_path))
        Proxies.proxy_list = lst

    @staticmethod
    def get_random_proxy():
        """ Returns a random proxy """
        return choice(Proxies.proxy_list)


class AccountCreator:
    """ Class for creating msgsafe.io account
    with randomly generated details"""
    URL = 'https://www.msgsafe.io/register'
    def init(self, use_proxy: bool = False):
        self.driver = self.open_browser(use_proxy)
        self.tr = None#'https://www.msgsafe.io/confirm/email/a6f3d120-7389-449b-b586-bb8899c1dbe0'

    def create_account_ms(self):
        """
        Goes through website process of creating the account
        :return: dictionary with login information for the account
        """
        for i in range(1):
            person = self.__generate_random_details()
            print('Creating new Outlook email account')
            if self.tr:
                self.driver.get(self.tr)
            time.sleep(3)
            self.driver.get('https://www.msgsafe.io/register')
            sleep(2)
            #self.driver.find_element_by_id('firstname')
            ActionChains(self.driver) \
                .send_keys_to_element(self.driver.find_element_by_xpath(f'//input[@tabindex="1"]'), person['username']).pause(1).perform()
            ActionChains(self.driver) \
                .send_keys_to_element(self.driver.find_element_by_xpath(f'//input[@tabindex="3"]'), person['password']).pause(1).perform()
            ActionChains(self.driver) \
                .send_keys_to_element(self.driver.find_element_by_xpath(f'//input[@tabindex="4"]'), person['password']).pause(1).perform()
            while True:
                self.driver.find_element_by_class_name('z-form__captcha-refresh').click()
                time.sleep(2)
                self.driver.find_element_by_class_name('z-form__captcha-image').screenshot('captcha.png')

                data = {'key': '123'}
                file = {'file': open('captcha.png', 'rb'), 'submit': 'Upload and get the ID'} 
                r = requests.post('http://2captcha.com/in.php', data=data, files=file) 
                ref = r.text.split('|')[-1] 
                result = requests.get(f'http://2captcha.com/res.php?key=123&action=get&id={ref}') 
                res = result.text.split('|')[-1] 
                print(res)
                a = self.driver.find_element_by_xpath(f'//input[@tabindex="5"]')#self.driver.find_element_by_id('captcha')
                a.send_keys(Keys.CONTROL+'a')#.clear()
                a.send_keys(Keys.DELETE)
                time.sleep(0.2)
                ActionChains(self.driver) \
                    .send_keys_to_element(self.driver.find_element_by_xpath(f'//input[@tabindex="5"]'), res.upper()).send_keys(Keys.ENTER).pause(1).perform()
                time.sleep(1)

                try:
                    self.driver.find_element_by_class_name('z-form__captcha-image')

                except:

                    self.driver.back()
                    time.sleep(2)
                    self.driver.find_element_by_class_name('page-header__toolbar__button').click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath('//button').click()
                    time.sleep(15)
                    while True:
                        try:
                            self.driver.find_element_by_xpath('//button').click()
                            break
                        except:
                            time.sleep(3)
                    self.driver.get('https://www.msgsafe.io/esp/new')

                    ActionChains(self.driver) \
                        .send_keys_to_element(self.driver.find_element_by_xpath(f'//input[@tabindex="1"]'), person['first_name']).pause(1).perform()
                    re = self.gen_temp_mail()
                    print('end')

                    if re:
                        with open('reported2.csv', 'a', newline='\n') as f_object:
                            writer_obj = writer(f_object)
                            writer_obj.writerow([person['username'], person['password'], person['country']])
                            f_object.close()
                    self.driver.quit()
                    break
    # Generate temp email
    def gen_temp_mail(self):
        a = '''mutation {
        introduceSession
         {
             id,
             expiresAt,
             addresses
             {
              id,
              address
             }
         }
        }'''
        b = '''query
                {session(id:"%s") 
                {id, expiresAt, mails{id, fromAddr, toAddr, receivedAt, downloadUrl, toAddrOrig, decodeStatus, text, headerSubject}}}'''%("U2Vzc2lvbjr64txDN2hC6pCV7otuQ6TW")
        response = requests.post('https://dropmail.me/api/graphql/sprotyv2', json={'query':a})
        #assert response.status_code == 200
        print(response.json()) 
        i = response.json()['data']['introduceSession']['id']
        print(i)
        e =response.json()['data']['introduceSession']['addresses'][0]['address']
        ActionChains(self.driver) \
                        .send_keys_to_element(self.driver.find_element_by_xpath(f'//input[@tabindex="2"]'), e).send_keys(Keys.ENTER).pause(1).perform()
        print(e)
        sleep(5)
        b = '''query
                {session(id:"%s") 
                {id, expiresAt, mails{id, fromAddr, toAddr, receivedAt, downloadUrl, toAddrOrig, decodeStatus, text, headerSubject}}}'''%(i)
        tq = 0
        while True:
            try:
                r = requests.post('https://dropmail.me/api/graphql/sprotyv2', json={'query':b})
                tr= r.json()['data']['session']['mails'][0]['text'].split('](')[3].split(')')[0]
                print(tr)

                self.driver.get(tr)
                self.tr = tr
                return True
                break
            except:
                if tq>30:
                    return False
                    break
                sleep(3)
                tq+=3
        
    
    @staticmethod
    def __generate_random_details():
        """
        Generates random details for new account
        :return: dictionary with fake details
        """
        fake_details = Faker()
        name = fake_details.name()
        username = AccountCreator.__create_username(name)
        password = AccountCreator.__generate_password()
        first, last = name.split(' ', 1)

        while True:
            dob = fake_details.date_time()
            if dob.year < 2000:
                break
            if dob.month != 2:
                break
        while True:
            country = fake_details.country_code(representation="alpha-2")
            if country != "GB":
                break
        return {
            "first_name": first,
            'last_name': last,
            'country': country,
            'username': username,
            'password': password,
            'dob': dob
        }

    @staticmethod
    def __create_username(name: str):
        """
        Creates username based on name
        :param name: string with person name
        :return: string with username based on the name
        """
        return name.replace(' ', '').lower() + str(random.randint(1000, 10000))


    @staticmethod
    def __generate_password():
        """
        generates password 10 char long, with at least one number and symbol
        :return: string with new password
        """
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(8))
        return password + random.choice('$#@!%^') + random.choice('0123456789')

    @staticmethod
    def __open_browser(use_proxy: bool = False):
        # TODO: add user agent
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('user-data-dir=C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\User Data')
        if use_proxy:
            random_proxy = Proxies.get_random_proxy()
            # Parse Proxy
            auth, ip_port = random_proxy.split('@')
            user, pwd = auth.split(':')
            ip, port = ip_port.split(':')

            with zipfile.ZipFile(plugin_file, 'w') as zp:
                zp.writestr("manifest.json", manifest_json)
                zp.writestr("background.js", background_js % (ip, port, user, pwd))
            chrome_options.add_extension(plugin_file)

        return webdriver.Chrome(chrome_options=chrome_options)


if __name == 'main':
    # Load proxies from file
    Proxies.load_proxies('proxies.txt')
    # Initialize account creator class
    # Run account creator
    tr = 'https://www.msgsafe.io/confirm/email/ad67b453-e990-4ea6-af89-f0b5e545314e'
    while True:
        account_creator = AccountCreator()
        account_creator.tr = tr
        account_creator.create_account_ms()
        tr = account_creator.tr
