# home_work/4_hw/python_trening/task_9_checks.py - `Alexandra Bujor`

class Checks:
    """Базовый класс для проверок с локатором."""
    
    def __init__(self, loc: str):
        """
        Инициализация класса Checks.
        
        Args:
            loc (str): Локатор элемента
        """
        self.loc = loc
    
    def check_text(self) -> str:
        """
        Метод для проверки текста.
        
        Returns:
            str: Локатор элемента
        """
        return self.loc
