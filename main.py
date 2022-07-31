from pathlib import Path

path = plugdir.joinpath("apta.csv")

with open(path, 'r', encoding='utf-8') as apta:
    lines = apta.readlines()
    for i in lines:
        vals = i.split(",", 1)
        vals[1] = vals[1].replace("\n", "")
        if output.find(vals[1]) != -1:
            output = output.replace(vals[1], vals[0])

