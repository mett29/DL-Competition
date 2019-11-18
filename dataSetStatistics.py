from PIL import Image
from itertools import chain
import os
from os.path import isfile, join
import matplotlib.pyplot as plt

basePath = "DL-CompetitionsDatasets/Classification_Dataset/training"

dirs = [join(basePath, d) for d in os.listdir(basePath) if not isfile(join(basePath, d)) ]
onlyfiles = list(chain.from_iterable(map(lambda d: [join(d,f) for f in os.listdir(d)] ,dirs ) ))

res = {}
for f in onlyfiles:
  im = Image.open(f)
  width, height = im.size
  key = "{}x{}".format(width,height)
  #print(width,height)
  if key not in res:
    res[key] = 0
  res[key] +=1


print(res)

plt.figure( figsize=(10, 10), dpi=80)
plt.bar(range(len(res)), list(res.values()), align='center')
plt.xticks(range(len(res)), list(res.keys()),  rotation='vertical', fontsize=3 )
plt.show()

filtered_res = {}
for e in res:
  if res[e] > 2:
    filtered_res[e] = res[e]


plt.figure( figsize=(15, 15), dpi=80)
plt.bar(range(len(filtered_res)), list(filtered_res.values()), align='center')
plt.xticks(range(len(filtered_res)), list(filtered_res.keys()),  rotation='vertical', fontsize=3 )
plt.show()

