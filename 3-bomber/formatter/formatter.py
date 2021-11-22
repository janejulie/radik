import csv
with open('../data.csv') as csvDataFile:
    with open('../data_new_format.csv', 'w', encoding='UTF8') as f:
        reader = csv.reader(csvDataFile)
        writer = csv.writer(f)
        for row in reader:
            row[3] = " ".join(row[3].split('.'))
            row[4] = " ".join(row[4].split('.'))
            writer.writerow(row)
