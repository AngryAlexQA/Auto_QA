# Домашнее задание №6 - `Александра Бужор`
## Алгоритм построения архитектуры проекта demoqa_home:

## 1. Создание структуры проекта

```bash
# Создаем директории
mkdir -p demoqa_home/{pages,tests,components}
cd demoqa_home

# Копируем драйвер (предполагается, что chromedriver уже скачан)
# Создаем необходимые файлы
touch .gitignore readme.md conftest.py

# Инициализируем git и устанавливаем зависимости
git init
pip install pytest selenium
pip freeze > requirements.txt
```

## 2. Файл `.gitignore`

```gitignore
/venv
.idea
*.pytest_cache
__pycache__/
*.pyc
chromedriver
chromedriver.exe
.DS_Store
```

## 3. Файл `conftest.py`

```python
# demoqa_home/conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    # Настройка драйвера
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    
    yield driver
    
    # Закрытие драйвера после теста
    driver.quit()
```

## 4. Реализация `base_page.py`

```python
# demoqa_home/pages/base_page.py
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.saucedemo.com/"
    
    def visit(self):
        """Переход на базовую страницу."""
        self.driver.get(self.base_url)
    
    def find_element(self, locator):
        """Поиск элемента на странице."""
        return self.driver.find_element(By.CSS_SELECTOR, locator)
```

## 5. Реализация `swag_labs.py`

```python
# demoqa_home/pages/swag_labs.py
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage


class SwagLabs(BasePage):
    """Класс для работы со страницей Swag Labs."""
    
    def exist_icon(self):
        """Проверяет наличие иконки на странице."""
        try:
            self.find_element(locator='div.login_logo')
            return True
        except NoSuchElementException:
            return False
    
    def exist_username_field(self):
        """Проверяет наличие поля имени пользователя."""
        try:
            self.find_element(locator='input[data-test="username"]')
            return True
        except NoSuchElementException:
            return False
    
    def exist_password_field(self):
        """Проверяет наличие поля пароля."""
        try:
            self.find_element(locator='input[data-test="password"]')
            return True
        except NoSuchElementException:
            return False
```

## 6. Реализация тестов `test_check_swag.py`

```python
# demoqa_home/tests/test_check_swag.py
import pytest
from pages.swag_labs import SwagLabs


class TestSwagLabs:
    """Тесты для страницы Swag Labs."""
    
    def test_check_icon(self, driver):
        """Тест проверки наличия иконки."""
        # Переходим на страницу
        swag_page = SwagLabs(driver)
        swag_page.visit()
        
        # Проверяем наличие иконки
        assert swag_page.exist_icon() == True, "Иконка не найдена на странице"
    
    def test_check_username_field(self, driver):
        """Тест проверки наличия поля имени пользователя."""
        # Переходим на страницу
        swag_page = SwagLabs(driver)
        swag_page.visit()
        
        # Проверяем наличие поля имени
        assert swag_page.exist_username_field() == True, "Поле имени пользователя не найдено"
    
    def test_check_password_field(self, driver):
        """Тест проверки наличия поля пароля."""
        # Переходим на страницу
        swag_page = SwagLabs(driver)
        swag_page.visit()
        
        # Проверяем наличие поля пароля
        assert swag_page.exist_password_field() == True, "Поле пароля не найдено"
```

## 7. Файл `readme.md`

```markdown
# DemoQA Home Project

Проект для автоматизации тестирования демо-сайта Swag Labs.

## Структура проекта


demoqa_home/
├── pages/           # Page Objects
├── tests/           # Тесты
├── components/      # Компоненты
├── conftest.py     # Фикстуры pytest
├── requirements.txt # Зависимости
└── .gitignore      # Исключения Git
```

## Установка и запуск

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Запустите тесты:
```bash
pytest tests/test_check_swag.py -v
```

## Тесты

- Проверка наличия иконки на странице
- Проверка наличия поля имени пользователя
- Проверка наличия поля пароля
```

## 8. Запуск тестов

```bash
# Переходим в директорию проекта
cd demoqa_home

# Запускаем все тесты
pytest tests/test_check_swag.py -v

# Запуск с выводом подробной информации
pytest tests/test_check_swag.py -v --tb=short
```

## 📁 Итоговая структура проекта:

```
demoqa_home/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   └── swag_labs.py
├── tests/
│   ├── __init__.py
│   └── test_check_swag.py
├── components/
│   └── __init__.py
├── conftest.py
├── .gitignore
├── readme.md
└── requirements.txt
```
