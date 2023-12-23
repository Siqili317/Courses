from selenium import webdriver
from selenium.webdriver.common.by import By

import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(chrome_options)

#-----------Get count from wiki---------------
# driver.get('https://en.wikipedia.org/wiki/Main_Page')

# count = driver.find_element(by=By.CSS_SELECTOR, value='#articlecount a')
# print(count.text)

#------------sign up websit newsletter--------
# driver.get('http://secure-retreat-92358.herokuapp.com/')

# first_name = driver.find_element(By.NAME, value='fName')
# first_name.send_keys('Taylor')

# last_name = driver.find_element(By.NAME, value='lName')
# last_name.send_keys('Jenkins')

# email = driver.find_element(By.NAME, value='email')
# email.send_keys('my@email.com')

# sign_up = driver.find_element(By.TAG_NAME, value='button')
# sign_up.click()

# -------------------Cookies--------------------

driver.get('https://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element(by=By.ID, value='cookie')

def get_money():
    return int(driver.find_element(By.ID, 'money').text.replace(',',''))

def get_cost():
    elements = driver.find_elements(By.CSS_SELECTOR, '#store b')

    stores = []
    for n in range(8):
        store = {
            'id': f"buy{elements[n].text.split('-')[0].strip()}",
            'cost': int(elements[n].text.split('-')[-1].replace(',','').strip())
        }
        stores.append(store)

    return stores[::-1]

timeout = time.time() + 60*5
while time.time() < timeout:
    after5s = time.time() + 5
    while time.time() < after5s:
        cookie.click()
    money = get_money()
    stores = get_cost()
    print(money)
    for store in stores:
        if store['cost'] < money:
            print(store['cost'], store['id'])
            driver.find_element(By.ID, value=store['id']).click()
            break

print(driver.find_element(By.ID, value='cps').text)

driver.quit()

