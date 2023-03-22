# trello_boards_cards_ui_api

## Автоматизация UI и API-тестов для работы с досками в сервисе Trello (Python)

### Шаги
1. Клонировать проект командой `git clone https://github.com/MarinaAlPu/trello_boards_cards_ui_api.git`
2. Установить все зависимости командой `python -m pip install -r requirements.txt`
3. Запустить тесты:
- запуск только UI-тестов командой `pytest -k test_ui.py`
    - с созданием папки с результатами: `python -m pytest -k test_api.py --alluredir=.\allure-files`
- запуск только API-тестов командой `pytest -k test_api.py`
    - с созданием папки с результатами: `python -m pytest -k test_ui.py --alluredir=.\allure-files`
- запуск всех тестов  командой `pytest`
    - с созданием папки с результатами: `python -m pytest --alluredir=.\allure-files`
4. Сгенерировать отчёт командой `allure generate allure-files -o allure-report`
5. Открыть отчёт командой `allure open allure-report`

### Стек:
- pytest
- selenium
- webdriver manager
- requests
- allure
- configparser
- json

### Структура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работе с API
- ./configuration - провайдер настроек
    - test_config.ini - настройки для тестов
- ./test_data - провайдер тестовых данных
    - test_data.json - тестовые данные

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/cheat-sheet/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore/)
- [Про configparser](https://docs.python.org/3.10/library/configparser.html?highlight=configparser)
- [Про pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/)
