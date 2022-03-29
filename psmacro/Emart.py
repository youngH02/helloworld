from selenium import webdriver

class Emart():
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.user_id: str = 'genesis87'
        self.user_pwd: str = 'Ckwlsdnr1!'


    def _do_login(self):
        print('------ LOGIN START ------')
        try:
            self.driver.get('https://member.ssg.com/member/popup/popupLogin.ssg?originSite=http%3A//emart.ssg.com&t=&gnb=login')
            self.driver.find_element_by_id('mem_id').send_keys(self.user_id)
            self.driver.find_element_by_id('mem_pw').send_keys(self.user_pwd)
            self.driver.find_element_by_id('loginBtn').click()
            self.is_login = True
        except Exception as e:
            print('예외가 발생', e)

        print('------ LOGIN DONE ------')

    def _go_reserve_page(self):
        def _go_reserve_page(self):
            self.seat_url = 'http://poticket.interpark.com/Book/BookSession.asp?GroupCode={}&Tiki=N&Point=N&PlayDate={}&PlaySeq={}&BizCode=&BizMemberCode='.format(
                self.group_code, self.play_date, self.play_seq)
            self.driver.get(self.seat_url)