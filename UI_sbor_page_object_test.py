import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pages.MainPage import MainPage

@allure.title("Открытие сайта")
@allure.description("Тест проверяет наличие связи с сайтом")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_opening(): 
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        browser = webdriver.Chrome() 
        main_page = MainPage(browser)  

@allure.title("Заполнение персональных данных")
@allure.description("Тест проверяет заполнение персональных данных при заказе звонка с последующим сообщением 'Спасибо, Ваша заявка отправлена!'")
@allure.feature("UPDATE")
@allure.severity("blocker")
def test_personal_data():
    with allure.step("Открытие веб-страницы в Chrome"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser)
    with allure.step("Заполнение персональных данных"):
        msg = main_page.personal_data("Daria", "9036456738", "dariaabr@mail.ru", "Просьба звонить до 22:00")
        assert msg == "Спасибо, Ваша заявка отправлена!"
    with allure.step("Закрытие браузера"):
        main_page.close_driver()  
        
@allure.title("Пустая корзина")
@allure.description("Тест проверяет, что в пустой корзине отображается сообщение'Корзина пуста, необходимо это исправить'")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_empty_cart():
    with allure.step("Открытие веб-страницы в Chrome"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser)
    with allure.step('Проверка наличия фразы "Корзина пуста, необходимо это исправить"'):
        msg = main_page.empty_cart()
        assert msg == "Корзина пуста, необходимо это исправить"
    with allure.step("Закрытие браузера"):
        main_page.close_driver()

@allure.title("Добавление товара в корзину")
@allure.description("Тест проверяет, что товар добавляется в корзину и отображение суммы заказа")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_add_item():
    with allure.step("Открытие веб-страницы в Chrome"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser)
    with allure.step("Проверка суммы покупки: 1400"):
        msg = main_page.add_item()
        assert msg == "1400"
    with allure.step("Закрытие браузера"):
        main_page.close_driver()