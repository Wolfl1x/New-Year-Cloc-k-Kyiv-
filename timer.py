import tkinter as tk
from datetime import datetime, timedelta
import pyfiglet

def update_timer():
    # Определяем дату и время следующего Нового года
    now = datetime.now()
    next_new_year = datetime(now.year + 1, 1, 1)
    
    # Рассчитываем оставшееся время
    time_left = next_new_year - now
    
    # Форматируем оставшееся время (дни, часы, минуты, секунды)
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    # Создаем строку в формате "D:HH:MM:SS"
    time_left_str = f"{days}d {hours:02}:{minutes:02}:{seconds:02}"
    
    # Преобразуем время в ASCII-формат
    ascii_time = pyfiglet.figlet_format(time_left_str, font="slant")
    
    # Обновляем текст на метке
    timer_label.config(text=ascii_time)
    
    # Запускаем обновление таймера каждую секунду
    timer_label.after(1000, update_timer)

# Создаем главное окно
root = tk.Tk()
root.title("Таймер до Нового года в ASCII")
root.geometry("1000x600")
root["bg"] = "black"

# Создаем метку для отображения таймера
timer_label = tk.Label(root, font=("Courier", 12), bg="black", fg="white", justify="left")
timer_label.pack(expand=True)

# Запускаем функцию обновления таймера
update_timer()

# Запускаем главный цикл приложения
root.mainloop()
