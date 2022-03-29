from selenium import webdriver
from selenium.webdriver.support.ui import Select

class PreOrders():
    def __init__(self, url):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options=self.options, executable_path=r'./chromedriver')
        self.seat_url = url

    def _go_reserve_page(self):
        self.driver.get(self.seat_url)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def _do_refresh(self):
        self.driver.execute_script("location.reload()")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def _do_write(self):
        self.driver.find_element_by_id('etc').click()
        self.driver.find_element_by_id('customer-name').send_keys('전민승')
        self.driver.find_element_by_id('customer-tel').send_keys('01041394619')
        self.driver.find_element_by_id('pwd').send_keys('1111')
        self.driver.find_element_by_id('re-pwd').send_keys('1111')
        select = Select(self.driver.find_element_by_id('product'))
        select.select_by_index(1)

