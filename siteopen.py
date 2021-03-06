
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Data collection
delay = 5
uploadfilename = "D:\Learning\Python\PythonLearning\BOTOX_ONERegistrationQuickLookGuide.html"
sesName = "Test Session name"
sesTitle = "Test Session title"
sesType = "Email Fragment"
sesCountry = "India"
sesProduct = "Test Session Product"



browser = webdriver.Chrome('D:\\chromedriver')
print("Browser opened")
browser.maximize_window()
# LOGIN FUNCTION
def siteLogin(url, uname, pwd):
    browser.get(url)
    username = browser.find_element_by_id('j_username')
    username.send_keys(uname)
    password = browser.find_element_by_id('j_password')
    password.send_keys(pwd)
    password.send_keys(Keys.ENTER)


siteLogin('https://login.veevavault.com/auth/login',
          'girish@vv-agency.com', 'V@ult123')

print("Loged in")
# -------------

# UPLOAD SECTION

browser.get('https://vv-agency-indegene.veevavault.com/ui/#inbox/upload')

print("Entered upload page")

# WAIT
browser.implicitly_wait(delay)

def chooseFileFunc():
    
    try:
        chooseFile = browser.find_element_by_id('inboxFileChooserHTML5')
        chooseFile.send_keys(uploadfilename)
        # chooseFile.click()
        
        print("Successful")
    except Exception as axp:
        print("Click ok Again")
        # clickOkBtn()
        chooseFileFunc()


def clickOkBtn():
    try:
        okBtn = browser.find_element_by_link_text('OK')
        okBtn.click()
        okBtn.send_keys(Keys.ENTER )
        self.send_keys(Keys.ENTER)
        print("Able to find the element")
    except Exception as axp:
        print("unable to find OK BUTTON")
        

def clicknextBtn():
    try:
        nextBtn = browser.find_element_by_id('inboxUploadNext')
        nextBtn.click()
        # nextBtn.send_keys(Keys.ENTER )
        print("Able to find NEXT BUTTON")
        clicknextBtn()
        
    except Exception as axp:
        print("unable to find NEXT BUTTON")
        # clicknextBtn()        


def clicksaveBtn():
    try:
        saveBtn = browser.find_element_by_id('inboxUploadSave')
        saveBtn.click()
        print('Save clicked')
    except Exception as axpn:
        print("Unable to click save")
        clicknextBtn()

# uploadType = browser.find_element_by_id('uploadTypeSelect')
# uploadType.click()        
chooseFileFunc()

# Click document type section
docType = browser.find_element_by_xpath(
    '//*[@id="inboxUploadPageContent"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/button')
docType.click()
# ------------------

print("Open document type")
# WAIT


uploadType = browser.find_element_by_id('uploadTypeSelect')
uploadType.click()
# -------------------

# WAIT

# Click ok button function
browser.implicitly_wait(delay)
for option in uploadType.find_elements_by_tag_name('option'):
    if option.text == sesType:
        WebDriverWait(browser, 10)
        option.click() 
        WebDriverWait(browser, 10)
        break
print("Email Fragment option selected")

clickOkBtn()
clickOkBtn()
browser.implicitly_wait(delay)
clicknextBtn()
# clicknextBtn()



browser.implicitly_wait(delay)

eleName=browser.find_element_by_name('name')
eleName.clear()
eleName.send_keys(sesName)
eleTitle=browser.find_element_by_name('title')
eleTitle.send_keys(sesTitle)
eleCountry=browser.find_element_by_name('country_b')
print('ATTRIBUTE: ',eleCountry.get_attribute)

eleCountry.send_keys(sesCountry)
eleCountry.click()