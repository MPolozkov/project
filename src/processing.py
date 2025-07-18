from datetime import datetime
from typing import Dict, List, Optional


def filter_by_state(data: List[Dict], state_value: Optional[str] = "EXECUTED") -> List[Dict]:
    """Фильтрует список словарей, возвращая только те словари,
    у которых значение ключа 'state' соответствует указанному значению."""

    filtered_data = []

    # Запускаем цикл
    for item in data:
        if isinstance(item, dict) and item.get("state") == state_value:  # Используем .get()
            filtered_data.append(item)
    return filtered_data


def sort_by_date(data: List[Dict], descending: Optional[bool] = True) -> List[Dict]:
    """Сортирует список словарей по дате (ключ 'date')."""

    valid_dates = []  # Список для элементов с корректными датами
    invalid_dates = []  # Список для элементов с некорректными датами
    no_dates = []  # Список для элементов без ключа 'date'

    # Разделяем элементы на три группы:
    for item in data:
        date_str = item.get("date")  # Получаем значение ключа 'date', если он есть
        if date_str:  # Если ключ 'date' существует
            try:
                # Пытаемся преобразовать строку даты в объект datetime
                date_object = datetime.fromisoformat(date_str)
                # Если преобразование прошло успешно, добавляем кортеж (date_object, item)
                # в список valid_dates.  Сохраняем и дату, и исходный словарь.
                valid_dates.append((date_object, item))
            except ValueError:
                # Если преобразование не удалось (некорректный формат даты),
                # добавляем элемент в список invalid_dates
                invalid_dates.append(item)
        else:
            # Если ключ 'date' отсутствует, добавляем элемент в список no_dates
            no_dates.append(item)

    # Сортируем только элементы с корректными датами:
    # Используем метод sort() со вспомогательной лямбда-функцией в качестве ключа сортировки.
    # Лямбда-функция извлекает объект datetime из кортежа (date_object, item).
    if descending is True:
        valid_dates.sort(key=lambda x: x[0], reverse=True)
    else:
        valid_dates.sort(key=lambda x: x[0], reverse=False)

    # После сортировки извлекаем только сами словари из valid_dates
    #  и сохраняем в отдельный список
    valid_dates_only = [item[1] for item in valid_dates]

    # Объединяем все три списка в один:
    # Сначала идут отсортированные элементы с корректными датами,
    # затем элементы с некорректными датами, и в конце элементы без даты.
    # Порядок элементов в списках invalid_dates и no_dates сохраняется.
    if descending:
        if valid_dates_only:
            return valid_dates_only
        elif invalid_dates:
            return invalid_dates
        else:
            return no_dates
    else:
        return valid_dates_only


if __name__ == "__main__":
    # Проверочные данные:
    data = [
        {"id": 1, "date": "2023-10-29T10:00:00"},
        {"id": 2, "date": "2023-10-30T12:00:00"},
        {"id": 3, "date": "2023-10-28T14:00:00"},
    ]
    print(sort_by_date(data))
