from lazada import *
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
# options.add_argument('--headless') 
options.add_argument('start-maximized') 
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
browser = webdriver.Chrome(options=options)

browser.get("file:///Users/houman/Desktop/Productify/captcha.html")
# browser.switch_to_frame(browser.find_element_by_id("nc_2_wrapper"))
source = browser.find_element_by_id("nc_2_n1z")
move = ActionChains(browser)
move.click_and_hold(source).move_by_offset(400, 0).release().perform()

# browser.quit()
