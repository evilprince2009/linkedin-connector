from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


mail = "your_nice_username"
key = "your_secret_pass"
search_param = "search_term"

url = "https://www.linkedin.com"
searcher_url = "https://www.linkedin.com/search/results/people/?geoUrn=%5B%22102105699%22%2C%22101620260%22%2C%22101174742%22%2C%22105117694%22%2C%22106693272%22%2C%22103819153%22%2C%22105490917%22%2C%22100456013%22%2C%22105072130%22%2C%22102264497%22%2C%22106670623%22%2C%22104170880%22%2C%22104305776%22%2C%22101165590%22%2C%22103350119%22%2C%22101728296%22%2C%22102890719%22%2C%22101452733%22%2C%22103644278%22%5D&keywords=" + search_param + "&network=%5B%22S%22%5D&origin=FACETED_SEARCH&sid=1e7"

browser = webdriver.Edge("msedgedriver.exe")
browser.maximize_window()
browser.get(url)
time.sleep(1)

username = browser.find_element_by_xpath("//input[@name='session_key']")
password = browser.find_element_by_xpath("//input[@name='session_password']")
username.send_keys(mail)
password.send_keys(key)
submit = browser.find_element_by_xpath("//button[@type='submit']")
submit.click()
time.sleep(1)

browser.get(searcher_url)
time.sleep(2)

buttons = browser.find_elements_by_tag_name("button")
connect_buttons = [btn for btn in buttons if btn.text == "Connect"]

for btn in connect_buttons:
    browser.execute_script("arguments[0].click();", btn)
    time.sleep(1)
    send = browser.find_element_by_xpath("//button[@aria-label='Send now']")
    browser.execute_script("arguments[0].click();", send)
    dismiss = browser.find_element_by_xpath("//button[@aria-label='Dismiss']")
    browser.execute_script("arguments[0].click();", dismiss)
    time.sleep(1)
