# home_work/4_hw/car.py - `Alexandra Bujor`

class Car:
    """Класс для представления автомобиля."""
    
    def __init__(self, color: str = "неизвестен", car_type: str = "неизвестен", year: int = 0):
        """
        Конструктор класса Car.
        
        Args:
            color (str): Цвет автомобиля
            car_type (str): Тип автомобиля
            year (int): Год выпуска
        """
        self.color = color
        self.type = car_type
        self.year = year
    
    def start_engine(self) -> str:
        """Запуск автомобиля."""
        return "Автомобиль заведен"
    
    def stop_engine(self) -> str:
        """Остановка автомобиля."""
        return "Автомобиль заглушен"
    
    def set_year(self, year: int) -> None:
        """Присвоение года выпуска."""
        self.year = year
        print(f"Год выпуска установлен: {self.year}")
    
    def set_type(self, car_type: str) -> None:
        """Присвоение типа автомобиля."""
        self.type = car_type
        print(f"Тип автомобиля установлен: {self.type}")
    
    def set_color(self, color: str) -> None:
        """Присвоение цвета автомобиля."""
        self.color = color
        print(f"Цвет автомобиля установлен: {self.color}")
    
    def __str__(self) -> str:
        """Строковое представление автомобиля."""
        return f"Автомобиль: {self.color} {self.type} {self.year} года"


# Демонстрация работы класса Car
if __name__ == "__main__":
    print("=== Демонстрация класса Car ===")
    
    # Создаем автомобиль
    my_car = Car("красный", "седан", 2020)
    print(my_car)
    
    # Используем методы
    print(my_car.start_engine())
    print(my_car.stop_engine())
    
    # Меняем свойства
    my_car.set_year(2022)
    my_car.set_type("хэтчбек")
    my_car.set_color("синий")
    
    print(my_car)
