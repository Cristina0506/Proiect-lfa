README - Emulatoare pentru DFA, NFA, PDA și Mașina Turing
Acest proiect conține 4 emulatoare diferite care simulează funcționarea automatelor finite și a mașinii Turing.

1. DFA - Automat Finit Determinist
Ce face: Primește un șir de caractere și verifică dacă este acceptat de automat.
Automat determinist = pentru fiecare stare și simbol există o singură tranziție posibilă.
Exemplu: Șirul "0110" este acceptat dacă duce într-o stare finală.
Cod de test: dfa_test.py
Datele automatului: automata_emulators/dfa.txt

2. NFA - Automat Finit Nedeterminist
Ce face: Verifică dacă există cel puțin un drum prin automat care duce la o stare finală.
Automat nedeterminist = pot exista mai multe tranziții pentru aceeași stare și simbol.
Exemplu: "aa" poate fi acceptat chiar dacă sunt mai multe opțiuni de parcurs.
Cod de test: nfa_test.py
Datele automatului: automata_emulators/nfa.txt

3. PDA - Automat cu Stivă
Ce face: Acceptă șiruri în care contează câte caractere sunt și ordinea lor, cu ajutorul unei stive.
Exemplu: Recunoaște șiruri de forma "aaabb" (număr egal de a și b).
Stiva este folosită pentru a memora și compara simboluri pe parcurs.
Cod de test: pda_test.py
Datele automatului: automata_emulators/pda.txt

4. TM - Mașina Turing
Ce face: Simulează o mașină Turing, un model foarte puternic de calcul.
Are o bandă infinită și se poate deplasa la stânga sau la dreapta, citind și scriind simboluri.
Acceptă dacă ajunge într-o stare finală, respinge dacă ajunge într-o stare de respingere.
Exemplu: Acceptă "0111" dacă regula este: „un 0 urmat de cel puțin un 1”.
Cod de test: tm_test.py

Datele automatului: automata_emulators/tm.txt

Cum să folosești
Descarcă și dezarhivează proiectul.

Deschide folderul în PyCharm.

Rulează oricare dintre fișierele:

dfa_test.py

nfa_test.py

pda_test.py

tm_test.py

Poți modifica șirurile testate sau fișierele .txt cu alte tranziții și stări.

Format fișier automat (exemplu simplu)
txt
Copy
Edit
STATES=q0,q1
ALPHABET=0,1
START=q0
ACCEPT=q1
TRANSITIONS=
q0,0->q0
q0,1->q1