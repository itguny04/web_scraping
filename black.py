def blackword():
    black = []

    f = open('filter_data.txt', 'r', encoding="utf-8")
    
    for line in f:
        black = line.split(' ')
    
    return black