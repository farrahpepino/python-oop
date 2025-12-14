class Microwave:
    
    def __init__(self, brand: str, price: float) -> None:
        self.brand = brand
        self.price = price
    
    def print_details(self) -> None:
        print(self.brand, self.price)
        
smeg: Microwave = Microwave(brand = 'smeg', price=754.72)
smeg.print_details()

whirlpool: Microwave = Microwave("whirlpool", 419.99)
whirlpool.print_details()

samsung = Microwave("samsung", 499.75)
samsung.print_details()