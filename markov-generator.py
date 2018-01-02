dataset_file = ["i like cats", "i sometimes think cats are like dogs"]
model = {}

for line in dataset_file:    #dataset_file is a txt file with training quotes
    line = line.lower().split()
    for i, word in enumerate(line):
        if i == len(line)-1:
            model['END'] = model.get('END', []) + [word]
        else:
            if i == 0:
                model['START'] = model.get('START', []) + [word]
            model[word] = model.get(word, []) + [line[i+1]]


import random

generated = []
while True:
    if not generated:
        words = model['START']
    elif generated[-1] in model['END']:
        break
    else:
        words = model[generated[-1]]
    generated.append(random.choice(words))

print(generated)
