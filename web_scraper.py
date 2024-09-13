from selenium import webdriver
from lxml import html
from time import sleep

def get_prod_title_desc(url):
    """
    Given an aliexpress product URL, this function will scrape the product title and description

    RETURNS
    title: str - the product title
    parsed_desc: str - the product description
    """
    driver = webdriver.Chrome()
    driver.get(url)
    sleep(2)

    SCROLL_PAUSE_TIME = 4  # Adjust based on how fast the page loads

    # Get the initial scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down by 3000 pixels
        driver.execute_script("window.scrollBy(0, 3000);")

        # Wait to load more content
        sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height after scrolling
        new_height = driver.execute_script("return document.body.scrollHeight")
        print(last_height, new_height)
        # Break the loop if no new content has loaded (i.e., scroll height hasn't changed)
        if new_height == last_height:
            break

        # Update the last height to the new height
        last_height = new_height

    tree = html.fromstring(driver.page_source)

    #get the title and description
    title = tree.xpath("//div[contains(@class, 'title--wrap')]")[0].text_content()
    desc = tree.xpath("//div[contains(@id, 'product-description')]")
    parsed_desc = ""

    #parse the description into one string
    for child in desc[0]:
        parsed_desc += child.text_content().strip() + "\n"

    driver.quit()
    return title, parsed_desc

print(get_prod_title_desc('https://vi.aliexpress.com/item/1005005707583364.html'))