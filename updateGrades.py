import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# chrome-extension://lffljkleilfpjlmcdnoaghhcbnemelge/background.js
# /Users/taylortackett/PycharmProjects/shopify-automation/venv/chromedriver


shopify_url = "https://basis-ed.myshopify.com/admin/customers"

shopify_username = "taylor.tackett@basised.com"
shopify_password = "L57s21rq1!"


students_csv = '/Users/taylortackett/Documents/CSVS/students.csv'

# with open(students_csv, newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         # print(row)
#         # print(row['LastFirst'])

customer_email = (row['U_Students_Extension.guardian1_email'])

browser = webdriver.Chrome(executable_path='/Users/taylortackett/PycharmProjects/shopify-automation/venv/chromedriver'
                           #  , chrome_options=option
                           )


def shopify_import_grade_level():

    browser.get(shopify_url)
    username = browser.find_element_by_xpath('//*[@id="Login"]')
    username.send_keys(shopify_username)
    password = browser.find_element_by_xpath('//*[@id="Password"]')
    password.send_keys(shopify_password)
    browser.find_element_by_xpath('//*[@id="LoginSubmit"]').click()
    time.sleep(100)

    customer_input_field = browser.find_element_by_xpath('//*[@id="search-customer"]')
    customer_input_field.send_keys(customer_email)
    browser.find_element_by_xpath('//*[@id="CustomersResults"]/li/a').click()
    #updated_url = browser.get();
    #time.sleep(3)
    browser.refresh()
    time.sleep(3)
    browser.get('chrome-extension://lffljkleilfpjlmcdnoaghhcbnemelge/background.js')


    # next we want to enable our ShopifyFD extension


    browser.close()




shopify_import_grade_level()

