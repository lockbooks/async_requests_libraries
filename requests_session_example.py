# улучшаем запросы через requests: делаем их все за один сеанс

from typing import Any
# импортируем модуль time, чтобы можно было засекать время
import time
# импортируем библиотеку requests для запросов
import requests

# пишем основной адрес, куда будем слать запросы
BASE_URL = "https://postman-echo.com"


def fetch_get(session: requests.Session):
    response = session.get(f"{BASE_URL}/get")
    return response.status_code, response.json()


def fetch_post(session: requests.Session) -> Any:
    data_to_post = {"key": "value"}
    response = session.post(f"{BASE_URL}/post", json=data_to_post)
    return response.status_code, response.json()


def fetch_put(session: requests.Session) -> Any:
    data_to_put = {"key": "updated_value"}
    response = session.put(f"{BASE_URL}/put", json=data_to_put)
    return response.status_code, response.json()


def fetch_delete(session: requests.Session) -> Any:
    response = session.delete(f"{BASE_URL}/delete")
    return response.status_code, response.json()


# пишем основную функцию
def main():
    # начинаем отсчёт времени
    start = time.perf_counter()

    # создаём контекстный менеджер с из одного открытого сеанса
    # и выполняем все запросы внутри одного сеанса, не закрывая его
    with requests.Session() as session:
        # выполняем GET-запроc
        status_code, response_json = fetch_get(session)
        # выводим код ответа от сервера и содержимое ответа
        print(f"GET Status Code: {status_code}")
        print(f"GET Response: {response_json}")
        # выполняем POST-запроc
        status_code, response_json = fetch_post(session)
        # выводим код ответа от сервера и содержимое ответа
        print(f"POST Status Code: {status_code}")
        print(f"POST Response: {response_json}")
        # выполняем PUT-запроc
        status_code, response_json = fetch_put(session)
        # выводим код ответа от сервера и содержимое ответа
        print(f"PUT Status Code: {status_code}")
        print(f"PUT Response: {response_json}")
        # выполняем DELETE-запроc
        status_code, response_json = fetch_delete(session)
        # выводим код ответа от сервера и содержимое ответа
        print(f"DELETE Status Code: {status_code}")
        print(f"DELETE Response: {response_json}")

    # останавливаем отсчёт времени и выводим результат,
    # округляя до двух цифр после запятой
    end = time.perf_counter()
    print(f"Time taken: {end - start:.2f} seconds.")

# запускаем основную функцию
main()
