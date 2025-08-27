# home_work/4_hw/4_hw.py - `Alexandra Bujor`

# Задача 1: Класс прямоугольника
class Rectangle:
    """Класс для представления прямоугольника."""
    
    def __init__(self, width: float, height: float):
        """
        Инициализация прямоугольника.
        
        Args:
            width (float): Ширина прямоугольника
            height (float): Высота прямоугольника
        """
        self.width = width
        self.height = height
    
    def calculate_area(self) -> float:
        """Расчет площади прямоугольника."""
        return self.width * self.height
    
    def calculate_perimeter(self) -> float:
        """Расчет периметра прямоугольника."""
        return 2 * (self.width + self.height)


# Задача 2: Класс Math
class Math:
    """Класс для математических операций."""
    
    def __init__(self, a: float, b: float):
        """
        Инициализация математического калькулятора.
        
        Args:
            a (float): Первое число
            b (float): Второе число
        """
        self.a = a
        self.b = b
    
    def addition(self) -> float:
        """Сложение чисел a и b."""
        result = self.a + self.b
        print(f"Сложение: {self.a} + {self.b} = {result}")
        return result
    
    def multiplication(self) -> float:
        """Умножение чисел a и b."""
        result = self.a * self.b
        print(f"Умножение: {self.a} * {self.b} = {result}")
        return result
    
    def division(self) -> float:
        """Деление числа a на b."""
        if self.b == 0:
            print("Ошибка: деление на ноль!")
            return float('inf')  # Возвращаем бесконечность при делении на ноль
        result = self.a / self.b
        print(f"Деление: {self.a} / {self.b} = {result}")
        return result
    
    def subtraction(self) -> float:
        """Вычитание числа b из a."""
        result = self.a - self.b
        print(f"Вычитание: {self.a} - {self.b} = {result}")
        return result


# Задача 3: Класс для кнопок DemoQA
class DemoQAButton:
    """Класс для представления кнопок на сайте DemoQA."""
    
    def __init__(self, button_text: str):
        """
        Инициализация кнопки.
        
        Args:
            button_text (str): Текст кнопки
        """
        self.button_text = button_text
        self.type = "Кнопка"
        self.locator = ""  # Локатор по умолчанию пустая строка
    
    def click(self) -> str:
        """Метод для клика по кнопке."""
        return f"Клик по кнопке {self.button_text}"


# Демонстрация работы всех классов
if __name__ == "__main__":
    print("=== Задача 1: Прямоугольники ===")
    # Создаем 3 объекта прямоугольников
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(3.5, 7.2)
    rect3 = Rectangle(8, 8)  # Квадрат
    
    rectangles = [rect1, rect2, rect3]
    
    for i, rect in enumerate(rectangles, 1):
        area = rect.calculate_area()
        perimeter = rect.calculate_perimeter()
        print(f"Прямоугольник {i}: {rect.width}x{rect.height}")
        print(f"  Площадь: {area}")
        print(f"  Периметр: {perimeter}")
    
    print("\n=== Задача 2: Математические операции ===")
    math_ops = Math(10, 5)
    math_ops.addition()
    math_ops.subtraction()
    math_ops.multiplication()
    math_ops.division()
    
    # Тест с делением на ноль
    math_zero = Math(10, 0)
    math_zero.division()
    
    print("\n=== Задача 3: Кнопки DemoQA ===")
    # Создаем объекты для кнопок 2-го уровня вложенности
    buttons_data = [
        "Text Box",
        "Check Box", 
        "Radio Button",
        "Web Tables",
        "Buttons",
        "Links",
        "Broken Links - Images",
        "Upload and Download",
        "Dynamic Properties"
    ]
    
    # Создаем объекты кнопок
    demoqa_buttons = [DemoQAButton(text) for text in buttons_data]
    
    # Выводим текст для каждой кнопки и имитируем клик
    for button in demoqa_buttons:
        print(f"Текст кнопки: {button.button_text}")
        print(f"Тип: {button.type}")
        print(f"Локатор: '{button.locator}'")
        print(button.click())
        print("-" * 30)
