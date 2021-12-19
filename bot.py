import time
from selenium import webdriver

mail = "your_nice_username"
key = "your_secret_pass"
search_param = "search_term"
pages_upto = 5

url = "https://www.linkedin.com"
search_param = search_param.replace(" ", "%20")

browser = webdriver.Edge("msedgedriver.exe")
browser.maximize_window()
browser.get(url)
time.sleep(2)

username = browser.find_element_by_xpath("//input[@name='session_key']")
password = browser.find_element_by_xpath("//input[@name='session_password']")
username.send_keys(mail)
password.send_keys(key)
submit = browser.find_element_by_xpath("//button[@type='submit']")
submit.click()
time.sleep(2)

for page in range(1, pages_upto):
    searcher_url = f"{url}/search/results/people/?geoUrn=%5B%22103644278%22%2C%22101165590%22%2C%22101174742%22%2C%22103350119%22%2C%22104305776%22%2C%22100456013%22%2C%22101452733%22%2C%22101620260%22%2C%22101728296%22%2C%22102105699%22%2C%22102264497%22%2C%22102890719%22%2C%22103819153%22%2C%22104170880%22%2C%22105072130%22%2C%22105117694%22%2C%22105490917%22%2C%22106670623%22%2C%22106693272%22%5D&keywords={search_param}&network=%5B%22S%22%5D&origin=FACETED_SEARCH&page={page}&serviceCategory=%5B%221275%22%2C%22669%22%2C%2269%22%2C%224044%22%2C%221723%22%2C%222004%22%2C%22482%22%2C%2210048%22%2C%225255%22%2C%221836%22%2C%222174%22%2C%22899%22%2C%2249%22%2C%222269%22%2C%22123%22%2C%22115%22%5D&sid=WRy"

    browser.get(searcher_url)
    time.sleep(2)

    buttons = browser.find_elements_by_tag_name("button")
    connect_buttons = [btn for btn in buttons if btn.text == "Connect"]

    counter = 0
    for btn in connect_buttons:
        browser.execute_script("arguments[0].click();", btn)
        time.sleep(2)
        send = browser.find_element_by_xpath(
            "//button[@aria-label='Send now']")
        browser.execute_script("arguments[0].click();", send)
        dismiss = browser.find_element_by_xpath(
            "//button[@aria-label='Dismiss']")
        browser.execute_script("arguments[0].click();", dismiss)
        time.sleep(2)
        counter += 1
        if counter % 3 == 0:
            time.sleep(3)
