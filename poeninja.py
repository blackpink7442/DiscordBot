from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import discord

options = Options()
options.add_argument("--no-sandbox") #bypass OS security model
options.add_argument("headless")
browser = webdriver.Chrome(options=options)

def get_orb_price(url):
    Orburl = 'https://poe.ninja/challenge/currency/{}'.format(url)
    browser.get(Orburl)
    OrbName = []
    try:
        OrbName.append("Buy")
        for i in range(1,4):
            if i != 2:
                OrbName.append(browser.find_element_by_xpath('//*[@id="main"]/section/div/main/section/div/div/div[2]/div[1]/div[1]/div/span[{}]/div/span'.format(i)).text)
                OrbName.append(browser.find_element_by_xpath('//*[@id="main"]/section/div/main/section/div/div/div[2]/div[1]/div[1]/div/span[{}]/span'.format(i)).text)
            elif i ==2:
                OrbName.append('for')

    except:
        print('not found Orb price')
    print("--------------------")
    try:
        OrbName.append("Sell")
        for i in range(1,4):
            if i != 2:
                OrbName.append(browser.find_element_by_xpath('//*[@id="main"]/section/div/main/section/div/div/div[2]/div[1]/div[2]/div/span[{}]/div/span'.format(i)).text)
                OrbName.append(browser.find_element_by_xpath('//*[@id="main"]/section/div/main/section/div/div/div[2]/div[1]/div[2]/div/span[{}]/span'.format(i)).text)

            elif i == 2:
                OrbName.append('for')
    except:
        print('not found Orb price')
    return OrbName