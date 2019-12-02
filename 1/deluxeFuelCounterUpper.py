module_mass = []
required_fuel = []

with open("input.txt") as f:
    modules = f.read().splitlines()

for module in modules:
    module_mass.append(int(module))

for module in module_mass:
    required_fuel.append(int((module / 3)) - 2)

final_fuel = sum(required_fuel)
print(final_fuel)