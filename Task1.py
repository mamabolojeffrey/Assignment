card = str(input())
suit = card[-1]
value = card[:-1]

face_cards = {
    "A":"1 or 11",
    "J":10,
    "Q":10,
    "K":10,
}

try:
    print(int(value))
except:
    print(face_cards[value])
