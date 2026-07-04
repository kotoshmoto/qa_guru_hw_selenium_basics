import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from generators.form_fields_g import g_get_valid_fields, g_get_invalid_email


def test_fill_form_fields():
    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        # web_elements = driver.find_elements(By.XPATH, "someXPath")
        full_name_field.clear()
        full_name_field.send_keys("Петров Петр Петрович")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.clear()
        email_field.send_keys("test@example.com")

        # Находим поле Current Address по его ID и вводим текст
        current_address = driver.find_element(By.ID, "currentAddress")
        current_address.clear()
        current_address.send_keys("г. Москва, Пушкина 101")

        # Находим поле Permanent Address по его ID и вводим текст
        permanent_address = driver.find_element(By.ID, "permanentAddress")
        permanent_address.clear()
        permanent_address.send_keys("г. Москва, Комсомольский проспект 42")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert "Петров Петр Петрович" in result_box.text
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


@pytest.mark.parametrize("params", g_get_valid_fields())
def test_fill_form_fields_with_valid_values(params):
    fullname, email, cur_addr, per_addr = params

    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст

        full_name_field = driver.find_element(By.ID, "userName")
        # web_elements = driver.find_elements(By.XPATH, "someXPath")
        full_name_field.clear()
        full_name_field.send_keys(fullname)

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.clear()
        email_field.send_keys(email)

        # Находим поле Current Address по его ID и вводим текст
        current_address = driver.find_element(By.ID, "currentAddress")
        current_address.clear()
        current_address.send_keys(cur_addr)

        # Находим поле Permanent Address по его ID и вводим текст
        permanent_address = driver.find_element(By.ID, "permanentAddress")
        permanent_address.clear()
        permanent_address.send_keys(per_addr)

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert fullname in result_box.text
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


@pytest.mark.parametrize("email", g_get_invalid_email())
def test_fill_form_with_invalid_email(email):
    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст

        full_name_field = driver.find_element(By.ID, "userName")
        # web_elements = driver.find_elements(By.XPATH, "someXPath")
        full_name_field.clear()
        full_name_field.send_keys("Захаров Геннадий Павлович")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.clear()
        email_field.send_keys(email)

        # Находим поле Current Address по его ID и вводим текст
        current_address = driver.find_element(By.ID, "currentAddress")
        current_address.clear()
        current_address.send_keys("г. Санкт-Петербург, Ленина 12, 22")

        # Находим поле Permanent Address по его ID и вводим текст
        permanent_address = driver.find_element(By.ID, "permanentAddress")
        permanent_address.clear()
        permanent_address.send_keys("г. Санкт-Петербург, Ленина 12, 24")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        validation_message = email_field.get_property("validationMessage")
        print(validation_message)

        assert (f'Адрес электронной почты должен содержать символ "@". В адресе "{email}"'
                f' отсутствует символ "@".') in validation_message

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()



