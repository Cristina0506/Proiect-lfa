
from emulatori_simplificati import load_automat_simplu, run_dfa_simple

info, transitions = load_automat_simplu("automata_emulators/dfa.txt")
tests = ["0110", "0", "01", "011", ""]

for test in tests:
    print(f"DFA('{test}') = {run_dfa_simple(info, transitions, test)}")
