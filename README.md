
---

## Краткое описание

- **Справочник.xlsx** — файл с GUID и названиями зон (может дополняться).
- Скрипт автоматически формирует таблицу посещаемости по всем зонам на заданную дату.
---

## Быстрый старт

1. **Клонируйте репозиторий и создайте виртуальное окружение:**

```sh
https://github.com/makstravel/testovoe_termoland.git
```

```sh
cd testovoe_termoland
```

```sh
    python3 -m venv .venv
```
```sh
    source .venv/bin/activate
```
```sh
    pip install -r requirements.txt
```

3. **Проверьте, что рядом с main.py есть файл `Справочник.xlsx` такого вида:**
    | GUID      | Наименование |
    |-----------|-------------|
    | vFHlJ5Es  | Хаммам      |
    | Gp7yQFaE  | Парная      |
    | Ab7WxWkw  | Бассейн     |

4. **Запустите основной скрипт:**
    ```sh
    python main.py
    ```
    - По умолчанию используется мок-API (mock/mock_border_api.py), что позволяет работать без доступа к серверу.
    - Итоговый файл отчёта будет сохранён как `attendance_<дата>.xlsx`.

---


## Поддержка мок-режима и разработка без API

- Для разработки и тестирования используется модуль `mock/mock_border_api.py`, который эмулирует ответы API.
- Для переключения на настоящий API (при доступности сервера), просто раскомментируйте строку с импортом настоящего класса в main.py:
    ```python
    # from datasource.border_api import BorderAPI
    from mock.mock_border_api import MockBorderAPI
    ```
    → заменить на  
    ```python
    from datasource.border_api import BorderAPI
    # from mock.mock_border_api import MockBorderAPI
    ```
- При необходимости можно расширять мок-ответ любыми данными для тестов.

---



