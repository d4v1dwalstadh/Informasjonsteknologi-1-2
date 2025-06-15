import datetime as dt
# Lager objekter for fødselsdato og datoen i dag
fodseslsdato = dt.datetime(2005, 5, 10) # år, måned, dag
dagensDato = dt.datetime.now()

# Skriver ut fødselsdato på en fin måte
print(fodseslsdato.strftime("%d.%m.%Y"))

# Beregner tidsforskjell mellom de to datoene
tidsforskjell = dagensDato - fodseslsdato

# Skriver ut tidsforskjell i dager delt på 365 (finner alderen)
print(tidsforskjell.days // 365)