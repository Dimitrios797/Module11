def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Получаем методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # Получаем модуль, к которому принадлежит объект
    obj_module = getattr(obj, '__module__', '__builtin__')  # Устанавливаем значение по умолчанию для встроенных типов

    # Создаем словарь с информацией об объекте
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
    }

    return info


# Пример пользовательского класса
class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")

    def increment(self):
        self.value += 1


# Пример использования функции
number_info = introspection_info(42)
print(number_info)

my_obj = MyClass(10)
class_info = introspection_info(my_obj)
print(class_info)