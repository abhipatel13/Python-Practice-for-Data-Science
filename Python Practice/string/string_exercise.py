# Create three variable

street = "Blvd"
city = "Tempe"
country = "AZ"

address = street + "\n" + city + "\n" + country
address_two = f"{street}\n{city}\n{country}"

print(address, address_two)

# use of slice operator
variable_str = "Earth revolves around the sun"

print(variable_str[6:])

print(variable_str[-3:0])

# replace in string

s='maine 200 banana khaye'
s = s.replace('200','10')
s = s.replace('banana', 'samosa')
print(s)
