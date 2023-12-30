from datetime import datetime

def info_decorator(func):
    def wrapper(*args, **kwargs):
        current_time = datetime.now()

        print(f'\nНачало выполнения функции {func.__name__}')
        print(f'Текущее время: {current_time.replace(microsecond=0)}')

        result = func(*args, **kwargs)
        finish = datetime.now()

        print(f'Затраченное время: {finish.second - current_time.second} с {finish.microsecond - current_time.microsecond} мкс')
        print('Результат выполнения:\n')

        return result
    return wrapper

class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.wines = { drink.title: drink for drink in wines }
        self.beers = { drink.title: drink for drink in beers }
        pass

    @info_decorator
    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)

        :param title:
        :return: True|False
        """
        if not title:
            return False

        if title not in self.wines and title not in self.beers:
            return False
        return True

    @info_decorator
    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        def sort_by_title(drink):
            return drink.title
        
        drinks = [*self.beers.values(), *self.wines.values()]

        sorted_drinks_by_title = sorted(drinks, key = sort_by_title)
        return sorted_drinks_by_title

    @info_decorator
    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        def sort_by_date(drink):
            return drink.production_date
        
        def is_in_range(drink):
            if not from_date and not to_date:
                return True
            elif not from_date:
                return drink.production_date <= to_date
            elif not to_date:
                return drink.production_date >= from_date
            return drink.production_date >= from_date and drink.production_date <= to_date

        drinks = [*self.beers.values(), *self.wines.values()]

        sorted_drinks_by_date = sorted(drinks, key = sort_by_date)
        filtered_drinks_by_date = list(filter(lambda drink: is_in_range(drink), sorted_drinks_by_date))
        
        return filtered_drinks_by_date
