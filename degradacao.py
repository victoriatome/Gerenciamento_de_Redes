import requests
import time

import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

times = []

url = "http://127.0.0.1:5000/"

N = 1000

for i in range(N):
    # Calculando o tempo de resposta da API em segundos
    response = requests.post(url, timeout=1000)
    elapsed_time = response.elapsed.total_seconds()
    times.append(elapsed_time)

    print(elapsed_time)


# Gráfico
fig = plt.figure()
ax = plt.axes()

x = list(range(N))

ax.plot(x, times, color='blue')
plt.show()
