# 1+2*3 => 7;

# result = eval('1+2*3')
# print(result)

mass = [5, 3, 2, 5, 10, 15, 10, 8, 3, 8]

def get_unic(mass):
    mass2 = []
    for i in range(len(mass)):
        if mass[i] not in mass[i+1::] and mass[i] not in mass[:i-1:]:
            mass2.append(mass[i])
    return mass2

print(get_unic(mass))