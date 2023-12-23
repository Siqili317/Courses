from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

whole_price = driver.find_element(by=By.CLASS_NAME, value='a-price-whole')
fraction_price = driver.find_element(by=By.CLASS_NAME, value='a-price-fraction')

print(f"The price on Amazon is {whole_price.text}.{fraction_price.text}")

# # Close one tab
# driver.close()

# # Close browser
driver.quit()