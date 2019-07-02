import sys
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
testing = False #True
try:
    if not testing:
        driver = webdriver.Chrome('chromedriver.exe')  # Optional argument, if not specified will search path.
        driver.get('https://register.moex.gov.tw/index_S2.jsp?language=C&firstPage=Y&fun=A')
        time.sleep(3) # Let the user actually see something!
        driver.get('https://register.moex.gov.tw/portal_c/registration/a901m.jsp?language=C')
        IDPWD_box = driver.find_element_by_id('p_idno') #//*[@id="ctl00_holderContent_txtSubjectName"]
        IDPWD_box.clear()
        IDPWD_box.send_keys(sys.argv[1])
        IDPWD_box = driver.find_element_by_id('p_password') #//*[@id="ctl00_holderContent_txtSubjectName"]
        IDPWD_box.clear()
        IDPWD_box.send_keys(sys.argv[2])
        time.sleep(3) # Let the user actually see something!
        Verb_box = driver.find_element_by_xpath('//*[@id="table1"]/tbody/tr[6]/td/input') #////*[@id="ctl00_holderContent_ibtnFull"]
        Verb_box.click()
        time.sleep(3) # Let the user actually see something!
        Verb_box = driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table/tbody/tr[2]/td[7]/input')
        Verb_box.click()
        time.sleep(3) # Let the user actually see something!
        ExamSubject = Select(driver.find_element_by_name('OBJECT_Name_TMP'))
        ExamSubject.select_by_index(2)
        QUESTION_NO_box = driver.find_element_by_name('QUESTION_NO') #//*[@id="ctl00_holderContent_txtSubjectName"]
        QUESTION_NO_box.clear()
        QUESTION_NO_box.send_keys('74')
        EXAMINEE_RSN_box = driver.find_element_by_name('EXAMINEE_RSN') #//*[@id="ctl00_holderContent_txtSubjectName"]
        EXAMINEE_RSN_box.clear()
        EXAMINEE_RSN_box.send_keys('''考生當初在螢幕上看到的圖非常暗，不明顯，希望可請老師們也在螢幕確認暗度可理解我們考生情況。

建議答案：A B C D
''')
        ChoiceA = driver.find_element_by_xpath('//*[@id="sub"]/input[1]')
        if not ChoiceA.is_selected():
            ChoiceA.click()
        ChoiceB = driver.find_element_by_xpath('//*[@id="sub"]/input[2]')
        if not ChoiceB.is_selected():
            ChoiceB.click()
        ChoiceC = driver.find_element_by_xpath('//*[@id="sub"]/input[3]')
        if not ChoiceC.is_selected():
            ChoiceC.click()
        ChoiceD = driver.find_element_by_xpath('//*[@id="sub"]/input[4]')
        if not ChoiceD.is_selected():
            ChoiceD.click()
        time.sleep(50) # Let the user actually see something!
finally:
    if not testing:
        driver.quit()
