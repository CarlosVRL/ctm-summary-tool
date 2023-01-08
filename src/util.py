import csv


def get_csv(filename):
    results = []
    with open(filename, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            results.append(row)
    return results


def get_props(filename):
    props = {}
    with open(filename) as file:
        for line in file:
            name, var = line.partition('=')[::2]
            props[name.strip()] = var.strip()
    return props
