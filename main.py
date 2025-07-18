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
    filter_many = []
    filter_code = []
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
                status = ["EXECUTED", "CANCELED", "PENDING"]
                # for s in status:
                    #print(f"{s}", end=', ')
                print(", ".join(status))
                print()
                filters = input("Выберите фильтрацию:\n").upper()
                transaction.append(filters)
                if filters in status:
                    print(f"Вы выбрали фильтр: {filters}")
                    h = False
                    for p in transaction[0]:
                        if "state" in p:
                            if filters == p["state"]:
                                r = process_bank_search(transaction[0], transaction[1])
                                filter_status.append(r)
                                h = True
                    if not h:
                        print("Данного статуса нету в списке")
                        exit()
                        # print(filter_status)
                else:
                    print(f"Статус операции {filters} недоступен")

            else:
                return load_bank()

            print("Отсортировать операции по дате? Да/Нет")
            user = str(input("Ваш ответ?:\n")).lower()
            dates_filter = []

            if user:
                if user == "да":
                    print("Отсортировать 'по возрастанию' или 'по убыванию'")
                    revers = str(input("Ваш ответ\n")).lower()
                    if revers == "по возрастанию":
                        if user_point == "1":
                            for t in filter_status[0]:
                                if "date" in t:
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
                            # print(f"{dates_filter}\n")
                        else:
                            for t in filter_status[0]:
                                if "date" in t:
                                    dates = get_date(t["date"])
                                    t["date"] = dates
                                if "from" in t:
                                    y = mask_account_card(str(t["from"]))
                                    t["from"] = y
                                if "to" in t:
                                    o = mask_account_card(str(t["to"]))
                                    t["to"] = o
                                dates_filter.append(t)
                            dates_filter.sort(key=lambda x: x["date"])
                            # print(f"{dates_filter}\n")

                    elif revers == "по убыванию":
                        if user_point == "1":
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
                            dates_filter.sort(key=lambda x: x["date"], reverse=True)
                            # print(f"{dates_filter}\n")
                        else:
                            for t in filter_status[0]:
                                dates = get_date(t["date"])
                                t["date"] = dates
                                if "from" in t:
                                    y = mask_account_card(str(t["from"]))
                                    t["from"] = y
                                if "to" in t:
                                    o = mask_account_card(str(t["to"]))
                                    t["to"] = o
                                dates_filter.append(t)
                            dates_filter.sort(key=lambda x: x["date"], reverse=True)
                            # print(f"{dates_filter}\n")

                elif user == "нет":
                    if user_point == "1":
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
                        #print(f"{dates_filter}\n")
                    else:
                        for t in filter_status[0]:
                            dates = get_date(t["date"])
                            t["date"] = dates
                            if "from" in t:
                                y = mask_account_card(str(t["from"]))
                                t["from"] = y
                            if "to" in t:
                                o = mask_account_card(str(t["to"]))
                                t["to"] = o
                            dates_filter.append(t)
                        #print(f"{dates_filter}\n")
            else:
                print("Вы не выбрали вариант сортировки")
                return load_bank()

            print("Выводить только рублевые транзакции? Да/Нет\n")
            currency = str(input("Ваш ответ:\n")).lower()
            if currency:
                if currency == "да":
                    if user_point == '1':
                        rub_found = False
                        for t in dates_filter:
                            yt = t["operationAmount"]["currency"]["code"]
                            if yt == "RUB":
                                filter_many.append(t)
                                rub_found = True
                        if not rub_found:
                            print("Нет рублевых транзакций")
                            filter_many = dates_filter
                        # print(filter_many)

                    else:
                        rub_found = False
                        for t in dates_filter:
                            yt = t["currency_name"]
                            if "RUB" in yt:
                                filter_many.append(t)
                                rub_found = True
                        if not rub_found:
                            print("Нету рублевых транзакций")
                            filter_many = dates_filter
                        # print(filter_many)

                elif currency == "нет":
                    if user_point == '1':
                        for t in dates_filter:
                            yt = t["operationAmount"]["currency"]["code"]
                            if yt != "RUB":
                                filter_many.append(t)

                    else:
                        for t in dates_filter:
                            yt = t["currency_name"]
                            if yt != "RUB":
                                filter_many.append(t)
            else:
                print("Вы не выбрали вариант транзакции\n")
                return load_bank()

            print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
            transaction_word = input("Ваш ответ:\n").lower()
            if transaction_word:
                if transaction_word == "да":
                    f = []
                    filter_word = input("Введите слово для фильтрации:\n").capitalize()
                    filter_transaction = []
                    categories_list = []
                    for i in filter_many:
                        o = i["description"]
                        if filter_word in o:
                            filter_transaction.append(i)
                            categories_list.append(filter_word)
                            filter_code.append(i)
                    category_count = process_bank_operations(filter_transaction, categories_list)
                    f.append(category_count)
                    for o in f[0].values():
                        print(f"Всего банковских операций: {o}\n")
                else:
                    filter_code = filter_many
            else:
                print("Нету транзакции")

            print_exit = []
            if user_point == '1':
                for i in filter_code:
                    if "from" in i:
                        date_filter = i["date"]
                        description_filter = i["description"]
                        from_filter = i["from"]
                        to_filter = i["to"]
                        amount_filter = i["operationAmount"]["amount"]
                        code_filter = i["operationAmount"]["currency"]["name"]
                        x = date_filter, description_filter, from_filter, to_filter, amount_filter, code_filter
                        print_exit.append(x)
                    else:
                        date_filter = i["date"]
                        description_filter = i["description"]
                        to_filter = i["to"]
                        amount_filter = i["operationAmount"]["amount"]
                        code_filter = i["operationAmount"]["currency"]["name"]
                        x = date_filter, description_filter, to_filter, amount_filter, code_filter
                        print_exit.append(x)

            elif user_point == "2":
                for i in filter_code:
                    if "from" in i:
                        if i["from"] != "Поле для ввода пустое":
                            date_filter = i["date"]
                            description_filter = i["description"]
                            from_filter = i["from"]
                            to_filter = i["to"]
                            amount_filter = i["amount"]
                            code_filter = i["currency_name"]
                            x = date_filter, description_filter, from_filter, to_filter, amount_filter, code_filter
                            print_exit.append(x)
                        else:
                            date_filter = i["date"]
                            description_filter = i["description"]
                            to_filter = i["to"]
                            amount_filter = i["amount"]
                            code_filter = i["currency_name"]
                            x = date_filter, description_filter, to_filter, amount_filter, code_filter
                            print_exit.append(x)

            elif user_point == "3":
                for i in filter_code:
                    if "from" in i:
                        if i["from"] != "Некорректный ввод":
                            date_filter = i["date"]
                            description_filter = i["description"]
                            from_filter = i["from"]
                            to_filter = i["to"]
                            amount_filter = i["amount"]
                            code_filter = i["currency_name"]
                            x = date_filter, description_filter, from_filter, to_filter, amount_filter, code_filter
                            print_exit.append(x)
                        else:
                            date_filter = i["date"]
                            description_filter = i["description"]
                            to_filter = i["to"]
                            amount_filter = i["amount"]
                            code_filter = i["currency_name"]
                            x = date_filter, description_filter, to_filter, amount_filter, code_filter
                            print_exit.append(x)

            # print(print_exit)

            for item in print_exit:
                if "Открытие" in item[1]:
                    print(f"{item[0]} {item[1]}\n {item[2]}\n Сумма: {item[3]} {item[4]}")

                if "Перевод" in item[1]:
                    print(f"{item[0]} {item[1]}\n {item[2]} -> {item[3]}\n "
                          f"Сумма: {item[4]} {item[5]}")
                else:
                    print(f"{item[0]} {item[1]}\n {item[2]}\n "
                          f"Сумма: {item[3]} {item[4]}")

        except ValueError as e:
            print(f"{e}")
        except Exception as e:
            print(f"Не понятная ошибка {e}")

    else:
        print("No name")


if __name__ == "__main__":
    load_bank()
