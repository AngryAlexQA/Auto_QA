# Домашнее задание №7 - `Александра Бужор`

## 1. Обновляем структуру проекта

Сначала создадим необходимые директории и файлы:

```bash
# Создаем директорию для домашних тестов
mkdir -p demoqa_home/tests/tests_hw

# Создаем файлы
touch demoqa_home/tests/tests_hw/test_check_text.py
touch demoqa_home/components/__init__.py
touch demoqa_home/components/base_component.py
```

## 2. Создаем базовый компонент с методом get_text()

```python
# demoqa_home/components/base_component.py
from selenium.common.exceptions import NoSuchElementException


class BaseComponent:
    """Базовый класс для компонентов страницы."""
    
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
    
    def find_element(self):
        """Поиск элемента компонента."""
        from selenium.webdriver.common.by import By
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)
    
    def get_text(self):
        """Получение текста из элемента."""
        try:
            element = self.find_element()
            return str(element.text)
        except NoSuchElementException:
            return ""
```

## 3. Обновляем base_page.py для работы с компонентами

```python
# demoqa_home/pages/base_page.py
from selenium.webdriver.common.by import By
from components.base_component import BaseComponent


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://demoqa.com/"
    
    def visit(self):
        """Переход на базовую страницу."""
        self.driver.get(self.base_url)
    
    def find_element(self, locator):
        """Поиск элемента на странице."""
        return self.driver.find_element(By.CSS_SELECTOR, locator)
    
    def get_component(self, locator):
        """Создание компонента."""
        return BaseComponent(self.driver, locator)
```

## 4. Создаем page object для DemoQA

```python
# demoqa_home/pages/demoqa_page.py
from pages.base_page import BasePage


class DemoQAPage(BasePage):
    """Класс для работы со страницей DemoQA."""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.footer_locator = "footer span"
        self.center_text_locator = "div.col-12.mt-4.col-md-6"
        self.elements_button_locator = "div.card-body h5"  # Первая карточка "Elements"
    
    def get_footer_text(self):
        """Получает текст из подвала."""
        footer_component = self.get_component(self.footer_locator)
        return footer_component.get_text()
    
    def get_center_text(self):
        """Получает текст из центрального блока."""
        center_component = self.get_component(self.center_text_locator)
        return center_component.get_text()
    
    def click_elements_button(self):
        """Кликает по кнопке Elements."""
        elements_button = self.find_element(self.elements_button_locator)
        elements_button.click()
```

## 5. Реализуем тесты в test_check_text.py

```python
# demoqa_home/tests/tests_hw/test_check_text.py
import pytest
from pages.demoqa_page import DemoQAPage


class TestDemoQAText:
    """Тесты для проверки текста на сайте DemoQA."""
    
    def test_check_footer_text(self, driver):
        """
        Тест проверки текста в подвале.
        a. перейти на страницу 'https://demoqa.com/'
        b. проверить что текст в подвале == ‘© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.’
        """
        # Переходим на страницу
        demoqa_page = DemoQAPage(driver)
        demoqa_page.visit()
        
        # Получаем текст из подвала
        footer_text = demoqa_page.get_footer_text()
        
        # Проверяем соответствие текста
        expected_text = "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."
        assert footer_text == expected_text, f"Текст в подвале не совпадает. Ожидалось: '{expected_text}', Получено: '{footer_text}'"
    
    def test_check_center_text_after_navigation(self, driver):
        """
        Тест проверки текста после перехода на страницу Elements.
        a. перейти на страницу 'https://demoqa.com/'
        b. через кнопку перейти на страницу 'https://demoqa.com/elements'
        c. проверить что текст по центру == 'Please select an item from left to start practice.'
        """
        # Переходим на главную страницу
        demoqa_page = DemoQAPage(driver)
        demoqa_page.visit()
        
        # Кликаем по кнопке Elements
        demoqa_page.click_elements_button()
        
        # Ждем загрузки страницы (можно добавить явное ожидание)
        driver.implicitly_wait(3)
        
        # Получаем текст из центрального блока
        center_text = demoqa_page.get_center_text()
        
        # Проверяем соответствие текста
        expected_text = "Please select an item from left to start practice."
        assert center_text == expected_text, f"Текст по центру не совпадает. Ожидалось: '{expected_text}', Получено: '{center_text}'"
```

## 6. Обновляем conftest.py для корректной работы

```python
# demoqa_home/conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации и закрытия драйвера."""
    # Настройка драйвера
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    
    yield driver
    
    # Закрытие драйвера после теста
    driver.quit()
```

## 7. Запуск тестов

```bash
# Переходим в директорию проекта
cd demoqa_home

# Запускаем домашние тесты
pytest tests/tests_hw/test_check_text.py -v

# Запуск с подробным выводом
pytest tests/tests_hw/test_check_text.py -v --tb=short
```

## 📁 Итоговая структура проекта:

```
demoqa_home/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── swag_labs.py
│   └── demoqa_page.py
├── tests/
│   ├── __init__.py
│   ├── test_check_swag.py
│   └── tests_hw/
│       ├── __init__.py
│       └── test_check_text.py
├── components/
│   ├── __init__.py
│   └── base_component.py
├── conftest.py
├── .gitignore
├── readme.md
└── requirements.txt
```

## 🔧 Особенности реализации:

1. **Компонентный подход**: Создан базовый класс `BaseComponent` с методом `get_text()`
2. **Переиспользование кода**: Методы поиска и работы с текстом вынесены в компоненты
3. **Чистая архитектура**: Разделение page objects и тестов
4. **Обработка ошибок**: Метод `get_text()` возвращает пустую строку при отсутствии элемента
5. **Гибкость**: Легко добавлять новые компоненты и страницы
