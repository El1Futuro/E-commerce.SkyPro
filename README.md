# ***Основа для интернет-магазина***

## Описание:

E-commerce — электронная торговля, или электронная коммерция. На данном этапе работы мы подготовим всё для того, чтобы у нас появилось ядро для интернет-магазина. 
В дальнейшем для этого ядра возможно будет реализовать любой интерфейс — от сайта до телеграм-бота.
Ядро будет разработано на Python.
####
**Уже осуществлено:**

- Созданы классы и описаны их инициализации со всеми свойствами.
- Объекты продуктов хранятся в соответствующем атрибуте объекта категории.
- Созданы два атрибута, в которых хранится общее количество категорий и общее количество уникальных продуктов.
- Реализована подгрузка данных по категориям и товарам из файла JSON.


Написаны тестовые функции с использованием библиотеки pytest для существующего кода проекта.
Использованы фикстуры для формирования входных данных для тестов
Написаны тесты с использованием специальных инструментов Mock и patch


***
Покрытие тестами 100% кода, согласно Code coverage.
***

## Установка:

1. Клонируйте [репозиторий](https://github.com/El1Futuro/E-commerce.SkyPro.git):
~~~ 
git clone https://github.com/El1Futuro/E-commerce.SkyPro.git 
~~~
2. Установите зависимости:
```
pip freeze > requirements.txt
```
```
pip install -r requirements.txt
```
## Использование:


****
По окончании клонирования будет открыт проект. Вы можете работать с этим проектом локально и отправлять свои коммиты 
в удаленный клонированный репозиторий.

Также возможно дополнительно проводить тестирование кода при помощи фреймворка Pytest.
Запуск pytest удобнее всего производить из PyCharm.
Команда терминала 
```
pytest
``` 
запускает все тесты текущего каталога. 

Чем выше процент покрытия кода, тем больше вероятность обнаружения ошибок и проблем в программе. 
В pytest для анализа покрытия кода надо поставить библиотеку 
pytest-cov:
```
poetry add --group dev pytest-cov
```
Чтобы запустить тесты с оценкой покрытия, можно воспользоваться следующими командами:
```
pytest --cov
```
 — при активированном виртуальном окружении.
```
poetry run pytest --cov
```
 — через poetry.
```
pytest --cov=src --cov-report=html
```
 — чтобы сгенерировать отчет о покрытии в HTML-формате, где 
src — пакет c модулями, которые тестируем. Отчет будет сгенерирован в папке 
htmlcov и храниться в файле с названием index.html.

## Документация:

Для получения дополнительной информации обратитесь к [документации](https://github.com/El1Futuro/SkyProHomework#/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).
