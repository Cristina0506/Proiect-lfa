

def load_automat_simplu(path):
    try:
        with open(path, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
        info = {}
        transitions = {}
        for line in lines:
            if "=" in line:
                key, val = line.split("=", 1)
                info[key] = val
            elif "->" in line:
                left, right = line.split("->")
                parts = left.split(",")
                if len(parts) == 2:
                    state, symbol = parts
                    transitions[(state.strip(), symbol.strip())] = right.strip()
                elif len(parts) == 3:  # PDA
                    state, symbol, stack_top = parts
                    transitions.setdefault((state.strip(), symbol.strip(), stack_top.strip()), []).append(right.strip())
        return info, transitions
    except Exception as e:
        return {"error": str(e)}, {}

# DFA
def run_dfa_simple(info, transitions, input_str):
    try:
        state = info["START"]
        accept = set(info["ACCEPT"].split(","))
        alphabet = set(info["ALPHABET"].split(","))
        for symbol in input_str:
            if symbol not in alphabet:
                return False
            key = (state, symbol)
            if key not in transitions:
                return False
            state = transitions[key]
        return state in accept
    except:
        return False

# NFA
def run_nfa_simple(info, transitions, input_str):
    try:
        start = info["START"]
        accept = set(info["ACCEPT"].split(","))
        alphabet = set(info["ALPHABET"].split(","))
        current_states = set([start])
        for symbol in input_str:
            next_states = set()
            for state in current_states:
                key = (state, symbol)
                if key in transitions:
                    next_states.update(transitions[key].split(","))
            current_states = next_states
        return bool(current_states & accept)
    except:
        return False

# PDA
from collections import deque
def run_pda_simple(info, transitions, input_str):
    try:
        stack = deque(["Z"])
        start = info["START"]
        accept = set(info["ACCEPT"].split(","))
        def dfs(state, index, stack):
            if index == len(input_str) and state in accept:
                return True
            symbol = input_str[index] if index < len(input_str) else "ε"
            top = stack[-1] if stack else "ε"
            key = (state, symbol, top)
            if key in transitions:
                for action in transitions[key]:
                    next_state, push = action.split(",")
                    new_stack = stack.copy()
                    if top != "ε":
                        new_stack.pop()
                    if push != "ε":
                        for s in reversed(push):
                            new_stack.append(s)
                    if dfs(next_state, index + (symbol != "ε"), new_stack):
                        return True
            return False
        return dfs(start, 0, stack)
    except:
        return False

# Turing machine
def run_tm_simple(info, transitions, input_str):
    try:
        tape = list(input_str) + ["B"]
        head = 0
        state = info["START"]
        accept = info["ACCEPT"]
        reject = info["REJECT"]
        for _ in range(1000):
            symbol = tape[head]
            key = (state, symbol)
            if key not in transitions:
                break
            next_state, write, move = transitions[key].split(",")
            tape[head] = write
            if move == "R":
                head += 1
                if head == len(tape):
                    tape.append("B")
            elif move == "L":
                head = max(0, head - 1)
            state = next_state
            if state == accept:
                return True
            if state == reject:
                return False
        return False
    except:
        return False
