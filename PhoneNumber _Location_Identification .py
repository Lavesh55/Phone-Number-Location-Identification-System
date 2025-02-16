import phonenumbers

from phonenumbers import geocoder
from phonenumbers import timezone 
from phonenumbers import carrier

phone_number1 =phonenumbers.parse("+918878586271")
timezone1=timezone.time_zones_for_number(phone_number1)

phone_number2 =phonenumbers.parse("+919829635011")
timezone2=timezone.time_zones_for_number(phone_number2)

phone_number3 =phonenumbers.parse("+911234567890")
timezone3=timezone.time_zones_for_number(phone_number3)

print("\nPhone Numbers Location,timezone,company name\n")

print(geocoder.description_for_number(phone_number1,"en"));
print(timezone1);
print(carrier.name_for_number(phone_number1,"en"));

print(geocoder.description_for_number(phone_number2, "en"));
print(timezone2);
print(carrier.name_for_number(phone_number1,"en"));

print(geocoder.description_for_number(phone_number3,"en"));
print(timezone3);
print(carrier.name_for_number(phone_number3,"en"));