import csv
def readvisitors(file):
    visitors = []
    with open(file, encoding = 'utf-8') as f:
        reader = csv.DictReader(f, delimiter=',', quotechar = '"')
        for visitor in reader:
            visitors.append(visitor)
            return visitors
def selection_sort(visitors):
    n = len(visitors)
    for i in range(n -1):
        mi = i
        for j in range(i + 1, n):
            if visitors[j]['age'] < visitors[mi]['age']:
                mi = j
        visitors[i], visitors[mi] = visitors[mi], visitors[i]
