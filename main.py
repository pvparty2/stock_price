import time
import smtplib
import webpage
import sys
import messenger

# Open Chrome driver and go to Finance Homepage
my_driver = webpage.Driver()

# Search for stock info and get the stock page
search_text = 'TESLA'
my_driver.search(search_text)

# Read Stock Name
stock_name = my_driver.get_name()

# Read Stock Price
stock_price = my_driver.get_price()

# Sign in to your email and send message of stock price
my_messenger = messenger.Messenger()
my_messenger.send_text_msg(stock_name + ' Current Price:', stock_price)

# Send another message if stock price changes by $delta
is_done = False
while not is_done:
"""Message new price when it moves up/down by delta"""
    new_stock_price = my_driver.get_price()
    delta = 0

    if abs(float(stock_price.replace(',', '')) - \
        float(new_stock_price.replace(',', ''))) >= delta:
        stock_price = new_stock_price
        is_done = True
        my_messenger = messenger.Messenger()
        my_messenger.send_text_msg(stock_name + ' Current Price:', stock_price)
        print('Changed by $%s.' % (str(delta)))
    else:
        time.sleep(2)

my_driver.quit()




