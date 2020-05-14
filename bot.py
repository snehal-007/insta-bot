#author-Snehal Bhoya

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(path)


# Login Insta
def login(usr,pss):
    driver.get("https://www.instagram.com/")
    time.sleep(2)

    usr_ent = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
    usr_ent.clear()
    usr_ent.send_keys(usr)
    time.sleep(2)

    pss_ent = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")

    pss_ent.clear()
    pss_ent.send_keys(pss)
    pss_ent.send_keys(Keys.ENTER)

    time.sleep(5)

    try:
        # see insta Messages
        main = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CLASS_NAME,"KdEwV"))
            )

        print("Line-1",main.text)

        main.click()

        time.sleep(10)

        # click First Message
        main_2 = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CLASS_NAME,"-qQT3.rOtsg"))
            )

        print("Line-2",main_2.text)

        main_2.click()

        time.sleep(10)

        # Auto replay For First Contact
        main_3 = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CLASS_NAME,"focus-visible"))
            )

        print("Line-3",main_3.text)

        main_3.click()

        main_3.clear()
        main_3.send_keys("cool pic bro")
        main_3.send_keys(Keys.ENTER)

        time.sleep(5)



        # articles = main.find_element_by_class_name("bg-blue")
        # print("Line-2",articles.text)

        # target subelements
        # for article in articles:
        #     header = article.find_element_by_class_name("bg-blue")
        #     print(header.text)
    except:
        print("Error")



def follow(hashtag):
    driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
    time.sleep(5)

    # Scrolling
    # for i in range(7):
    #     driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")


    href_found = driver.find_element_by_tag_name("a")
    print("href_founf",href_found)
    pic_href = [ele.get_attribute('href') for ele in href_found if '.com/p' in ele.get_attribute('href')]
    print("pic href:-",pic_href)

    for ele in pic_href:
        driver.get(ele)
        time.sleep(5)

        # For Follow
        #follow = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[2]/botton")
        
        # For Like
        follow = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[1]/span[1]/button")
        follow.click()
        time.sleep(5)


if __name__ == "__main__":
    
    # first login
    login("Username","Password")    

    # Foollow hashtags
    # follow("hacking")        

    
