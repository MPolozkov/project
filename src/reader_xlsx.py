from typing import Any, Dict, List

import pandas as pd


def reader_xlsx(read: str) -> List[Dict[str, Any]]:
    """Функция для чтения файлов EXEL"""
    try:
        df = pd.read_excel(read, engine='openpyxl')
        transaction: List[Dict[str, Any]] = df.to_dict(orient='records')
        return transaction
    except FileNotFoundError:
        print(f"Ошибка: Файл '{read}' не найден.")
        return []
    except ImportError:
        print("Ошибка: Библиотека 'openpyxl' не установлена. Пожалуйста, установите ее.")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return []


# file_patch = '../data/transactions_excel.xlsx'
# data = reader_xlsx(file_patch)
# print(data)
