def hokuspokus(tekst, n):
  """funk for kryptering av teksten ved å bytte alle bokstavene i teksten med et visst
antall fremover"""
  nytekst = ""

  for bokstav in tekst:
    tallkode = ord(bokstav)
    tallkode += n
    nytekst += chr(tallkode)

  return nytekst


def simsalabim(tekst, n):
  """funk for kryptering av teksten ved å bytte alle bokstavene i teksten med et visst
antall fremover"""
  nytekst = ""

  for bokstav in tekst:
    tallkode = ord(bokstav)
    tallkode -= n
    nytekst += chr(tallkode)

  return nytekst
