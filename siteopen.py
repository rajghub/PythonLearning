
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

delay = 5

browser = webdriver.Chrome('D:\\chromedriver')

print("Browser opened")
browser.minimize_window()
# LOGIN
def siteLogin(url, uname, pwd):
    browser.get(url)
    username = browser.find_element_by_id('j_username')
    username.send_keys(uname)
    password = browser.find_element_by_id('j_password')
    password.send_keys(pwd)
    password.send_keys(Keys.ENTER)


siteLogin('https://login.veevavault.com/auth/login',
          'girish@vv-agency.com', 'V@ult123')

# browser.get('https://login.veevavault.com/auth/login')
# username = browser.find_element_by_id('j_username')
# username.send_keys('girish@vv-agency.com')
# password = browser.find_element_by_id('j_password')
# password.send_keys('V@ult123')
# password.send_keys(Keys.ENTER)
# browser.minimize_window()
print("link opened")
# -------------

# WAIT
# while True:
#     try:  
#         myEle = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID,'headerTabContainer')))
#         # print("page is ready")
#     except TimeoutException:
#         print("Too late")

# testBtn = browser.find_element_by_link_text('Dashboards').click()
# WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,'headerTabContainer')))
# UPLOAD SECTION

browser.get('https://vv-agency-indegene.veevavault.com/ui/#inbox/upload')

print("Entered upload page")
# createBtn = browser.find_element_by_css_selector('button.vv_button.vv_button_nav.vv_inbox_new_button.inboxNewButton')
# createBtn.click()

# binder = browser.find_element_by_link_text('Upload')
# binder.click()
# -----------------

# WAIT
# WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,'inboxUploadPageContent')))
browser.implicitly_wait(delay)
docType = browser.find_element_by_xpath('//*[@id="inboxUploadPageContent"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/button')
docType.click()
# ------------------

print("Open document type")
# WAIT
# WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.ID,'uploadTypeSelect')))
# browser.implicitly_wait(delay)

uploadType = browser.find_element_by_id('uploadTypeSelect')
uploadType.click()
# -------------------


for option in uploadType.find_elements_by_tag_name('option'):
    if option.text == 'Email Fragment':
        WebDriverWait(browser, 10)
        option.click() 
        break

print("Email Fragment option selected")
# WAIT


# browser.implicitly_wait(5)
# WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.LINK_TEXT,'OK')))
browser.implicitly_wait(delay)

okBtn = browser.find_element_by_link_text('OK')
print("Click OK")
# print(okBtn.__bool__)
# WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT,'OK')))
okBtn.click()

 
# CHOOSE FILE 
# WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,'inboxFileChooserHTML5')))


chooseFile = browser.find_element_by_id('inboxFileChooserHTML5')
chooseFile.click()
browser.maximize_window()