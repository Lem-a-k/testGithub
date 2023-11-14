# csv-файл, заголовок, читать + сортировка
import csv

FILE = 'test.csv'  # input()
with open(FILE) as csv_in:
    dr = csv.DictReader(csv_in, delimiter=';')
    fn = dr.fieldnames
    table = [(row[fn[0]],
              float(row[fn[1]]),
              int(row[fn[2]])) for row in dr]

print(*sorted(table, key=lambda x: x[1]), sep='\n')