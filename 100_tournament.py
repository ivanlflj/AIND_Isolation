import os

with open("data_winratio.txt", "a") as myfile:
    myfile.write('One move ahead, without average.\n')
for i in range(20):
    os.system('python tournament.py')
