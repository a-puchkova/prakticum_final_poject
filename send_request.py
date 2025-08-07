import configuration
import requests
import data

def post_new_order(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)

# Вызов функции post_new_order с телом запроса для создания нового заказа из модуля data
response = post_new_order(data.order_body)
track = str(response.json()["track"])

# получение заказа по его номеру GET запрос
def get_new_order_number ():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_NUMBER + track)
