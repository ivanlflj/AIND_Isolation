import os

for i in range(20):
    with open("data_winratio.txt", "a") as myfile:
        myfile.write('In the move.\n')
    os.system('python tournament_in_the_move.py')

for i in range(20):
    with open("data_winratio.txt", "a") as myfile:
        myfile.write('One move ahead.\n')
    os.system('python tournament.py')

for i in range(20):
    with open("data_winratio.txt", "a") as myfile:
        myfile.write('Two moves ahead.\n')
    os.system('python tournament_two_moves.py')
