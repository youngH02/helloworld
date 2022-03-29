from selenium import webdriver

class Etland():
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.user_id: str = 'genesis87'
        self.user_pwd: str = 'Ckwlsdnr1!'


    def _do_login(self):
        print('------ LOGIN START ------')
        try:
            self.driver.get('https://www.etlandmall.co.kr/pc/manager/login.do?url=https%3A%2F%2Fwww.etlandmall.co.kr%2Fpc%2Fmain%2Findex.do&locationProtocol=http')
            self.driver.find_element_by_id('MEM_MST_MEM_ID').send_keys(self.user_id)
            self.driver.find_element_by_id('MEM_MST_WEB_PWD').send_keys(self.user_pwd)
            self.driver.execute_script("login('');")
            self.is_login = True
        except Exception as e:
            print('예외가 발생', e)

        print('------ LOGIN DONE ------')

    def _go_reserve_page(self):
        self.seat_url = 'https://www.etlandmall.co.kr/pc/product/product.do?prdMstCd=S2846563'
        self.driver.get(self.seat_url)