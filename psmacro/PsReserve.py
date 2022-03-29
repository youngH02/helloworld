
import PreOrders
import ServerTime
from selenium.webdriver.chrome.options import Options

class PsReserve():
    def __init__(self):
        self.reserve_time = '2021년 09월 03일 12시 00분 00초'
        self.reserve = False


    def _do_reserve(self):
        server_time = ServerTime.ServerTime("http://preorders.kr")

        preOrders = PreOrders.PreOrders('http://preorders.kr/product/detail?id=1396')
        preOrders._go_reserve_page()


        while not self.reserve:
            if self.reserve_time == server_time.get_time():
                preOrders._do_refresh()
                preOrders._do_write()
                self.reserve = True





