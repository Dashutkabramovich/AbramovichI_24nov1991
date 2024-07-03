import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
      def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.sibdar-spb.ru")
        self._driver.implicitly_wait(20)
        self._driver.maximize_window()
        
      with allure.step("Заполнение персональных данных"):
        def personal_data(self, name: str, phone: int, email: str, comment: str):
                 self._driver.get("https://www.sibdar-spb.ru")
                 self._driver.find_element(By.XPATH, '/html/body/header/div/div/div[2]/div/button[1]').click()
                 self._driver.find_element(By.XPATH, '//*[@id="formCall"]/input[4]').send_keys(name)
                 phone = WebDriverWait(self._driver, 10).until(
    EC.visibility_of_element_located
    ((By.XPATH,'//*[@id="formCall"]/input[5]'))).send_keys(phone)
                 #self._driver.find_element(By.XPATH, '//*[@id="formCall"]/input[5]').send_keys(phone)
                 self._driver.find_element(By.XPATH, '//*[@id="formCall"]/input[6]').send_keys(email)
                 self._driver.find_element(By.XPATH, '//*[@id="formCall"]/textarea').send_keys(comment)
                 self._driver.find_element(By.XPATH, '//*[@id="formCall"]/button').click()
                 txt = WebDriverWait(self._driver, 5).until(
    EC.visibility_of_element_located
    ((By.XPATH,'/html/body/div[2]/div[2]/h3'))).text
                 return txt   
             
      with allure.step("Пустая корзина"):
            def empty_cart(self):
                 self._driver.get("https://www.sibdar-spb.ru")
                 self._driver.find_element(By.XPATH, '/html/body/header/div/div/div[2]/div/a').click()
                 txt = self._driver.find_element(By.XPATH,'//*[@id="order-list"]/h2').text
                 return txt  
            
      with allure.step("Добавить товар в корзину"):
            def add_item(self):
                 self._driver.get("https://www.sibdar-spb.ru")
                 self._driver.find_element(By.XPATH, '//*[@id="bx_3218110189_204"]/div[3]/button').click()
                 self._driver.find_element(By.XPATH, '/html/body/a').click()
                 counter = self._driver.find_element(By.XPATH,'//*[@id="price_ti_204"]').text
                 return counter  
      
      with allure.step("Закрытие веб-браузера"):
            def close_driver(self):
                self._driver.quit()