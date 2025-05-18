from collections import defaultdict

fname = input("Masukkan nama file: ")
fhandle = open(fname)
domains = defaultdict(int)

for line in fhandle:
    if line.startswith("From "):
        parts = line.split()
        if len(parts) > 1 and '@' in parts[1]:
            domain = parts[1].split('@')[1]
            domains[domain] += 1

print(dict(domains))
