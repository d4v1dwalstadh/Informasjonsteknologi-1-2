def potensiellEnergi(m, h, g=9.81):
  print(f"En gjenstand med massen {m} kg ved høyden {h} m har den p_E\t")
  print(f"{m*g*h:.2f} J (med g = {g}).")


potensiellEnergi(50, 10)

potensiellEnergi(50, 10, g=1.62)
potensiellEnergi(50, 10, 1.62)

