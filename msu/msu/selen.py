import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By


def find_a(f, question):
    t = ''
    f.seek(0)
    ans = set()
    while True:
        file_line = f.readline()[:-1]
        # print(list(file_line))
        if file_line == "END":
            ans = list(ans)
            ans.append(t)
            return ans
        if question == file_line:
            file_line = f.readline()[:-1]
            number, t = file_line.split()
            for i in range(int(number)):
                file_line = f.readline()[:-1]
                ans.add(file_line)


driver = webdriver.Chrome()
file = open("C:\\Users\пк\Downloads\\answers (1) (1).txt", encoding='utf-8')
login = input("Insert login:")
password = input("Insert password:")
try:
    driver.maximize_window() #для того чтобы не было проблем, если сайт заебланит и велючит мобильную версию
    driver.get('https://dist.law.msu.ru/login/index.php')
    email_input = driver.find_element(By.NAME, "username")
    email_input.send_keys('15210836')#s15220500
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys('gkgN9ok7')#hMhu5kWv
    driver.find_element(By.ID, "loginbtn").click()
    link = driver.find_element(By.CSS_SELECTOR, '[href="https://dist.law.msu.ru/local/crw/category.php?cid=22&crws"]')
    link.click()
    link = driver.find_element(By.CSS_SELECTOR, '[href="https://dist.law.msu.ru/local/crw/category.php?cid=65&crws"]')
    link.click()
    link = driver.find_element(By.CSS_SELECTOR, '[href="https://dist.law.msu.ru/local/crw/course.php?id=94"]')
    link.click()
    link = driver.find_element(By.CSS_SELECTOR, '[href="https://dist.law.msu.ru/course/view.php?id=94"]')
    link.click()
    link = driver.find_element(By.CSS_SELECTOR, '[href="https://dist.law.msu.ru/mod/quiz/view.php?id=1825"]')
    link.click()
    link = driver.find_element(By.CSS_SELECTOR, '[action="https://dist.law.msu.ru/mod/quiz/startattempt.php"]')
    link.click()
    for i in range(20):
        qtext = driver.find_element(By.CLASS_NAME, 'qtext').text
        answers = find_a(file, qtext)
        if answers[-1] == "Test":
            answer = driver.find_element(By.CLASS_NAME, "answer").text.split('\n')
            ii = 0
            while ii < len(answer):
                if answer[ii] == '':
                    answer.pop(ii)
                    ii -= 1
                ii += 1
            for i in range(len(answer)):
                if answer[i] in answers:
                    elem = driver.find_element(By.XPATH, f'//input[contains(@id, "_choice{i}") or contains(@id, "_answer{i}")]')
                    elem.click()
        elif answers[-1] == "Write":
            elem = driver.find_element(By.XPATH, f'//input[contains(@id, "_answer")]')
            elem.send_keys(answers[0])
        # time.sleep(randint(420, 1020))
        btn = driver.find_element(By.NAME, "next")
        btn.click()
    link = driver.find_element(By.CSS_SELECTOR, '[action="https://dist.law.msu.ru/mod/quiz/processattempt.php"]')
    link.click()
    time.sleep(100000)
    pass
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
file.close()







