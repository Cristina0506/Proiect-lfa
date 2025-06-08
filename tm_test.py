

from emulatori_simplificati import load_automat_simplu, run_tm_simple

info, transitions = load_automat_simplu("tm.txt")
print("TM accepta doar siruri de forma 1+")
print("Rezultat test pentru 01010 :", run_tm_simple(info, transitions, "01010"))
print("Rezultat test pentru 1111 :", run_tm_simple(info, transitions, "1111"))
print("Rezultat test pentru 000 :", run_tm_simple(info, transitions, "000"))
print("Rezultat test pentru 11101 :", run_tm_simple(info, transitions, "11101"))
print("Rezultat test pentru 1 :", run_tm_simple(info, transitions, "1"))

