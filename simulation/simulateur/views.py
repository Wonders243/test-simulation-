from django.shortcuts import render
from django.http import JsonResponse
import random

# Taille de la grille
GRID_SIZE = 500

# Position initiale du point rouge
posX, posY = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)

def simulation_view(request):
    """Affiche la grille avec le point rouge."""
    grid_range = list(range(GRID_SIZE))  # Transformer en liste pour le template
    return render(request, 'simulateur/simulation.html', {'grid_size': GRID_SIZE, 'grid_range': grid_range})
def move_point(request):
    """Génère une nouvelle position pour le point rouge et la renvoie en JSON."""
    global posX, posY
    posX = (posX + random.choice([-1, 0, 1])) % GRID_SIZE  # Se déplace de -1, 0 ou +1
    posY = (posY + random.choice([-1, 0, 1])) % GRID_SIZE  # Se déplace de -1, 0 ou +1

    return JsonResponse({'x': posX, 'y': posY})
