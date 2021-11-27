from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return math.log(abs(12*math.sin(x)))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    ...
    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    z=calc(x)
    y_element = browser.find_element_by_id('answer')
    y_element.send_keys(f"{z}")
    print(z)

    browser.execute_script("window.scrollBy(0, 150);")

    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()

    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()

    button = browser.find_element_by_css_selector("button[type=submit]")
    button.click()




    # Отправляем заполненную форму


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

input("Нажмите Enter")