bokstaver = ["a", "b", "c", "d", "e", "f", "e"]


def gi_antall_karakterer(tekst):
    teller = 0
    for bokstav in bokstaver:
        teller += tekst.count(bokstav)
    print(teller)
    
    
def gi_midterste_tegn(tekst):
    if len(tekst) % 2 == 0:
        tall1 = int(len(tekst) / 2 - 1)
        tall2 = int(len(tekst) / 2)
        print(tekst[tall1], tekst[tall2])
    else:
        print(tekst[int(len(tekst)/2)])
        

def sjekk_palindrom(tekst):
    reversert_tekst = tekst[::-1]
    if tekst.lower() == reversert_tekst.lower():
        print("True")
    else: 
        print("False")
        

gi_antall_karakterer("abca")
gi_midterste_tegn("abcde")    
sjekk_palindrom("Otto")   
    