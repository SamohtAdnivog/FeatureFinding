import numpy as np
import pandas as pd


def main():
    global compared_c, searched_c
    outputfile = input("Please enter output filename: ")
    deviation = input("Please enter a deviation: ")
    try:
        deviation = float(deviation)
    except:
        print("Input not valid!")
    searchfile = pd.read_csv("200509_IM_mulitplex_salad_MFA_20mgL_0151.csv")
    compare = pd.read_csv("MFA_calc.csv")
    calcfeat = compare['m/zp']
    feature = searchfile['m/z']
    featurenr = searchfile['Feature']
    compared_a = pd.DataFrame(np.random.randn(0, 0))
    searched_a = pd.DataFrame(np.random.randn(0, 0))

    for comp in calcfeat:
        comp = float(comp)
        comp_ppm = deviation / (10 ** 6) * comp
        lb = comp - comp_ppm
        ub = comp + comp_ppm
        for feat, nr in zip(feature, featurenr):
            feat = float(feat)
            if lb <= feat <= ub:
                compared_b = compare.loc[compare['m/zp'].isin([comp])]
                compared_c = compared_a.append(compared_b)
                compared_a = compared_c
                searched_b = searchfile.loc[searchfile['Feature'].isin([nr])]
                searched_c = searched_a.append(searched_b)
                searched_a = searched_c
    head1 = list(searchfile.columns)
    head2 = list(compare.columns)
    head0 = ['index1']
    head00 = ['index2']
    head = head0 + head1 + head00 + head2

    a = (searched_c.reset_index(col_level=1))
    b = (compared_c.reset_index(col_level=1))
    merged = pd.concat([a, b], axis=1, ignore_index=True)
    merged.columns = head
    merged.drop(axis=1, labels='index1', inplace=True)
    merged.drop(axis=1, labels='index2', inplace=True)

    try:
        merged.to_csv(outputfile + '_searched.csv', index=False)
    except:
        print('File exists!')


if __name__ == "__main__":
    main()
