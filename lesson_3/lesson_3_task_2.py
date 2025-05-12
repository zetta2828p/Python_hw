
from smartphone import Smartphone

catalog = [
    Smartphone(brand="HUAWEI", model="Mate XT", number="+79991234567"),
    Smartphone(brand="Redmi", model="14C", number="+79219876541"),
    Smartphone(brand="HONOR", model="9A", number="+79219871234"),
    Smartphone(brand="LG", model="L-52A", number="+79998529631"),
    Smartphone(brand="Xiaomi", model="13-c", number="+79233314253")
]

for smartphone in catalog:
    print (f"{smartphone.brand} {smartphone.model} {smartphone.number}")
