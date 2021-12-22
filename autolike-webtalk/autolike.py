#importing libraries
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.common.exceptions import ElementClickInterceptedException

#initialisong varaibles 
PATH = 'C:\\Users\hussa\\Desktop\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

#NAVIGATING ANF LOGGING IN

#navigating
driver.get("https://www.webtalk.co/")

#login
link = driver.find_element_by_link_text("Login")
link.click()

time.sleep(1)

username_textbox = driver.find_element_by_name("userName")
username_textbox.send_keys("<yourmail@email.com>")

password_textbox = driver.find_element_by_name("password")
password_textbox.send_keys("<password>")

time.sleep(1)

logging = driver.find_element_by_id("signInSubmit")
logging.click()

time.sleep(1)

#initializing the profile link text in a variable

text = '''

\\list\\

'''




#filtering list of usernmae from text
exceptions = []
profiles = []
def filter(numloc):
    loc = text.find("https://www.webtalk.co/",numloc)
    end = text.find('\n' or '/news',loc)
    username = text[loc+len("https://www.webtalk.co/"):end]
    if '/news' in username:
        username=username[:username.find('/news')]
    profiles.append(username)


for a in range (1,53):
    if len(str(a))==1:
        numloc = text.find("0"+str(a)+".")
        filter(numloc)
    elif len(str(a))==2:
        numloc = text.find(str(a)+".")
        filter(numloc)




print (profiles)

#naviagting to the profile

for users in profiles:
    time.sleep(1)
    driver.get("https://www.webtalk.co/"+str(users)+"/news")
    time.sleep(3)

    #scrolling and finding elements which are not already liked
    driver.execute_script("window.scrollBy(0,8000)","")
    time.sleep(3)

    like = driver.find_elements_by_xpath('//*[contains(@id, "3")]/div[5]/div/div/ul/li[@class="liked-desk like-border-right"]')
    driver.execute_script("scrollBy(0,-8000);")
    time.sleep(2)

    #checking if the element list is empty
    if len(like) != 0:
        #scrolling and clicking elements

        for i in like:


            driver.execute_script("arguments[0].scrollIntoView();",i)
            time.sleep(1)
            driver.execute_script("scrollBy(0,-80);")
            time.sleep(1)
            try:
                i.click()
            except ElementClickInterceptedException:
                exceptions.append(i)

        if len(exceptions) !=0:

            driver.execute_script("scrollBy(0,-8000);")
            for ele in exceptions:
                driver.execute_script("arguments[0].scrollIntoView();",ele)
                time.sleep(1)
                driver.execute_script("scrollBy(0,-80);")
                time.sleep(1)
                ele.click()

            exceptions = []


    
    time.sleep(1)
