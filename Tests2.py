import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test:
    # для оптимизации предполагается замена ожиданий на явные, вынос селекторов в отдельный класс, выделение повторов в методы

    driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get("https://letbefit.ru/?ov2")

    def test1(self):
        '''
        Проверка невозможности заказать без заполнения телефона
        '''
        time.sleep(5)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(By.CSS_SELECTOR,
                                                                                                  ".br-8.bg--white.p-32"))
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".js-order-form-submit").click()
        assert self.driver.find_element(By.XPATH,
                                        "//div[@class='input-row input-row--validate checkPhoneBlockWithoutCoupon input-row--error']/child::div[@class='input-msg']").text == "Введите корректный телефон"
        time.sleep(3)
        self.driver.quit()

    def test2(self):
        '''
        Проверка заполнения полей при заказе и успешность перехода на страницу оформления заказа
        '''
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(By.CSS_SELECTOR,
                                                                                                  ".br-8.bg--white.p-32"))
        time.sleep(5)
        self.driver.find_elements(By.CSS_SELECTOR,
                                  ".check-dot.icon--32.br-round.bor.bor--border.cp.sm__hide")[0].click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,
                                 "//label[@class='check-el js-switch ']/div/div[1]").click()

        self.driver.find_element(By.XPATH,
                                 "//label[@class='check-el js-switch couponBlock']/div/div[1]").click()
        self.driver.find_element(By.XPATH,
                                 "//input[@data-test='recommendFriendPhone']/following-sibling::span").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 "//input[@data-test='recommendFriendPhone']").send_keys("4444444444")

        self.driver.find_element(By.XPATH,
                                 "//div[@class='input-row input-row--validate checkPhoneBlock']/input").click()
        self.driver.find_element(By.XPATH,
                                 "//div[@class='input-row input-row--validate checkPhoneBlock']/input").send_keys(
            "4444444449")
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".js-order-form-submit").click()
        time.sleep(5)
        assert self.driver.find_elements(By.XPATH,
                                         "//div[@class='type--w700 type--32 mb-32 sm__type--20']")[
                   0].text == "Оформление заказа"
        time.sleep(3)
        self.driver.quit()
