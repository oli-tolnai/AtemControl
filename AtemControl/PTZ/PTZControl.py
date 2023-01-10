from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True) # Browser stay open after the code finish

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.hitradio.hu/")
#driver.get("http://192.168.1.1/")
driver.set_window_size(1216,844)
driver.set_window_position(312,12)


from time import sleep
sleep(5)
print(driver.get_window_size())
print(driver.get_window_position())

links = driver.find_elements("xpath", "//a[@href]")


#
# for link in links:
#     if "Videók" in link.get_attribute("innerHTML"):
#         link.click()
#         break

driver.find_element(by=By.XPATH, value='/html/body/div[19]/div/div[1]/div/div/div[1]/a  ').click()

