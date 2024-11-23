from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://2nhaber.com/")

# Arama ikonunun tıklanabilir olduğundan emin olalım
search_icon = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div.elementor-widget-cmsmasters-search__popup-trigger-container span.elementor-widget-cmsmasters-search__popup-trigger-inner-icon"))
)


search_icon.click()

search_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Keşfet...']"))
)
search_input.send_keys("İstanbul")

search_input.send_keys(Keys.RETURN)
