#funker kun hvis du åpner mappen
with open("tall.txt") as fil:
    for linje in fil:
        data = linje.rstrip().split("-")
        data = list(map(int, data))
    
        summen = sum(data)
        gjennomsnitt = summen / 5
    
        with open("organiserte_tall.txt", "a") as fil2: 
            fil2.write(f"Tall: {data}, sum: {summen}, gjennomsnitt: {gjennomsnitt} \n")

