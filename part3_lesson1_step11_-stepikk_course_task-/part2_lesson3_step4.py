from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    ...



    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button[type=submit]")
    button.click()

    confirm=browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_css_selector('.form-group .nowrap#input_value')
    x = x_element.text
    y = calc(x)
    y_element = browser.find_element_by_css_selector('.form-group #answer  ')
    y_element.send_keys(y)

    button = browser.find_element_by_css_selector("button[type=submit]")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()