def er_du_ung(navn:str, alder:int):
    if alder < 30:
        print(f"Hei, {navn}, du er ung")
    else:
        print(f"Du er gammel, {navn}!")
    
er_du_ung("Lise", 78)
er_du_ung("Janne", 28)