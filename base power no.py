def raise_to_power (base_no , power_no ):
    result = 1
    for index in range(power_no):
        result = result * base_no
    return result
print(raise_to_power(2 ,3))