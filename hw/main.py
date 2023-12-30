from .wine import Wine
from .beer import Beer
from .market import Market

from random import randint, shuffle
"""
TODO: Доработать заготовки классов вина (Wine), пива (Beer) и магазина (Market) таким образом, чтобы через класс Market можно было:

    * получить список всех напитков (вина и пива) отсортированный по наименованию
    * проверить наличие напитка в магазине (за время О(1))
    * получить список напитков (вина и пива) в указанном диапазоне даты производства
    * (*) написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
"""

def toTitlesList(drinks):
    return list(map(lambda drink: f'{drink.title}: {drink.production_date}', drinks))

beers = []
wines = []

beers_count = randint(1, 10)
wines_count = randint(1, 10)

for i in range(beers_count):
    beers.append(Beer(f'beer_{i}', randint(1, 100)))

for j in range(wines_count):
    wines.append(Wine(f'wine_{j}', randint(1, 100)))

shuffle(beers)
shuffle(wines)

print('beers:', toTitlesList(beers))
print('wines:', toTitlesList(wines))

market = Market(wines, beers)

print(toTitlesList(market.get_drinks_sorted_by_title()))
print(toTitlesList(market.get_drinks_by_production_date(10, 30)))
print(market.has_drink_with_title('wine_8'))
