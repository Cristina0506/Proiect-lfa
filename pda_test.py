
from emulatori_simplificati import load_automat_simplu, run_pda_simple

info, transitions = load_automat_simplu("automata_emulators/pda.txt")
tests = ["aaabb", "aab", "aaabbb", "aabb", "ab", ""]

for test in tests:
    print(f"PDA('{test}') = {run_pda_simple(info, transitions, test)}")
