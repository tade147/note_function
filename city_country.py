def city_country(city, country):
    """输出城市及其所属国家"""
    city_country = city.title() + ", " + country.title()
    return city_country

c_c1 = city_country('beijing', 'china')
c_c2 = city_country('new york', 'america')
c_c3 = city_country('tokyo', 'japan')

print(c_c1)
print(c_c2)
print(c_c3)
