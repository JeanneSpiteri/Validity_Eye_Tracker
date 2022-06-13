import glob
import numpy as np
import pandas as pd
import os
data_id = []
data_left_eye = []
data_right_eye = []

chemin = glob.glob(os.path.join('/Users/jeannespiteri/Desktop/csv_eyetracker_7_diff', '*.tsv'))
for tsv in chemin:
    df = pd.read_csv(tsv, delimiter='\t', on_bad_lines='skip')

    id = (os.path.splitext(os.path.basename(tsv))[0])
    data_id.append(id)

    Correct_left = df[df['ValidityLeft'] == 1]
    proportion = len(Correct_left) / len(df['ValidityLeft'])
    Pourcentage_data_correct_left = proportion * 100
    #print('Le pourcentage de coordonnées valides pour l oeil gauche est ', Pourcentage_data_correct_left)
    data_left_eye.append(Pourcentage_data_correct_left)


    Correct_Right = df[df['ValidityRight'] == 1]
    proportion = len(Correct_Right) / len(df['ValidityRight'])
    Pourcentage_data_correct_right = proportion * 100
    #print('Le pourcentage de coordonnées valides pour l oeil droit est ', Pourcentage_data_correct_right)
    data_right_eye.append(Pourcentage_data_correct_right)

headerList = ['identifiant', 'validity left', 'validity right']
tableau = pd.DataFrame(np.array([data_id, data_left_eye, data_right_eye]).T)
tableau.columns=headerList
tableau.to_csv('ET_validity.csv', header=True, index=False)
print(tableau)





# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
