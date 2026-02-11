n = int(input())
trains = []
def build_name_key(name):
    key = []
    for ch in name:
        if 'a' <= ch <= 'z':
            key.append(ord(ch) - 97)       
        else:
            key.append(ord(ch) - 65 + 26)  
    return tuple(key)   
for i in range(n):
    line = input().strip()
    parts = line.split()
    train_name = parts[0]
    time_str = parts[-1]
    hh, mm = time_str.split(':')
    minutes = int(hh) * 60 + int(mm)
    name_key = build_name_key(train_name)
    trains.append((name_key, -minutes, i, line))
    trains.sort()
for item in trains:
    print(item[3])
