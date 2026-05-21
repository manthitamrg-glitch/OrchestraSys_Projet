print("=== Simulation FIFO ===")
processus = [
    ("p1", 5),
    ("p2", 3),
    ("p3", 2)
]
temps_attente = 0
temps_total = 0
for nom, duree in processus:
    print(f"{nom} s'execute pendant {duree} secondes")
    print(f"temps d'attente de {nom} : {temps_attente}")
    temps_total += duree
    temps_attente += duree
print(f"Temps total : {temps_total}")
print("\n=== Simulation SRTF ===")
processus_srtf = [
    ("p1", 5),
    ("p2", 2),
    ("p3", 1)
]
processus_tries = sorted(processus_srtf, key=lambda x: x[1])
for nom, duree in processus_tries:
    print(f"{nom} s'execute pendant {duree} secondes")