from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://2nhaber.com/")


def Nav(navText, expected_title):
    menu_item = driver.find_element(By.XPATH, f"//a[normalize-space(text())='{navText}']")
    menu_item.click()

    actual_title = driver.find_element(By.CSS_SELECTOR, "h1.entry-title.cmsmasters-widget-title__heading").text

    if actual_title.strip().lower() == expected_title.strip().lower():
        print(f"Doğru sayfadayım: {actual_title}")
    else:
        print(f"Hatalı sayfa! Beklenen: {expected_title}, Ancak Bulunan: {actual_title}")

Nav("İş Dünyası", "İş Dünyası")

driver.quit()


