import csv
import pprint

with open('/home/pi/DiscordBot/Schedule_FirstHalf.csv') as f:
    #print(f.read())
    reader = csv.reader(f)
    l = [row for row in reader]

print('教科:', end="")
print(l[11][1], end=", ")

print('場所:', end="")
print(l[11][2], end=", ")

print('担当教員:', end="")
print(l[11][3])