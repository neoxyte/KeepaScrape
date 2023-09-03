from playwright.sync_api import sync_playwright
import pandas as pd

import time

#todo
'''
debug mode = head browser not headless
Read keepa username and pw
go to keepa site
login if needed

input list of asins to search
one by one go through each asin (see if async is better for this)



'''

def get_asin_input():
    '''Takes user input from terminal. One asin per new line. Returns a data frame'''
    #TODO sanitize input; Error check input
    print("Copy and Paste asins. Enter blank line when finished:")
    asins = []
    while True:
        asin = input()
        if asin:
            asins.append(asin)
        else:
            break
    print("ASIN List: " + str(asins))
    data = {
        'asin' : [],
        'title' : [],
        'sales30': [],
        'stock30': [],
    }
    return data

def login(page, username, password):
    '''
    page.get_by_label("Username or email address").fill("username")
    page.get_by_label("Password").fill("password")
    page.get_by_role("button", name="Sign in").click()'''
    input("please login, press enter when ready")
    return False

def scrape_asin(asin):
    #TODO pass asin list here
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        #todo login
        login(page, "yonahs", "okeanos613")
        #for product in asins:
            #TODO
        '''driver.get('https://keepa.com/iframe_addon.html#1-0-'+ each['asin'])            
            print('\t ASIN: {:s}'.format(str(each['asin'])))
            print('\t Title: {:s}'.format(str(each['title'])))
            time.sleep(3)
            #click data tab
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,get_xpath(driver,'ce0s0srBElOUf0S')))).click()
            #click offers tab
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,get_xpath(driver,'Knhhnd9L2rkq8dF')))).click()
            xpath = '//*[@id="grid-offer"]/div/div[2]/div[1]/div[4]/div[2]/div/div/div[7]'
            element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            sales = element.text
            data['asin'].append(each['asin'])
            data['title'].append(each['title'])
            data['sales30'].append(sales.split('~')[1])
            print("\tSales 30 for " + asin + ": " + sales.split('~')[1])'''
        time.sleep(3)
