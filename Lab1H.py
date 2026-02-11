n = int(input())
trains = []
def name_to_key(name):
    key = []
    for ch in name:
        if 'a' <= ch <= 'z':
            key.append(ord(ch) - ord('a'))    
        else:  
            key.append(ord(ch) - ord('A') + 26) 
    return key
for idx in range(n):
    line = input().strip()
    parts = line.split()
    train_name = parts[0]
    time_str = parts[-1]
    hh, mm = time_str.split(':')
    minutes = int(hh) * 60 + int(mm)
    trains.append((train_name, minutes, idx, line))
    trains.sort(key=lambda x: (name_to_key(x[0]), -x[1]))
for t in trains:
    print(t[3])
