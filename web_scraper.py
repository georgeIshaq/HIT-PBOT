from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.aliexpress.com/item/1005005599682662.html?spm=a2g0o.productlist.main.1.569451b4xtESs3&algo_pvid=470ee236-4d63-4040-9b4c-5f6cdcc7646a&utparam-url=scene%3Asearch%7Cquery_from%3A")

driver.implicitly_wait(2)

first_dropdown = driver.find_element(By.CLASS_NAME, "ship-to--menuItem--WdBDsYl")
first_dropdown.click()

language_dropdown = driver.find_element(By.XPATH, "//div[contains(span/text(), 'العربية')]")
language_dropdown.click()
dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[contains(span/text(), 'العربية')]/following-sibling::div"))
)

english_option = driver.find_element(By.XPATH, "//div[contains(text(), 'English')]")
english_option.click()

#product_description_div = driver.find_element(By.ID, "root")
save_button = driver.find_element(By.CLASS_NAME, "es--saveBtn--w8EuBuy")
save_button.click()

WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
driver.execute_script("window.scrollBy(0, 1000);")

product_description_div = driver.find_element(By.XPATH, "//div[starts-with(@class, 'description--origin-part--')]")
#print('product description div 2:', product_description_div.get_attribute('innerHTML'))

text_content = ""
image_urls = []
for paragraph in product_description_div.find_elements(By.TAG_NAME, "p"):
    # Check if the paragraph contains text within a <span>
    #print('paragraph:', paragraph.get_attribute('innerHTML'), paragraph.find_elements(By.TAG_NAME, "img"))
    try:
        #print(paragraph.find_elements(By.TAG_NAME, "img"))
        if paragraph.find_elements(By.TAG_NAME, "img"):
            # If it contains images, extract the URLs and append them to the image_urls list
            print(f'in {paragraph.find_element(By.TAG_NAME, "img").get_attribute("src")}')
            image_urls.append(paragraph.find_element(By.TAG_NAME, "img").get_attribute("src"))
            #image_urls.extend([img.get_attribute("src") for img in paragraph.find_elements_by_tag_name("img")])
        elif paragraph.find_element(By.TAG_NAME, "span"):
            # If it contains text, append it to the text_content string
            text_content += paragraph.text + " "
        
    except:
        pass
print('done')
print('content:', text_content,'\n \n', image_urls)

while True:
    pass