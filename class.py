from typing import Self

class Car:
    def __init__(self, brand: str, year: int) -> None:
        self.brand = brand
        self.year = year
        
    def __str__(self) -> str:
        return f"{self.brand} {self.year}"
    
    def __add__(self, other: Self):
        return f"{self.brand} & {other.brand}"

volvo: Car = Car('volvo', 2023)

print(volvo)

bmw: Car = Car('bmw', 2024)

print (bmw)
print (bmw + volvo)