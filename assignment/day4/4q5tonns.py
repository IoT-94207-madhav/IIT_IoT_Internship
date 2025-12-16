tonns_to_kilograms = lambda tonns: tonns * 1000
kilograms_to_grams = lambda kg: kg * 1000
grams_to_milligrams = lambda g: g * 1000
milligrams_to_pounds = lambda mg: mg / 453592.37

tonns  = int(input("enter weight in tonns : "))
kg = tonns_to_kilograms(tonns)
g = kilograms_to_grams(kg)
mg = grams_to_milligrams(g)
pounds = milligrams_to_pounds(mg)
# convert into list 

print("Weight conversions in list format:")
return_list = [tonns, kg, g, mg, pounds]
print(return_list)
