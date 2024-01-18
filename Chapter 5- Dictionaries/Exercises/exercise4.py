rivers = {
    "Nile":"Egypt",
    "Mississippi River":"USA",
    "Yangtze":"China",
}
for k,v in rivers.items():
    print(k,"runs through",v,end='.\n')
for k in rivers.keys():
    print(k)
for v in rivers.values():
    print(v)