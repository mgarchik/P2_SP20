import itertools
x = itertools.combinations(["G1", "G2", "G3", "G4", "G5", "G6", "F1", "F2", "F3", "F4", "F5", "F6",
                            "E1", "E2", "E3", "E4", "E5", "E6", "D1", "D2", "D3", "D4", "D5", "D6",
                            "C1", "C2", "C3", "C4", "C5", "C6", "B1", "B2", "B3", "B4", "B5", "B6"], 6)

print(len(list(x)))
