#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import time
import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chromedriver_path = 'フルパス'


# In[ ]:


x1 = "/html/body/div/div/div/div[2]/p[2]/a"
x2 = "//*[@id='idToken1']"
x3 = "//*[@id='idToken2']" 
x4 = "//*[@id='loginButton_0']"
x5 = "//*[@id='content']/div/form/fieldset/div[2]/div[1]/button[2]"


# In[ ]:


login = "//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/c-wiz/div/div[4]/div/div/c-wiz/section/article/div/div/div/div/div/div/div[4]/div/a"
email = "//*[@id='identifierId']"
email_next = "//*[@id='identifierNext']/span/span"
continue_ = "//*[@id='view_container']/div/div/div[2]/div/div[2]/div/div[1]/div/span/span"


# In[ ]:


url = "https://myaccount.google.com/intro?utm_source=OGB&tab=rk&utm_medium=app" 
moocs = "https://moocs.iniad.org/courses/2019/DS103/DM-02-03/02" #moocs URLを指定して

iniad_mail = "@iniad.org" #自分のINIADのメールアドレス入力させる
ID = "ID" # INIADのID
Password = "Password" # INIADのPassword

make_dir = "hoge" # 作りたいディレクトリの名前
if not os.path.exists(make_dir):
    os.mkdir(make_dir) 
slide_count = ??? # スライドの枚数


# In[ ]:


options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.add_argument('--no-sandbox')

# capabilities = DesiredCapabilities.CHROME.copy()
# capabilities['acceptInsecureCerts'] = True


x = 280
y = 313

try:
#     driver = webdriver.Chrome(executable_path=chromedriver_path,
#                               options=options,
#                               desired_capabilities=capabilities)
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    driver.set_window_size(600, 600) #windowのsizeの指定　幅：高さ
    driver.get(url) #一番最初のURLへ
    print('clear1')
    time.sleep(2) #sleepさせないとページ読み込み遅い時errorになる
    driver.find_element_by_xpath(login).click()
    print('clear2')
    time.sleep(2)
    print('clear3')
    driver.find_element_by_xpath(email).send_keys(iniad_mail)
    print('clear4')
    driver.find_element_by_xpath(email_next).click()
    print('clear5')
    time.sleep(4)
    driver.find_element_by_xpath(x2).send_keys(ID)
    driver.find_element_by_xpath(x3).send_keys(Password)
    driver.find_element_by_xpath(x4).click()
    print('clear4')
    time.sleep(3)
    driver.find_element_by_xpath(continue_).click()
    time.sleep(3)
    driver.get(moocs)
    time.sleep(2)
    driver.find_element_by_xpath(x1).click()
    time.sleep(2)
    driver.find_element_by_xpath(x5).click()
    time.sleep(5)
    pyautogui.moveTo(x, y)
    pg.vscroll(-10)
    time.sleep(1)
    for i in range(slide_count):
        time.sleep(1)
        pg.screenshot('{0}/{1}{2}.png'.format(make_dir, make_dir, i), region=(0, 50, 1200, 1000)) #左上のx座標=0, 左上のy座標=50 の位置から幅300, 高さ=400
        pg.click(x, y)
    time.sleep(5)
    driver.quit()
except:
    time.sleep(5)
    driver.quit()


# In[ ]:





# In[ ]:




