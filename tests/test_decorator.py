import pytest
import decorators


def test_log_no_file(capsys):
    """Этот тест проверяет работу декоратора @decorators.log(), когда не указан файл для записи логов"""
    @decorators.log()
    def add(x, y):
        return x + y

    result = add(2, 3)
    captured = capsys.readouterr()
    assert "Вызов функции add()(x=2, y=3) выполнено успешно. Результат = 5" in captured.out
    assert result == 5


def test_log_with_file(tmp_path):
    """Тест для @decorators.log(), Здесь указан файл для записи логов (log_file). Она определяет функцию multiply(x, y), которая умножает два числа"""
    log_file = tmp_path / "test.log"

    @decorators.log(filename=log_file)
    def multiply(x, y):
        return x * y

    result = multiply(4, 5)
    assert result == 20

    with open(log_file, "r") as f:
        log_content = f.read()
        assert "Вызов функции multiply()(x=4, y=5) выполнено успешно. Результат = 20" in log_content


def test_log_exception(capsys, tmp_path):
    """Этот тест проверяет, как декоратор @decorators.log() обрабатывает исключения"""
    log_file = tmp_path / "error.log"

    @decorators.log(filename=log_file)
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    if log_file.exists():
        with open(log_file, "r") as f:
            log_content = f.read()
        assert "Ошибка в функции: divide()(x=10, y=0). Тип ошибки ZeroDivisionError" in log_content
    else:
        assert "Ошибка в функции: divide()(x=10, y=0). Тип ошибки ZeroDivisionError" in captured.err
