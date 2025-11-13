from cpmpy import *

# Duracoes (alvo i, cientista j)
dur = {
    (1,1):4, (1,4):3,
    (2,2):5, (2,3):2, (2,5):1,
    (3,1):3, (3,3):6, (3,4):2,
    (4,2):4, (4,5):4
}

horiz = 23

# Variáveis de início
starts = {k: intvar(0, horiz, name=f"T_{k[0]}_{k[1]}") for k in dur}
ends   = {k: starts[k] + dur[k] for k in dur}

model = Model()

# Fim dentro do horizonte
for k in dur:
    model += ends[k] <= horiz

# Agrupamentos
by_target = {}
by_scientist = {}
for (i,j) in dur:
    by_target.setdefault(i, []).append((i,j))
    by_scientist.setdefault(j, []).append((i,j))

# Precedência de alvos: todos de alvo i terminam antes de qualquer de alvo i+1 começar
for i in range(1,4):
    for k in by_target[i]:
        for k2 in by_target[i+1]:
            model += ends[k] <= starts[k2]

# Um cientista não sobrepõe suas próprias observações
for j, tasks in by_scientist.items():
    for idx in range(len(tasks)):
        for jdx in range(idx+1, len(tasks)):
            a = tasks[idx]; b = tasks[jdx]
            model += (ends[a] <= starts[b]) | (ends[b] <= starts[a])

# Capacidade dos instrumentos (máx 2 simultâneas)
starts_list   = [starts[k] for k in dur]
dur_list      = [dur[k] for k in dur]
demand_list   = [1]*len(dur)
model += cumulative(starts_list, dur_list, demand_list, 2)

# Minimizar makespan (fim máximo)
makespan = intvar(0, horiz, name="makespan")
for k in dur:
    model += ends[k] <= makespan
model.minimize(makespan)

# Resolver
sol = model.solve()
if sol:
    print("Makespan:", sol[makespan])
    # Ordenar por alvo
    for i in sorted(by_target):
        print(f"Alvo {i}:")
        for (ti,tj) in by_target[i]:
            s = sol[starts[(ti,tj)]]
            e = s + dur[(ti,tj)]
            print(f"  T_{ti}_{tj} = {s} .. {e} (dur={dur[(ti,tj)]})")
else:
    print("Sem solução")

