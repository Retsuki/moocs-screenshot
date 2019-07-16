#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import time
import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chromedriver_path = 'Your chromedriver path'


# In[2]:


x1 = "/html/body/div/div/div/div[2]/p[2]/a"
x2 = "//*[@id='idToken1']"
x3 = "//*[@id='idToken2']"
x4 = "//*[@id='loginButton_0']"
x5 = "//*[@id='content']/div/form/fieldset/div[2]/div[1]/button[2]"


# In[3]:


login = "//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/c-wiz/div/div[4]/div/div/c-wiz/section/article/div/div/div/div/div/div/div[4]/div/a"
email = "//*[@id='identifierId']"
email_next = "//*[@id='identifierNext']/span/span"
continue_ = "//*[@id='view_container']/div/div/div[2]/div/div[2]/div/div[1]/div/span/span"


# In[4]:


url = "https://myaccount.google.com/intro?utm_source=OGB&tab=rk&utm_medium=app"
moocs = str(input("What URL ? : "))  # moocs URLを指定して

iniad_mail = "Your Iniad Email address"  # 自分のINIADのメールアドレス入力させる
ID = "Your Iniad ID"  # INIADのID
Password = "Your Iniad Password"  # INIADのPassword

make_dir = str(input("Make dir name: "))
if not os.path.exists(make_dir):
    os.mkdir(make_dir)  # 作りたいディレクトリ
slide_count = int(input("How page ? : "))


# In[5]:


options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.add_argument('--no-sandbox')

# capabilities = DesiredCapabilities.CHROME.copy()
# capabilities['acceptInsecureCerts'] = True


x = 567
y = 205

try:
    #     driver = webdriver.Chrome(executable_path=chromedriver_path,
    #                               options=options,
    #                               desired_capabilities=capabilities)
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    driver.set_window_size(600, 600)  # windowのsizeの指定　幅：高さ
    driver.get(url)  # 一番最初のURLへ
    time.sleep(2)  # sleepさせないとページ読み込み遅い時errorになる
    driver.find_element_by_xpath(login).click()
    time.sleep(2)
    driver.find_element_by_xpath(email).send_keys(iniad_mail)
    driver.find_element_by_xpath(email_next).click()
    time.sleep(4)
    driver.find_element_by_xpath(x2).send_keys(ID)
    driver.find_element_by_xpath(x3).send_keys(Password)
    driver.find_element_by_xpath(x4).click()
    time.sleep(3)
    driver.find_element_by_xpath(continue_).click()
    time.sleep(3)
    driver.get(moocs)
    time.sleep(2)
    driver.find_element_by_xpath(x1).click()
    time.sleep(2)
    driver.find_element_by_xpath(x5).click()
    time.sleep(5)
    pg.moveTo(x, y)
    time.sleep(2)
    pg.vscroll(-10)
    time.sleep(1)
    """ カーソルの位置の確認
    print(pg.position())
    time.sleep(1)
    print(pg.position())
    time.sleep(1)
    print(pg.position())
    time.sleep(1)
    print(pg.position())
    time.sleep(1)
    print(pg.position())
    """
    for i in range(slide_count):
        time.sleep(1)
        # 左上のx座標=0, 左上のy座標=50 の位置から幅300, 高さ=400
        pg.screenshot('{0}/{1}.png'.format(make_dir, i),
                      region=(0, 50, 1200, 1000))
        pg.click(x, y)
    time.sleep(1)
    driver.quit()
except:
    time.sleep(1)
    driver.quit()


# In[ ]:
