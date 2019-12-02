module_mass = []
module_required_fuel = []
fuel_required_fuel = []
test = []

with open("input.txt") as f:
    modules = f.read().splitlines()

for module in modules:
    module_mass.append(int(module))

for module in module_mass:
    module_required_fuel.append(int(module / 3 - 2))

for fuel in module_required_fuel:
    while fuel / 3 - 2 > 0:
        reqd_fuel = int(fuel / 3 - 2)
        fuel = reqd_fuel
        fuel_required_fuel.append(reqd_fuel)

final_final_fuel = sum(fuel_required_fuel + module_required_fuel)
print(final_final_fuel)
