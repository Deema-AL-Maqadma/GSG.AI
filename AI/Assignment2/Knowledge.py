# ---------------------------------------------------------
# A* Search Algorithm - Assignment (1)
# Deema Mohammed AL-Maqadma
# ---------------------------------------------------------
from itertools import product

# Define the symbols (A = alarm, E = empty, S = armed)
symbols = ["A", "E", "S"]

# Generate all possible models (all True/False combinations)
models = []
for p in product([False, True], repeat=3):
    m = dict(zip(symbols, p))
    models.append(m)

# Implication function (P → Q)
def implication(p, q):
    return (not p) or q

# Helper function to print models
def print_models(title, models):
    print(title)
    for i, m in enumerate(models, start=1):
        print(f"M{i}: A={m['A']}, E={m['E']}, S={m['S']}")
    print()

# Build the Knowledge Base:
# A → E,  ¬E,  E → S,  ¬S
KB_models = []
for m in models:
    if (implication(m["A"], m["E"]) and
        (not m["E"]) and
        implication(m["E"], m["S"]) and
        (not m["S"])):
        KB_models.append(m)

# Show all models that satisfy the KB
print_models("Models that satisfy the Knowledge Base:", KB_models)

# Check entailment: all KB models must agree on the value
def entails(KB_models, symbol, value=True):
    for m in KB_models:
        if m[symbol] != value:
            return False
    return True

# Required queries
print("Does KB entail Alarm?        ", entails(KB_models, "A", True))
print("Does KB entail Empty?        ", entails(KB_models, "E", True))
print("Does KB entail Armed?        ", entails(KB_models, "S", True))
print("Does KB entail NOT Alarm?    ", entails(KB_models, "A", False))