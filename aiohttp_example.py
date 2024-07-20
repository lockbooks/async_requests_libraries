# импортируем библиотеку асинхронных запросов aiohttp
import aiohttp
# подключаем модуль для асинхронного кода asyncio
import asyncio
# импортируем модуль time, чтобы можно было засекать время
import time

# пишем основной адрес, куда будем слать запросы
BASE_URL = "https://postman-echo.com"


# пишем функцию GET-запроса
async def fetch_get(session: aiohttp.ClientSession):
    # открываем сеанс, отправляем запрос
    async with session.get(f"{BASE_URL}/get") as response:
        # возвращаем ответ от сервера
        return await response.json()


# пишем функцию POST-запроса
async def fetch_post(session: aiohttp.ClientSession):
    # создаём запись, которую хотим отправить
    data_to_post = {"key": "value"}
    # открываем сеанс, отправляем запрос
    async with session.post(f"{BASE_URL}/post", json=data_to_post) as response:
        # возвращаем ответ от сервера
        return await response.json()


# пишем функцию PUT-запроса
async def fetch_put(session: aiohttp.ClientSession):
    # создаём запись, на которую хотим заменить существующую запись
    data_to_put = {"key": "updated_value"}
    # открываем сеанс, отправляем запрос
    async with session.put(f"{BASE_URL}/put", json=data_to_put) as response:
        # возвращаем ответ от сервера
        return await response.json()


# пишем функцию DELETE-запроса
async def fetch_delete(session: aiohttp.ClientSession):
    # открываем сеанс, отправляем запрос
    async with session.delete(f"{BASE_URL}/delete") as response:
        # возвращаем ответ от сервера
        return await response.json()


# пишем основную функцию
async def main():
    # начинаем отсчёт времени
    start = time.perf_counter()

    # собираем все наши запросы и запускаем все почти одновременно: все асинхронные
    # функции запускаются друг за другом, не дожидаясь выполнения прудыдущей
    async with aiohttp.ClientSession() as session:
        # создаём список, куда последовательно сохраняем все ответы
        results = await asyncio.gather(
            # перечисляем асинхронные функции, которые нужно запустить
            fetch_get(session),
            fetch_post(session),
            fetch_put(session),
            fetch_delete(session)
        )

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
