
from emulatori_simplificati import load_automat_simplu, run_nfa_simple

info, transitions = load_automat_simplu("automata_emulators/nfa.txt")
tests = ["aa", "a", "ab", "b", "aaa", ""]

for test in tests:
    print(f"NFA('{test}') = {run_nfa_simple(info, transitions, test)}")
