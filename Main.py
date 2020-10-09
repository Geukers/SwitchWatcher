import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# BEST_BUY_NEON = "https://www.bestbuy.ca/en-ca/product/nintendo-switch-console-with-neon-red-blue-joy-con/13817625"
# BEST_BUY_GREY = "https://www.bestbuy.ca/en-ca/product/nintendo-switch-console-with-grey-joy-con/13817626"
# FREQUENCY = 5000  # Set Frequency To 2500 Hertz
# DURATION = 600000  # Set Duration To 1000 ms == 1 second
#
# if __name__ == '__main__':
#
#     driver = webdriver.Chrome("C:\\Users\\Philippe Geukers\\Downloads\\chromedriver_win32\\chromedriver.exe")
#
#     in_stock = False
#
#     best_buy_links = (BEST_BUY_NEON, BEST_BUY_GREY)
#
#     while not in_stock:
#
#         # Best Buy
#         for zelda in best_buy_links:
#             driver.get(zelda)
#             if driver.find_element_by_class_name('addToCartLabel_1eyxz')\
#                     .value_of_css_property('cursor') != 'not-allowed' \
#                     or driver.find_element_by_class_name('content_3dXxd')\
#                     .value_of_css_property('cursor') != 'not-allowed':
#                 print("Item In Stock!")
#                 winsound.Beep(FREQUENCY, DURATION)
#                 in_stock = True
#
#         if not in_stock:
#             time.sleep(60)

IPAD_URL = "https://www.apple.com/ca_edu_93120/shop/bag"
FREQUENCY = 5000  # Set Frequency To 2500 Hertz
DURATION = 600000  # Set Duration To 1000 ms == 1 second

if __name__ == '__main__':

    driver = webdriver.Chrome("C:\\Users\\Philippe Geukers\\Downloads\\chromedriver_win32\\chromedriver.exe")

    in_stock = False

    while not in_stock:
        # Best Buy
        driver.get(IPAD_URL)

        driver.find_element_by_id('select_noengraving').click()
        time.sleep(10)
        driver.find_element_by_css_selector('as-buttonlink rs-productlocator-trigger').click()

        # try:
        #     element = WebDriverWait(driver, 10).until(
        #         EC.presence_of_element_located((By.CLASS_NAME, "as-buttonlink rs-productlocator-trigger"))
        #     )
        # finally:
        #     driver.quit()
        # if driver.find_element_by_id('addToCartLabel_1eyxz')\
        #         .value_of_css_property('cursor') != 'not-allowed' \
        #         or driver.find_element_by_class_name('content_3dXxd')\
        #         .value_of_css_property('cursor') != 'not-allowed':

        #     print("Item In Stock!")
        #     winsound.Beep(FREQUENCY, DURATION)
        #     in_stock = True

        if not in_stock:
            time.sleep(60)

