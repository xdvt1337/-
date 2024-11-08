def introspection_info(obj):
    return {
        "Тип объекта:": type(obj),
        "Атрибуты": [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
        "Методы": [method for method in dir(obj) if callable(getattr(obj, method))],
        "Модуль": getattr(obj, '__module__', 'Не определен')
    }

number_info = introspection_info(42)
print(number_info)