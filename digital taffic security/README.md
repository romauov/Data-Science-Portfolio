# Определение злонамеренного трафика
Модель для автоматизация выявления аномального и злонамеренного трафика, которая будет классифицировать трафик на нормальный и злонамеренный.
## Стек
pandas - numpy - SMOTETomek - catboost - optuna - Flask - Docker - Locust
## Состав проекта:
| **Название файла**  | **Содержание**                            |
|:--------------------|:------------------------------------------|
| TRAFF.ipynb         | ноутбук с построением модели              |
| TRAFF.html          | html-версия ноутбука |
| cb_model.cbm        | обученная модель                          |
| app.py              | Flask-приложение для прогнозов            |
| Dockerfile          | докерфайл                                 |
| measure_response.py | скрипт для тестирования приложения        |
| app_test.py         | скрипт для тестирования с помощью Locust  |
| requirements.txt    | requirements.txt                          |