# Домашнее задание №8 - `Александра Бужор`

## 1. Создаем page object для Accordion

```python
# demoqa_home/pages/accordion.py
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AccordionPage(BasePage):
    """Класс для работы со страницей Accordion."""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/accordian"
        
        # Локаторы элементов
        self.section1_heading = "#section1Heading"
        self.section1_content = "#section1Content > p"
        self.section2_content_p1 = "#section2Content > p:nth-child(1)"
        self.section2_content_p2 = "#section2Content > p:nth-child(2)"
        self.section3_content = "#section3Content > p"
    
    def visit(self):
        """Переход на страницу аккордеона."""
        self.driver.get(self.url)
    
    def click_section1_heading(self):
        """Клик по заголовку первой секции."""
        element = self.find_element(self.section1_heading)
        element.click()
    
    def is_section1_content_visible(self):
        """Проверяет видимость контента первой секции."""
        try:
            element = self.find_element(self.section1_content)
            return element.is_displayed()
        except:
            return False
    
    def is_section2_content_p1_visible(self):
        """Проверяет видимость первого параграфа второй секции."""
        try:
            element = self.find_element(self.section2_content_p1)
            return element.is_displayed()
        except:
            return False
    
    def is_section2_content_p2_visible(self):
        """Проверяет видимость второго параграфа второй секции."""
        try:
            element = self.find_element(self.section2_content_p2)
            return element.is_displayed()
        except:
            return False
    
    def is_section3_content_visible(self):
        """Проверяет видимость контента третьей секции."""
        try:
            element = self.find_element(self.section3_content)
            return element.is_displayed()
        except:
            return False
```

## 2. Создаем тестовый файл

```python
# demoqa_home/tests/tests_hw/test_visible_hw.py
import time
import pytest
from pages.accordion import AccordionPage


class TestAccordionVisibility:
    """Тесты для проверки видимости элементов аккордеона."""
    
    def test_visible_accordion(self, driver):
        """
        Тест проверки видимости/скрытия контента аккордеона.
        
        Steps:
        i. перейти на страницу https://demoqa.com/accordian
        ii. проверьте, что элемент #section1Content > p виден
        iii. кликните на #section1Heading
        iv. После клика добавьте time.sleep(2)
        v. проверьте, что элемент #section1Content > p НЕ виден
        """
        # i. Переходим на страницу
        accordion_page = AccordionPage(driver)
        accordion_page.visit()
        
        # ii. Проверяем, что контент первой секции виден
        assert accordion_page.is_section1_content_visible() == True, \
            "Контент первой секции должен быть виден по умолчанию"
        
        # iii. Кликаем по заголовку первой секции
        accordion_page.click_section1_heading()
        
        # iv. Ждем 2 секунды для анимации
        time.sleep(2)
        
        # v. Проверяем, что контент первой секции НЕ виден
        assert accordion_page.is_section1_content_visible() == False, \
            "Контент первой секции должен быть скрыт после клика"
    
    def test_visible_accordion_default(self, driver):
        """
        Тест проверки скрытых элементов по умолчанию.
        
        Steps:
        i. перейдите на страницу https://demoqa.com/accordian
        ii. проверьте, что следующие элементы по умолчанию скрыты:
            - #section2Content > p:nth-child(1)
            - #section2Content > p:nth-child(2)
            - #section3Content > p
        """
        # i. Переходим на страницу
        accordion_page = AccordionPage(driver)
        accordion_page.visit()
        
        # ii. Проверяем, что элементы скрыты по умолчанию
        assert accordion_page.is_section2_content_p1_visible() == False, \
            "Первый параграф второй секции должен быть скрыт по умолчанию"
        
        assert accordion_page.is_section2_content_p2_visible() == False, \
            "Второй параграф второй секции должен быть скрыт по умолчанию"
        
        assert accordion_page.is_section3_content_visible() == False, \
            "Контент третьей секции должен быть скрыт по умолчанию"
```

## 3. Обновляем базовый класс (добавляем метод is_visible)

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

# Запускаем тесты для аккордеона
pytest tests/tests_hw/test_visible_hw.py -v

# Запуск с подробным выводом
pytest tests/tests_hw/test_visible_hw.py -v --tb=short
```

## 📁 Итоговая структура проекта:

```
demoqa_home/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── swag_labs.py
│   ├── demoqa_page.py
│   └── accordion.py          # ← НОВЫЙ ФАЙЛ
├── tests/
│   ├── __init__.py
│   ├── test_check_swag.py
│   └── tests_hw/
│       ├── __init__.py
│       ├── test_check_text.py
│       └── test_visible_hw.py  # ← НОВЫЙ ФАЙЛ
├── components/
│   ├── __init__.py
│   └── base_component.py
├── conftest.py
├── .gitignore
├── readme.md
└── requirements.txt
```

## 🔧 Особенности реализации:

1. **Специализированный Page Object**: Класс `AccordionPage` содержит все локаторы и методы для работы с аккордеоном
2. **Методы проверки видимости**: Каждый элемент имеет свой метод проверки видимости с обработкой исключений
3. **Четкое разделение тестов**: Два отдельных теста для разных сценариев
4. **Обработка анимации**: Использование `time.sleep(2)` для ожидания завершения анимации аккордеона
5. **Негативные проверки**: Проверка того, что элементы НЕ видны (с отрицанием в assertions)
