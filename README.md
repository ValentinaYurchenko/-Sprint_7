# Финальный проект 7 спринта

## Описание тестов: 
* test_create_courier.py - проверка создание курьера
* test_login_courier.py - проверка авторизации курьера 
* test_create_order.py - проверка создания заказа
* test_order_list.py - проверка полного списка заказов
* test_delete_courier.py - проверка удаления курьера

## Перед работой с репозиторием
* Установите зависимости
``` shell
pip3 install -r requirements.txt
```
* Запустить все тесты из директории tests
```shell
pytest tests --alluredir=allure_results
```
* Посмотреть отчет в веб версии пройденного прогона
``` shell
allure serve allure_results
```