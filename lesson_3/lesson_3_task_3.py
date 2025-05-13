from address import Address
from mailing import Mailing

# Создаем адреса
to_address = Address("614000", "Пермь", "Дзержинского", "53", "1")
from_address = Address("353450", "Анапа", "Ленина", "141", "10")

# Создаем почтовое отправление
mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=500,
    track="RF123456"
)

# Распечатываем отправление в требуемом формате
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в "
      f"{mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
