import time
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

driver.get('https://www.wikipedia.de')
time.sleep(5)

search_bar = driver.find_element_by_id('txtSearch')
search_bar.send_keys('Salzburg')
search_button = driver.find_element_by_class_name('search-icon')
search_button.click()

page = driver.find_element_by_class_name('mw-body')
print(page.text)

driver.quit()
