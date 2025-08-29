# home_work/5_hw/5_hw.py - `Alexandra Bujor`

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def sauce_demo_test():
    """
    Функция для тестирования страницы Saucedemo.
    Находит элементы и выводит результат в консоль.
    """
    try:
        # Инициализация драйвера
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        
        # a. Переход на страницу
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(2)  # Небольшая пауза для загрузки страницы
        
        # b. Поиск элементов
        # i. Текстовое поле username
        username_field = driver.find_element(By.ID, "user-name")
        
        # ii. Текстовое поле password
        password_field = driver.find_element(By.ID, "password")
        
        # iii. Кнопка submit
        submit_button = driver.find_element(By.ID, "login-button")
        
        # c. Проверка условий
        if username_field and password_field and submit_button:
            print("✓ Элементы найдены")
            print(f"  - Username field: {username_field.is_displayed()}")
            print(f"  - Password field: {password_field.is_displayed()}")
            print(f"  - Submit button: {submit_button.is_displayed()}")
        else:
            print("✗ Не все элементы найдены")
        
        # Закрытие браузера
        driver.quit()
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        if 'driver' in locals():
            driver.quit()

def css_trainer_info():
    """
    Информация о решении CSS заданий.
    """
    print("\n" + "="*50)
    print("CSS TRAINER (https://flukeout.github.io/)")
    print("="*50)
    print("Решены задания 1-14 включительно:")
    print("1. plate")
    print("2. bento")
    print("3. #fancy")
    print("4. plate apple")
    print("5. #fancy pickle")
    print("6. .small")
    print("7. orange.small")
    print("8. bento orange.small")
    print("9. plate, bento")
    print("10. *")
    print("11. plate *")
    print("12. plate + apple")
    print("13. bento ~ pickle")
    print("14. plate > apple")
    print("\nСкриншоты выполненных заданий приложены отдельно.")

def xpath_trainer_info():
    """
    Информация о решении XPATH заданий.
    """
    print("\n" + "="*50)
    print("XPATH TRAINER (https://topswagcode.com/xpath/)")
    print("="*50)
    print("Решены задания 1-14 включительно:")
    print("1. //button")
    print("2. //div")
    print("3. //div[@id='superman']")
    print("4. //div[@class='hero']")
    print("5. //div[@class='hero' and @id='superman']")
    print("6. //div[contains(@class, 'hero')]")
    print("7. //div[text()='Superman']")
    print("8. //div[contains(text(), 'man')]")
    print("9. //div[starts-with(text(), 'Super')]")
    print("10. //div[not(@class)]")
    print("11. //div[last()]")
    print("12. //div[position() < 3]")
    print("13. //div | //span")
    print("14. //div//span")
    print("\nСкриншоты выполненных заданий приложены отдельно.")

if __name__ == "__main__":
    print("=== Задание 1: Тестирование Saucedemo ===")
    sauce_demo_test()
    
    print("\n=== Задание 2: CSS Trainer ===")
    css_trainer_info()
    
    print("\n=== Задание 3: XPATH Trainer ===")
    xpath_trainer_info()
