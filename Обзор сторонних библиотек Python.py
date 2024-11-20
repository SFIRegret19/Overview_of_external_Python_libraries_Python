import numpy as np
import requests

# numpy
array = np.array([1, 2, 3, 4, 5])

squared_array = np.square(array)  # Квадрат каждого элемента
mean_value = np.mean(array)  # Среднее значение
sum_value = np.sum(array)  # Сумма всех элементов

print("Исходный массив:", array)
print("Квадрат каждого элемента:", squared_array)
print("Среднее значение массива:", mean_value)
print("Сумма элементов массива:", sum_value)

# requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# 2. Проверяем статус ответа
if response.status_code == 200:
    data = response.json()  # Преобразуем ответ в JSON
    
    print("\nОтвет от сервера:")
    print("Заголовок:", data['title'])
    print("Тело сообщения:", data['body'])
else:
    print("Ошибка при запросе данных, код ответа:", response.status_code)