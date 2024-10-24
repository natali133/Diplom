import requests
import allure

json = {
      "X-API-KEY": "9QW7JAM-MRN4VE4-JB01ANP-196GTDJ"
    }


@allure.title("Поиск фильма по id")
@allure.description("Тест проверяет поиск фильма по id")
@allure.severity("критический")
def test_search_by_id():
    with allure.step("отправка запроса "):
        response = requests.get("https://api.kinopoisk.dev/v1.4/movie/535341", headers=json)
    with allure.step("Проверка результата"):
        assert response.status_code == 200

@allure.title("Поиск фильма по названию c цифрами")
@allure.description("Тест проверяет поиск фильма по названию с цифрами")
@allure.severity("критический")
def test_search_by_name():
    with allure.step("отправка запроса "):
        response = requests.get("https://api.kinopoisk.dev/v1.4/movie/search?limit=10&query=1%2B1", headers=json)
    with allure.step("Проверка результата"):
        assert response.status_code == 200

@allure.title("Поиск фильма по названию по жанру")
@allure.description("Тест проверяет поиск фильма по жанру")
@allure.severity("критический")
def test_search_by_ganre():
    with allure.step("отправка запроса "):
        response = requests.get("https://api.kinopoisk.dev/v1/movie/possible-values-by-field?field=type", headers=json)
    with allure.step("Проверка результата"):
        assert response.status_code == 200

@allure.title("Негативный тест- поиск фильма по названию по жанру")
@allure.description("Негативный тест проверяет поиск фильма по жанру")
@allure.severity("критический")
def test_search_by_ganre_negative():
    with allure.step("отправка запроса "):
        response = requests.get("https://api.kinopoisk.dev/v1/movie/possible-values-by-field", headers=json)
    with allure.step("Проверка результата"):
        assert response.status_code == 400

@allure.title("Негативный тест -поиск фильма по id")
@allure.description("Негативный тест -проверяет поиск фильма по id")
@allure.severity("критический")
def test_search_by_id_negative():
    with allure.step("отправка запроса "):
       response = requests.get("https://api.kinopoisk.dev/v1.4/movie/5353414", headers=json)
    with allure.step("Проверка результата"):
       assert response.status_code == 404