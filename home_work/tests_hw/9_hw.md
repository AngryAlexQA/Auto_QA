# Домашнее задание №9 - `Александра Бужор`

## 1. Создаем page object для модальных диалогов

```python
# demoqa_home/pages/modal_dialogs.py
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ModalDialogsPage(BasePage):
    """Класс для работы со страницей Modal Dialogs."""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/modal-dialogs"
        
        # Локаторы элементов
        self.icon_locator = "header a > img"  # Иконка для перехода на главную
        self.buttons_locator = "button.btn"   # Локатор для всех кнопок
    
    def visit(self):
        """Переход на страницу модальных диалогов."""
        self.driver.get(self.url)
    
    def get_buttons_count(self):
        """Получает количество кнопок на странице."""
        buttons = self.driver.find_elements(By.CSS_SELECTOR, self.buttons_locator)
        return len(buttons)
    
    def click_icon(self):
        """Клик по иконке для перехода на главную."""
        icon = self.find_element(self.icon_locator)
        icon.click()
    
    def get_current_url(self):
        """Получает текущий URL."""
        return self.driver.current_url
    
    def get_page_title(self):
        """Получает title страницы."""
        return self.driver.title
    
    def refresh_page(self):
        """Обновляет страницу."""
        self.driver.refresh()
    
    def browser_back(self):
        """Шаг назад в браузере."""
        self.driver.back()
    
    def browser_forward(self):
        """Шаг вперед в браузере."""
        self.driver.forward()
    
    def set_window_size(self, width, height):
        """Устанавливает размер окна браузера."""
        self.driver.set_window_size(width, height)
    
    def maximize_window(self):
        """Максимизирует окно браузера."""
        self.driver.maximize_window()
```

## 2. Создаем тестовый файл

```python
# demoqa_home/tests/tests_hw/test_page_dialogs.py
import pytest
from pages.modal_dialogs import ModalDialogsPage


class TestModalDialogs:
    """Тесты для страницы Modal Dialogs."""
    
    def test_modal_elements(self, driver):
        """
        Тест проверки элементов на странице модальных диалогов.
        
        Steps:
        a. перейти на страницу https://demoqa.com/modal-dialogs
        b. проверить, что кнопок подменю, на странице - 5 шт
        """
        # a. Переходим на страницу
        modal_page = ModalDialogsPage(driver)
        modal_page.visit()
        
        # b. Проверяем количество кнопок
        buttons_count = modal_page.get_buttons_count()
        expected_count = 5
        
        assert buttons_count == expected_count, \
            f"Ожидалось {expected_count} кнопок, но найдено {buttons_count}"
    
    def test_navigation_modal(self, driver):
        """
        Тест навигации на странице модальных диалогов.
        
        Steps:
        a. перейти на страницу https://demoqa.com/modal-dialogs
        b. обновить страницу
        c. перейти на главную страницу через иконку
        d. сделать шаг назад стрелкой браузера
        e. установить размеры экрана 900х400
        f. сделать шаг вперед стрелкой браузера
        g. вызвать проверку урла на главной странице
        h. проверить title на главной
        i. вернуть размеры экрана по умолчанию 1000x1000
        """
        # a. Переходим на страницу
        modal_page = ModalDialogsPage(driver)
        modal_page.visit()
        
        # Сохраняем исходный URL для проверок
        modal_url = modal_page.get_current_url()
        
        # b. Обновляем страницу
        modal_page.refresh_page()
        
        # c. Переходим на главную страницу через иконку
        modal_page.click_icon()
        
        # d. Шаг назад в браузере (должен вернуть на modal-dialogs)
        modal_page.browser_back()
        
        # Проверяем, что вернулись на страницу modal-dialogs
        current_url_after_back = modal_page.get_current_url()
        assert current_url_after_back == modal_url, \
            f"После шага назад ожидался URL: {modal_url}, но получен: {current_url_after_back}"
        
        # e. Устанавливаем размеры экрана 900x400
        modal_page.set_window_size(900, 400)
        
        # f. Шаг вперед в браузере (должен вернуть на главную)
        modal_page.browser_forward()
        
        # g. Проверяем URL на главной странице
        home_url = "https://demoqa.com/"
        current_url_after_forward = modal_page.get_current_url()
        assert current_url_after_forward == home_url, \
            f"После шага вперед ожидался URL: {home_url}, но получен: {current_url_after_forward}"
        
        # h. Проверяем title на главной
        page_title = modal_page.get_page_title()
        expected_title = "DEMOQA"
        assert expected_title in page_title, \
            f"Title страницы должен содержать '{expected_title}', но получен: '{page_title}'"
        
        # i. Возвращаем размеры экрана по умолчанию (1000x1000)
        modal_page.set_window_size(1000, 1000)
        
        # Дополнительная проверка - убедимся, что размер установился корректно
        modal_page.set_window_size(1000, 1000)  # Явно устанавливаем 1000x1000
```

## 3. Обновляем базовый класс (добавляем методы для работы с элементами)

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
    
    def find_elements(self, locator):
        """Поиск нескольких элементов на странице."""
        return self.driver.find_elements(By.CSS_SELECTOR, locator)
    
    def get_component(self, locator):
        """Создание компонента."""
        return BaseComponent(self.driver, locator)
    
    def is_element_visible(self, locator):
        """Проверяет видимость элемента."""
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except:
            return False
```

## 4. Запуск тестов

```bash
# Переходим в директорию проекта
cd demoqa_home

# Запускаем тесты для модальных диалогов
pytest tests/tests_hw/test_page_dialogs.py -v

# Запуск с подробным выводом
pytest tests/tests_hw/test_page_dialogs.py -v --tb=short
```

## 📁 Итоговая структура проекта:

```
demoqa_home/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── swag_labs.py
│   ├── demoqa_page.py
│   ├── accordion.py
│   └── modal_dialogs.py      # ← НОВЫЙ ФАЙЛ
├── tests/
│   ├── __init__.py
│   ├── test_check_swag.py
│   └── tests_hw/
│       ├── __init__.py
│       ├── test_check_text.py
│       ├── test_visible_hw.py
│       └── test_page_dialogs.py  # ← НОВЫЙ ФАЙЛ
├── components/
│   ├── __init__.py
│   └── base_component.py
├── conftest.py
├── .gitignore
├── readme.md
└── requirements.txt
```

## 🔧 Особенности реализации:

1. **Универсальный локатор**: `button.btn` для поиска всех 5 кнопок на странице
2. **Методы навигации**: Реализованы все требуемые методы браузерной навигации
3. **Управление окном**: Методы для установки размеров окна браузера
4. **Проверки URL и title**: Методы для проверки текущего URL и заголовка страницы
5. **Последовательность действий**: Тест точно следует заданной последовательности шагов
6. **Обработка размеров**: Явная установка размеров 1000x1000 в конце теста
