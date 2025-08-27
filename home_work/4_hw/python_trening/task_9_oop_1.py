# home_work/4_hw/python_trening/task_9_oop_1.py - `Alexandra Bujor`

from task_9_checks import Checks

class Buttons(Checks):
    """Класс для кнопок."""
    
    def __init__(self, loc: str):
        super().__init__(loc)
    
    def click(self) -> str:
        return f"Клик по кнопке с локатором {self.loc}"


class InputFields(Checks):
    """Класс для полей ввода."""
    
    def __init__(self, loc: str):
        super().__init__(loc)
    
    def input_text(self, text: str) -> str:
        return f"Ввод текста '{text}' в поле с локатором {self.loc}"


class Text(Checks):
    """Класс для текстовых элементов."""
    
    def __init__(self, loc: str):
        super().__init__(loc)
    
    def get_text(self) -> str:
        return f"Получение текста элемента с локатором {self.loc}"


class Title(Checks):
    """Класс для заголовков."""
    
    def __init__(self, loc: str):
        super().__init__(loc)
    
    def get_title(self) -> str:
        return f"Получение заголовка элемента с локатором {self.loc}"


# Демонстрация работы классов
if __name__ == "__main__":
    print("=== Демонстрация наследования от класса Checks ===")
    
    # Создаем объекты классов
    button = Buttons("//button[@id='submit']")
    input_field = InputFields("//input[@name='username']")
    text_element = Text("//div[@class='content']")
    title_element = Title("//h1[@class='main-title']")
    
    # Вызываем метод check_text() для каждого объекта
    elements = [button, input_field, text_element, title_element]
    element_names = ["Buttons", "InputFields", "Text", "Title"]
    
    for name, element in zip(element_names, elements):
        result = element.check_text()
        print(f"{name}.check_text() = '{result}'")
