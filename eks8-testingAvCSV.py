from time import sleep
import csv
import random

with open('test.csv', mode='a') as csvfile:
    skriver = csv.writer(csvfile, delimiter=',')

    for x in range(1,10):
        skriver.writerow([random.randint(1,100),"blablabla"])
        sleep(0.1)