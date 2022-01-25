from datetime import datetime
tid = datetime.now()
print(tid.date())

import time
no = time.strftime('%Y-%m-%d %H-%M-%S')
print(no)

cpuTemp = 54
listeCPUTemp = [56.7,56.8,57.1,55.8,56.3]
print(listeCPUTemp[1:])
nyListe = listeCPUTemp[1:] + [cpuTemp]
print(nyListe)