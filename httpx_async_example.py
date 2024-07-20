# подключаем модуль для асинхронного кода asyncio
import asyncio
# импортируем модуль time, чтобы можно было засекать время
import time
# импортируем библиотеку  запросов httpx
import httpx

# пишем основной адрес, куда будем слать запросы
BASE_URL = "https://postman-echo.com"


# пишем функцию GET-запроса
async def fetch_get(client: httpx.AsyncClient):
    # объявляем переменную, в которой отправляем асинхронный GET-запрос на нужный адрес
    response = await client.get(f"{BASE_URL}/get")
    # возвращаем ответ с сервера в формате JSON
    return response.json()


# пишем функцию POST-запроса
async def fetch_post(client: httpx.AsyncClient):
    # объявляем переменную и указываем, что нужно добавить
    data_to_post = {"key": "value"}
    # объявляем переменную, в которой отправляем асинхронный POST-запрос на нужный адрес
    response = await client.post(f"{BASE_URL}/post", json=data_to_post)
    # возвращаем ответ с сервера в формате JSON
    return response.json()


# пишем функцию PUT-запроса
async def fetch_put(client: httpx.AsyncClient):
    # объявляем переменную и указываем, что нужно обновить
    data_to_put = {"key": "updated_value"}
    # объявляем переменную, в которой отправляем асинхронный PUT-запрос на нужный адрес
    response = await client.put(f"{BASE_URL}/put", json=data_to_put)
    # возвращаем ответ с сервера в формате JSON
    return response.json()


# пишем функцию DELETE-запроса
async def fetch_delete(client: httpx.AsyncClient):
    # объявляем переменную, в которой отправляем асинхронный DELETE-запрос на нужный адрес
    response = await client.delete(f"{BASE_URL}/delete")
    # возвращаем ответ с сервера в формате JSON
    return response.json()


# пишем основную функцию
async def main():
    # начинаем отсчёт времени
    start = time.perf_counter()

    # собираем все наши запросы и запускаем все почти одновременно: все асинхронные
    # функции запускаются друг за другом, не дожидаясь выполнения прудыдущей
    async with httpx.AsyncClient() as client:
        tasks = [
            fetch_get(client),
            fetch_post(client),
            fetch_put(client),
            fetch_delete(client),
        ]
        # создаём список, куда последовательно сохраняем все ответы
        results = await asyncio.gather(*tasks)

    # выводим результаты каждого запроса на экран
    print("GET:", results[0])
    print("POST:", results[1])
    print("PUT:", results[2])
    print("DELETE:", results[3])

    # останавливаем отсчёт времени и выводим результат,
    # округляя до двух цифр после запятой
    end = time.perf_counter()
    print(f"Time taken: {end - start:.2f} seconds.")


# запускаем основную функцию
asyncio.run(main())
