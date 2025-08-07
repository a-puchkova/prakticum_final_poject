# Алина Пучкова, 33-я когорта — Финальный проект. Инженер по тестированию плюс

import send_request

# Функция для проверки
def test_success_get_order_by_track():
    response = send_request.get_new_order_number()
    assert response.status_code == 200
    