import functools
import time
import inspect


def log(filename=None):
    """Генератор автоматически логирует начало и конец выполнения функции, Принимает необязательный аргумент filename"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            arg_names = list(inspect.signature(func).parameters.keys())

            arg_string = ', '.join([f'{arg_names[i]}={args[i]!r}' for i in range(len(args))])

            start_time = time.time()
            func_name = func.__name__
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(kwargs_repr + kwargs_repr)
            try:
                result = func(*args, **kwargs)
                end_time = time.time()
                execution_time = end_time - start_time
                success_message = (f"Вызов функции {func_name}({signature})({arg_string}) выполнено успешно. Результат = {result}. Время выполнения: {execution_time:.4f} сек")
                if filename:
                    with open(filename, 'a') as f:
                        f.write(success_message + "\n")
                else:
                    print(success_message)
                return result
            except Exception as e:
                end_time = time.time()
                execution_time = end_time - start_time
                error_message = f"Ошибка в функции: {func_name}({signature})({arg_string}). Тип ошибки {type(e).__name__}, сообщение: {e}. Время выполнения: {execution_time:.4f} сек."
                if filename:
                    with open(filename, 'a') as f:
                        f.write(error_message + "\n")
                else:
                    print(error_message)
                raise
        return wrapper
    return decorator
