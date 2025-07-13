from process_re import process_bank_search, process_bank_operations
from utils import json_get, transaction_sum
from reader_csv import reade_csv
from reader_xlsx import reader_xlsx
from widget import get_date, mask_account_card

get = json_get("./data/operations.json")
reader = reade_csv("./data/transactions.csv")
file_patch = "./data/transactions_excel.xlsx"
xlsx = reader_xlsx(file_patch)


def load_bank():
    """Функция предлагает пользователю выбор формата данных"""
    transaction = []
    filter_status = []
    name = input("Здравствуйте! Введите Ваше имя.\n")

    if name:
        try:
            print(f"Добро пожаловать {name} в программу работы с банковскими транзакциями")

            json_point = "1. Получить информацию о транзакциях из JSON-файла"
            csv_point = "2. Получить информацию о транзакциях из CSV-файла"
            xlsx_point = "3. Получить информацию о транзакциях из XLSX-файла"

            user_point = input(f"Выберите необходимый пункт меню: \n{json_point}\n{csv_point}\n{xlsx_point}\n")

            if user_point == '1':
                print("Выбрано получить информацию о транзакциях из JSON-файла")
                transaction.append(get)
            elif user_point == '2':
                print("Выбрано получить информацию о транзакциях из CSV-файла")
                transaction.append(reader)
            elif user_point == '3':
                print("Выбрано получить информацию о транзакциях из XLSX-файла")
                transaction.append(xlsx)
            else:
                print('Ошибка ввода, выберите вариант из списка.')
                return load_bank()

            if user_point:
                print("Введите статус, по которому необходимо выполнить фильтрацию.")
                status = ['EXECUTE', 'CANCELED', 'PENDING']
                for s in status:
                    print(f"{s}", end=', ')
                print()
                filters = input("Выберите фильтрацию:\n").upper()
                transaction.append(filters)
                if filters in status:
                    print(f"Вы выбрали фильтр: {filters}")
                    r = process_bank_search(transaction[0], transaction[1])
                    filter_status.append(r)
                    print(filter_status)
                else:
                    print(f"Статус операции {filters} недоступен")
            else:
                return load_bank()

            print("Отсортировать операции по дате? Да/Нет")
            user = str(input("Ваш ответ?:\n")).lower()
            dates_filter = []

            if user == "да":

                print("Отсортировать 'по возрастанию' или 'по убыванию'")
                revers = str(input("Ваш ответ\n")).lower()

                if revers == "по возрастанию":
                    for t in filter_status[0]:
                        dates = get_date(t["date"])
                        t["date"] = dates
                        if "from" in t:
                            y = mask_account_card(t["from"])
                            t["from"] = y
                        if "to" in t:
                            o = mask_account_card(t["to"])
                            t["to"] = o
                        dates_filter.append(t)
                    dates_filter.sort(key=lambda x: x["date"])
                    print(f"{dates_filter}\n")

                elif revers == "по убыванию":
                    for t in dates_filter[0]:
                        dates = get_date(t["date"])
                        t["date"] = dates
                        if "from" in t:
                            y = mask_account_card(t["from"])
                            t["from"] = y
                        if "to" in t:
                            o = mask_account_card(t["to"])
                            t["to"] = o
                        dates_filter.append(t)
                    dates_filter.sort(key=lambda x: x["date"], reverse=True)
                    print(f"{dates_filter}\n")
            elif user == "нет":
                return dates_filter


            # currency = str(input("Выводить только рублевые транзакции? Да/Нет")).lower()
            # if currency == "да":
                # summ = transaction_sum(transaction[0])
                # for t in transaction[0]:
                    # yt = t["operationAmount"]["currency"]["code"]
                    # process_bank_search(transaction[0], yt)
            # elif currency == "нет":
                # summ = transaction_sum(transaction[0])
                # print(summ)
        except ValueError as e:
            print(f"{e}")
        except Exception as e:
            print(f"Не понятная ошибка {e}")

    else:
        print("No name")


if __name__ == "__main__":
    load_bank()
