def on_palindromi(lause):
    teksti = ""
    for merkki in lause:
        if merkki.isalpha():
            teksti += merkki.lower()
    return teksti == teksti[::-1]
ehdokkaat = [
    'A man, a plan, a canal: Panama.',
    'Iso rikas sika sökösakissa kirosi.',
    '"Aa, viinaa sitruksilla", kallis kurtisaani ivaa.',
    'Joku satunnainen lause',
    "Madam, I'm Adam.",
    "Never odd or even.",
    "Was it a car or a cat I saw?",
    "Mr. Owl ate my metal worm.",
    "No lemon, no melon.",
    "Evil rats on no star live."
]
for e in ehdokkaat:
    if on_palindromi(e):
        print(f'"{e}": ON palindromi')
    else:
        print(f'"{e}": EI OLE palindromi')
