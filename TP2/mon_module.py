import random

def generer_notes(n=10):
    return [random.randint(0, 100) for _ in range(n)]

def moyenne(notes):
    return sum(notes) / len(notes)
