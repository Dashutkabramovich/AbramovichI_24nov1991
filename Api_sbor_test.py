import allure
import requests
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

base_url = "https://www.sibdar-spb.ru"

@allure.title("Добавление товара в корзину")
@allure.description("Тест проверяет добавление одного товара в корзину")
@allure.feature("ADD")
@allure.severity("blocker")
@pytest.mark.positive_test

def test_add_product_to_cart():
     data = {
    "idCookie":866733,
    "idProd":"180",
    "type":"add"
}
     headers = { 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
}
     resp = requests.get(base_url+'/ajax/basketOrder.php', data=data, headers=headers)
     assert resp.status_code == 200
     assert resp.headers["Content-Type"] == "text/html; charset=UTF-8"

@allure.title("Добавление нескольких товаров в корзину")
@allure.description("Тест проверяет добавление двух товаров в корзину")
@allure.feature("ADD")
@allure.severity("blocker")
@pytest.mark.positive_test

def test_add_products_to_cart():
     data = {
    "idCookie":866733,
    "idProd":"496",
    "type":"add"
}
     headers = { 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
}
     resp = requests.get(base_url+'/ajax/basketOrder.php', data=data, headers=headers)
     assert resp.status_code == 200
     assert resp.headers["Content-Type"] == "text/html; charset=UTF-8"

@allure.title("Удаление товара из корзины")
@allure.description("Тест проверяет удаление товара из корзины")
@allure.feature("DELETE")
@allure.severity("blocker")
@pytest.mark.positive_test

def test_delete_product():
     
     data = {
    "idCookie":866733,
    "idProd":"496",
    "type":"delete"
}
     headers = { 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
}
     resp = requests.get(base_url+'/ajax/basketOrder.php', data=data, headers=headers)
     assert resp.status_code == 200
     assert resp.headers["Content-Type"] == "text/html; charset=UTF-8"

@allure.title("Отображение пустой корзины")
@allure.description("Тест проверяет отображение сообщения 'Корзина пуста, необходимо это исправить'")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_empty_cart():
    headers = { 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    resp = requests.get(base_url+'//ajax/basketList.php', headers=headers)
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "text/html; charset=UTF-8"
    assert 'Корзина пуста, необходимо это исправить' in resp.text