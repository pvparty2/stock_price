from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def open_yahoo():
    """Function opens a Chrome or Firefox to finance.yahoo.com"""
    website = 'https://finance.yahoo.com/'

    # try to open Firefox
    try:
        print('Opening Firefox...')
        driver = webdriver.Firefox()
        driver.get(website)
        try:
            WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((
                    By.ID, 'yfin-usr-qry'
                ))
            )
        except:
            print('Error Firefox')
        return driver
    except:
        print('Could not open Firefox.')

    # if cannot open Firefox, try to open Chrome
    try:
        print('Opening Chrome...')
        driver = webdriver.Chrome()
        driver.get(website)
        try:
            WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((
                    By.ID, 'yfin-usr-qry'
                ))
            )
            print('Error Chrome')
        except:
            print('this is not ok')
        return driver

    # if could not open either, exit
    except:
        print('Could not open Chrome.\nEnding program.')


class Driver():
"""A tool that reads Yahoo stock webpages"""
    def __init__(self):
        self.driver = open_yahoo()
        self.counter_price = 0
        self.counter_name = 0


    def search(self, text):
    """Searches through Yahoo search bar"""
        time.sleep(1)
        elem = self.driver.find_element_by_id('yfin-usr-qry')
        elem.send_keys(text)
        time.sleep(1)
        self.driver.find_element_by_id('search-button').click()


    def get_price(self):
        # wait for element to appear 
        # get the stock price    
        got_price = False
        while not got_price:
            try:
                stock_price = self.driver.find_element_by_xpath(
                    '//span[@class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"]'
                ).text
                got_price = True
            except:
                print('Could not get price. Trying again...')
                self.counter_price += 1
                print(str(self.counter_price))
                continue
        return stock_price
        

    def get_name(self):
        # wait for element to appear 
        # get the stock name        
        got_name = False
        while not got_name:
            try:    
                stock_name = self.driver.find_element_by_xpath(
                    '//h1[@class="D(ib) Fz(18px)"]'
                ).text
                got_name = True
            except:
                print('Could not get name. Trying again...')
                self.counter_name += 1
                print(str(self.counter_name))
                continue
        return stock_name
        

    def quit(self):
        self.driver.quit()
        return print('Browser closed.')


