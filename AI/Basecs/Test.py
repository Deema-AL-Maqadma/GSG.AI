# from itertools import product

# Symboles = ["I","A","S"]
# models = []
# for p in product([False,True], repeat=3):
#     model = dict(zip(Symboles, p))
#     models.append(model)

# print(models)

# def print_models(title, models):
#     print(title)
#     for i,m in enumerate(models, start=1):
#         I = m["I"]
#         A = m["A"]
#         S = m["S"]
#         print(f"M{i}: I={I}, A={A}, S={S}")
#         #print(i, (m[S] for s in Symboles))

# print_models(models)

# models_s = []
# for m in models:
#     if m["S"] == False:
#         models_s.append(m)
# models_s = [m for ]




# from itertools import product

# Symboles = [ "I", "A", "S"]


# models = []
# for  p in product([False, True], repeat=3):
#     m = dict(zip(Symboles, p))
#     models.append(m)

# def print_models(title, models):
#     print(title)
#     for i, m in enumerate(models, start = 1):
#         I = m["I"]
#         A = m["A"]
#         S = m["S"]
#         print(f"M{i}: I={I}, A={A}, S={S}")
#         # print( i, (m[s] for s in Symboles) )

# print_models("All models", models)   

# models_s = []
# for m in models:
#     if m["S"] == False:
#         models_s.append(m)

# # models_s = [m for m in models if m["S"] == False]

# print_models("models_s", models_s)

# def implication( p, q):
#     return not p or q # p=T & q=F -> F else T


# models_A_S = []
# for m in models_s:
#     if implication(m["A"],m["S"]):
#         models_A_S.append(m)


from itertools import product

Symboles = [ "I", "A", "S"]


models = []
for  p in product([False, True], repeat=3):
    m = dict(zip(Symboles, p))
    models.append(m)

def print_models(title, models):
    print(title)
    for i, m in enumerate(models, start = 1):
        I = m["I"]
        A = m["A"]
        S = m["S"]
        print(f"M{i}: I={I}, A={A}, S={S}")
        # print( i, (m[s] for s in Symboles) )

print_models("All models", models)   

models_s = []
for m in models:
    if m["S"] == False:
        models_s.append(m)

# models_s = [m for m in models if m["S"] == False]

print_models("models_s", models_s)

def implication( p, q):
    return (not p) or q


def implication(p, q):
    return (not p) or q

I_A_models = [] 
if implication(m["I"], m["A"]):
    I_A_models.append(m)
print_models("I_S_models", I_A_models)


A_S_models = [] 
if implication(m["A"], m["S"]) and implication(m["I"], m["A"]):
    A_S_models.append(m)
print_models("A_S_models", A_S_models)

KB_models = []
for m in models:
    if (implication(m["A"], m["S"]) and
        implication(m["I"], m["A"]) and
        not m["S"]):
        KB_models.append(m)

print_models("Knowledge Base models (A→S, I→A, ¬S)", KB_models)

print("Conclusion:")
flag = True
for m in KB_models:
    if m["I"]:
        flag == False
        break
if flag:
    print("I is false in all KB models")
else:
    print("I is true in some KB models")
