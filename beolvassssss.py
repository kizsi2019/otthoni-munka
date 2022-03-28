programnyelv = []
program = open('programnyelv.csv')
with open('programnyelv.csv', 'r', encoding='utf-8') as programnyelv:
    for sor in programnyelv:
        adatok = sor.strip().split(',')
        nyelv = {'évszám': adatok[0], 'nyelv': adatok[1], 'feltaláló': int(adatok[2])}
        programnyelv.append(nyelv)
print(f'{nyelv=}')