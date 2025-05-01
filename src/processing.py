from datetime import datetime
from typing import Dict, List, Optional


def filter_by_state(data: List[Dict], state_value: Optional[str] = "EXECUTED") -> List[Dict]:
    """Фильтрует список словарей, возвращая только те словари,
    у которых значение ключа 'state' соответствует указанному значению."""

    filter_data = []
    for item in data:
        if item["state"] == state_value:
            filter_data.append(item)
    return filter_data


def sort_by_date(data: List[Dict], descending: Optional[bool] = True) -> List[Dict]:
    """Сортирует список словарей по дате (ключ 'date')."""

    sorted_data = data.copy()

    def get_date_for_sorting(item: Dict) -> datetime | str:
        """Вспомогательная функция для извлечения даты и обработки ошибок."""

        date_str = item.get("date")
        # Проверяем, что ключ 'date' существует
        if date_str:
            try:
                return datetime.fromisoformat(date_str)
            except ValueError:
                return "Дата не корректна"
        return "Нету ключа date"

    # Используем лямбда-функцию в качестве ключа для сортировки
    sorted_data.sort(key=get_date_for_sorting, reverse=True)

    return sorted_data
