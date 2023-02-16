from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import schedule

#personal data

my_usernumber = "840023095018"
my_password = "100702"
my_firstname = "Jan"
my_lastname = "Heimann"
my_email = "jan_heimann@icloud.com"
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser

def drachenArbeit():
    service_object_name = Service(r"/Users/janheimann/Downloads/chromedriver_mac64/chromedriver")

    # options_name = webdriver.ChromeOptions()

    driver = webdriver.Chrome(service=service_object_name)
    # to maximize the browser window
    driver.maximize_window()
    # get method to launch the URL
    driver.get(
        "https://www.bsb-muenchen.de/recherche-und-service/besuche-vor-ort/lesesaelearbeitsplaetze/allgemeiner-lesesaal/arbeitsplatz-im-allgemeinen-lesesaal-buchen/")
    # to refresh the browser
    driver.refresh()

    usernumber = driver.find_element(By.ID, "usernumber")
    for buchstabe in my_usernumber:
        time.sleep(0.1)
        usernumber.send_keys(buchstabe)

    password = driver.find_element(By.ID, "password")
    for zahl in my_password:
        time.sleep(0.1)
        password.send_keys(zahl)

    submit = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/form/input")
    submit.click()

    time.sleep(10)
    driver.refresh()

    # buchen = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div[1]/ul[5]/li[1]/div[3]/div[2]/a')
    # buchen = driver.find_element_by_class_name('js-register-button button')
    book = driver.find_element(By.LINK_TEXT, 'Buchen')
    driver.execute_script("arguments[0].click();", book)

    time.sleep(10)
    driver.refresh()

    firstname = driver.find_element(By.ID, "firstname")
    for letterI in my_firstname:
        time.sleep(0.1)
        firstname.send_keys(letterI)

    lastname = driver.find_element(By.ID, "lastname")
    for letterII in my_lastname:
        time.sleep(0.1)
        lastname.send_keys(letterII)

    email = driver.find_element(By.ID, "email")
    for letterIII in my_email:
        time.sleep(0.1)
        email.send_keys(letterIII)

    approve = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div/form/fieldset/input")
    approve.click()

    # to close the browser
    time.sleep(10)
    driver.close()


schedule.every(4).seconds.do(drachenArbeit)

while 1:
    schedule.run_pending()
    time.sleep(3)