class Smartphone:
    def __init__(self, model="Unknown", price=0.0, numbers=None, memory_gb=0, battery_mah=0):
        self.model = model
        self.price = price
        self.numbers = numbers or []
        self.memory_gb = memory_gb
        self.battery_mah = battery_mah

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('price must be >= 0')
        self.__price = value

    @property
    def numbers(self):
        return list(self.__numbers)

    @numbers.setter
    def numbers(self, value):
        self.__numbers = list(value)

    @property
    def memory_gb(self):
        return self.__memory_gb

    @memory_gb.setter
    def memory_gb(self, value):
        if value < 0:
            raise ValueError('memory_gb must be >= 0')
        self.__memory_gb = value

    @property
    def battery_mah(self):
        return self.__battery_mah

    @battery_mah.setter
    def battery_mah(self, value):
        if value < 0:
            raise ValueError('battery_mah must be >= 0')
        self.__battery_mah = value

    def show(self):
        print(f"{self.__model}: {self.__price} UAH, {self.__memory_gb} GB, "
              f"{self.__battery_mah} mAh, numbers={self.__numbers}")

    def __del__(self):
        print(f"Smartphone '{self.__model}' deleted")


class PhoneStore:
    def __init__(self, phones=None):
        self.__phones = list(phones or [])

    def add(self, phone):
        self.__phones.append(phone)

    def remove(self, model):
        self.__phones = [p for p in self.__phones if p.model != model]

    def best_for_budget(self, budget):
        """Найкращий = найбільше пам'яті, потім ємність батареї, потім ціна (серед тих, що вкладаються в бюджет)."""
        affordable = [p for p in self.__phones if p.price <= budget]
        return max(affordable,
                   key=lambda p: (p.memory_gb, p.battery_mah, p.price),
                   default=None)

    def sorted_by_price(self):
        return sorted(self.__phones, key=lambda p: p.price)

    def show(self):
        for p in self.sorted_by_price():
            p.show()

    def __del__(self):
        print("PhoneStore deleted")


def main():
    store = PhoneStore([
        Smartphone("Galaxy S24", 32000, ["+380501112233", "+380671112233"], 256, 4000),
        Smartphone("Redmi Note 13", 9000, ["+380931112233"], 128, 5000),
        Smartphone("iPhone 15", 40000, ["+380991112233"], 256, 3349),
        Smartphone("Pixel 8a", 18000, ["+380631112233"], 128, 4492),
    ])
    print("Sorted by price:")
    store.show()
    budget = 20000
    best = store.best_for_budget(budget)
    print(f"\nBest phone for budget {budget}:")
    best.show() if best else print("None affordable")
    store.remove("iPhone 15")
    print("\nAfter removing iPhone 15:")
    store.show()


if __name__ == "__main__":
    main()
