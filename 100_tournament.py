import os

for j in range(5):
    with open("data_winratio.txt", "a") as myfile:
        myfile.write('In the move.\n')
    for i in range(5):
        os.system('python tournament_in_the_move.py')

    with open("data_winratio.txt", "a") as myfile:
        myfile.write('One move ahead.\n')
    for i in range(5):
        os.system('python tournament.py')

    with open("data_winratio.txt", "a") as myfile:
        myfile.write('Two moves ahead.\n')
    for i in range(5):
        os.system('python tournament_two_moves.py')
