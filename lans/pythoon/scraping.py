from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


browser= webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://elzero.org")
browser.find_element_by_css_selector(".search.field").send_keys("Front-End Developer")
browser.implicitly_wait(1000)
browser.find_element_by_css_selector(".search-submit").click()
browser.find_element_by_css_selector(".all-search-post .search-post:frist-of-typs").click()
