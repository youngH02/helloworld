from selenium import webdriver


class Himart():
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.user_id: str = 'genesis87'
        self.user_pwd: str = 'Ckwlsdnr1!'

    def _do_login(self):
        print('------ LOGIN START ------')
        try:
            self.driver.get(
                'https://secure.e-himart.co.kr/app/login/login?returnUrl=http%3A%2F%2Fwww.e-himart.co.kr%2F')
            self.driver.find_element_by_id('ssoId').send_keys(self.user_id)
            self.driver.find_element_by_id('ssoPw').send_keys(self.user_pwd)
            self.driver.find_element_by_id('sso').click()
            self.is_login = True
        except Exception as e:
            print('예외가 발생', e)

        print('------ LOGIN DONE ------')

    def _go_reserve_page(self):
        self.seat_url = 'http://poticket.interpark.com/Book/BookSession.asp?GroupCode={}&Tiki=N&Point=N&PlayDate={}&PlaySeq={}&BizCode=&BizMemberCode='.format(
            self.group_code, self.play_date, self.play_seq)
        self.driver.get(self.seat_url)