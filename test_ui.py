import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("Поиск фильма по названию c цифрами")
@allure.description("Тест проверяет поиск фильма по названию состоящему из цифр и символа")
@allure.severity("критический")
def test_by_valid_symbol(chrome_browser):
    chrome_browser.get("https://www.kinopoisk.ru/")
    chrome_browser.find_element(By.NAME, "kp_query").send_keys("1+1")
    chrome_browser.find_element(By.ID, "suggest-item-film-535341").click()
    assert (chrome_browser.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "1+1 (2011)"


@allure.title("Негативный тест на ввод некорретных данных в поле название фильма ")
@allure.description("Негативный тест  по поиску  фильма по названию состоящему из  символов")
@allure.severity("критический")
def test_by_invalid_symbol(chrome_browser):
    chrome_browser.get("https://www.kinopoisk.ru/")
    chrome_browser.find_element(By.NAME, "kp_query").send_keys("%")
    assert chrome_browser.find_element(By.XPATH,
                                       "//*[contains(@class, 'emptySuggest')]").text == "По вашему запросу ничего не найдено"

@allure.title("Поиск фильма по названию на кириллице")
@allure.description("Поиск фильма по названию на кириллице")
@allure.severity("критический")
def test_search_by_russian_name(chrome_browser):
    chrome_browser.get("https://www.kinopoisk.ru/")
    chrome_browser.find_element(By.NAME, "kp_query").send_keys("Зеленая миля")
    chrome_browser.find_element(By.ID, "suggest-item-film-435").click()
    assert chrome_browser.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "Зеленая миля (1999)"

@allure.title("Поиск фильма по названию на латинице")
@allure.description("Поиск фильма по названию на латинице")
@allure.severity("критический")
def test_search_by_english_name(chrome_browser):
    chrome_browser.get("https://www.kinopoisk.ru/")
    chrome_browser.find_element(By.NAME, "kp_query").send_keys("The Green Mile")
    chrome_browser.find_element(By.ID, "suggest-item-film-435").click()
    assert chrome_browser.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "The Green Mile(1999)"
