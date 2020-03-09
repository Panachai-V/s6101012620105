from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_calculate_POST(self):
        # เขาได้ยินมาว่ามีเว็บสำหรับคิดเลข
        # จึงเข้าเว็บไปที่หน้า Homepage
        self.browser.get('http://localhost:8000/home_POST.html')

        # เขาสังเกตุว่าชื่อเว็บจะมีคำว่า calculator
        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Calculator by POST', header_text)

        # เขาเห็นช่องสำหรับใส่ค่าเข้าไป
        first_box = self.browser.find_element_by_tag_name('first_box').text
        self.assertIn('Enter a 1st number:', first_box)
        second_box = self.browser.find_element_by_tag_name('second_box').text
        self.assertIn('Enter a 2nd number:', second_box)

        # เขาต้องการบวกเลข
        # เขาใส่เลขไปในช่องที่ 1
        first_textbox = self.browser.find_element_by_id("first_textbox")
        first_textbox.send_keys('2')
        # เขาใส่เลขไปในช่องที่ 2
        second_textbox = self.browser.find_element_by_id("second_textbox")
        second_textbox.send_keys('3')
        # เข้ากุปปุ่ม add
        add_button = self.browser.find_element_by_id("add")
        add_button.click()
        # เขาเห็นผลลัพธ์มีค่าเท่ากับ 5
        result_text = self.browser.find_element_by_tag_name('result').text
        self.assertIn('Your Result : 5.0', result_text)


        # เขาต้องการลบเลข
        # เขาใส่เลขไปในช่องที่ 1
        first_textbox = self.browser.find_element_by_id("first_textbox")
        first_textbox.send_keys('199')
        # เขาใส่เลขไปในช่องที่ 2
        second_textbox = self.browser.find_element_by_id("second_textbox")
        second_textbox.send_keys('198')
        # เข้ากุปปุ่ม add
        add_button = self.browser.find_element_by_id("sub")
        add_button.click()
        # เขาเห็นผลลัพธ์มีค่าเท่ากับ 5
        result_text = self.browser.find_element_by_tag_name('result').text
        self.assertIn('Your Result : 1.0', result_text)


        # เขาต้องการคูณเลข
        # เขาใส่เลขไปในช่องที่ 1
        first_textbox = self.browser.find_element_by_id("first_textbox")
        first_textbox.send_keys('5')
        # เขาใส่เลขไปในช่องที่ 2
        second_textbox = self.browser.find_element_by_id("second_textbox")
        second_textbox.send_keys('5')
        # เข้ากุปปุ่ม add
        add_button = self.browser.find_element_by_id("mul")
        add_button.click()
        # เขาเห็นผลลัพธ์มีค่าเท่ากับ 5
        result_text = self.browser.find_element_by_tag_name('result').text
        self.assertIn('Your Result : 25.0', result_text)


        # เขาต้องการหารเลข
        # เขาใส่เลขไปในช่องที่ 1
        first_textbox = self.browser.find_element_by_id("first_textbox")
        first_textbox.send_keys('100')
        # เขาใส่เลขไปในช่องที่ 2
        second_textbox = self.browser.find_element_by_id("second_textbox")
        second_textbox.send_keys('5')
        # เข้ากุปปุ่ม add
        add_button = self.browser.find_element_by_id("div")
        add_button.click()
        # เขาเห็นผลลัพธ์มีค่าเท่ากับ 5
        result_text = self.browser.find_element_by_tag_name('result').text
        self.assertIn('Your Result : 20.0', result_text)
        time.sleep(3)

        self.fail('Finish the test!')

    def test_calculate_GET(self):
        # เขาได้ยินมาว่ามีเว็บสำหรับคิดเลข
        # จึงเข้าเว็บไปที่หน้า Homepage
        self.browser.get('http://localhost:8000/home_GET.html')

        # เขาสังเกตุว่าชื่อเว็บจะมีคำว่า calculator
        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Calculator by GET', header_text)

        # เขาเห็นช่องสำหรับใส่ค่าเข้าไป
        first_box = self.browser.find_element_by_tag_name('first_box').text
        self.assertIn('Enter a 1st number:', first_box)
        second_box = self.browser.find_element_by_tag_name('second_box').text
        self.assertIn('Enter a 2nd number:', second_box)

        # เขาต้องการบวกเลข
        # เขาใส่เลขไปในช่องที่ 1
        first_textbox = self.browser.find_element_by_id("first_textbox")
        first_textbox.send_keys('2')
        # เขาใส่เลขไปในช่องที่ 2
        second_textbox = self.browser.find_element_by_id("second_textbox")
        second_textbox.send_keys('3')
        # เข้ากุปปุ่ม add
        add_button = self.browser.find_element_by_id("add")
        add_button.click()
        # เขาเห็นผลลัพธ์มีค่าเท่ากับ 5
        result_text = self.browser.find_element_by_tag_name('result').text
        self.assertIn('Your Result : 5.0', result_text)


        # เขาต้องการลบเลข
        # เขาใส่เลขไปในช่องที่ 1
        first_textbox = self.browser.find_element_by_id("first_textbox")
        first_textbox.send_keys('199')
        # เขาใส่เลขไปในช่องที่ 2
        second_textbox = self.browser.find_element_by_id("second_textbox")
        second_textbox.send_keys('198')
        # เข้ากุปปุ่ม add
        add_button = self.browser.find_element_by_id("sub")
        add_button.click()
        # เขาเห็นผลลัพธ์มีค่าเท่ากับ 5
        result_text = self.browser.find_element_by_tag_name('result').text
        self.assertIn('Your Result : 1.0', result_text)


        # เขาต้องการคูณเลข
        # เขาใส่เลขไปในช่องที่ 1
        first_textbox = self.browser.find_element_by_id("first_textbox")
        first_textbox.send_keys('5')
        # เขาใส่เลขไปในช่องที่ 2
        second_textbox = self.browser.find_element_by_id("second_textbox")
        second_textbox.send_keys('5')
        # เข้ากุปปุ่ม add
        add_button = self.browser.find_element_by_id("mul")
        add_button.click()
        # เขาเห็นผลลัพธ์มีค่าเท่ากับ 5
        result_text = self.browser.find_element_by_tag_name('result').text
        self.assertIn('Your Result : 25.0', result_text)

        # เขาต้องการหารเลข
        # เขาใส่เลขไปในช่องที่ 1
        first_textbox = self.browser.find_element_by_id("first_textbox")
        first_textbox.send_keys('100')
        # เขาใส่เลขไปในช่องที่ 2
        second_textbox = self.browser.find_element_by_id("second_textbox")
        second_textbox.send_keys('5')
        # เข้ากุปปุ่ม add
        add_button = self.browser.find_element_by_id("div")
        add_button.click()
        # เขาเห็นผลลัพธ์มีค่าเท่ากับ 5
        result_text = self.browser.find_element_by_tag_name('result').text
        self.assertIn('Your Result : 20.0', result_text)
        time.sleep(3)

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')