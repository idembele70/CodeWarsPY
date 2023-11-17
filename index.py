def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False

print(is_leap_year(2020))
print(is_leap_year(2000))
print(is_leap_year(2015))
print(is_leap_year(2100))