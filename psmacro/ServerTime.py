from selenium import webdriver
from datetime import datetime


def is_cancel_ticket_open():

    is_cancel_ticket_time = False

    current_hour = int(datetime.today().hour)
    current_minute = int(datetime.today().minute)

    if(current_hour == 2) and (0 <= current_minute <= 40):
        is_cancel_ticket_time = True

    return is_cancel_ticket_time


class ServerTime():
    def __init__(self, url):
        self.time_driver = webdriver.Chrome('./chromedriver')
        self.time_driver.get('https://time.navyism.com/?host='+url)
        self.time_driver.find_element_by_id('msec_check').click()

    def get_time(self):
        return self.time_driver.find_element_by_id('time_area').text

    def get_msec_time(self):
        return self.time_driver.find_element_by_id('msec_area').text





