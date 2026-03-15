# Boids Flocking Simulation in Python

Acesta este un proiect de tip Swarm Intelligence (Inteligenta de roi) care simuleaza comportamentul organic al unui stol de pasari. 

Proiectul implementeaza celebrul algoritm Boids, inventat de Craig Reynolds in 1986, pentru a demonstra cum o miscare colectiva complexa poate fi generata din interactiuni individuale simple.

## Cum functioneaza?
Fiecare "pasare" (boid) din simulare este o entitate independenta care nu urmareste un lider prestabilit. Miscarea fluida a stolului se naste exclusiv din respectarea simultana a 3 reguli de baza:

1. **Separarea (Separation):** Boids evita sa se ciocneasca de vecinii aflati in imediata apropiere, pastrand o distanta de siguranta (spatiul personal).
2. **Alinierea (Alignment):** Boids isi ajusteaza directia si viteza de zbor pentru a se potrivi cu media directiilor vecinilor din raza lor vizuala.
3. **Coeziunea (Cohesion):** Boids sunt atrasi catre centrul de masa al grupului lor de vecini, prevenind astfel izolarea de stol.

## Tehnologii folosite
* **Python 3**
* **Pygame** (pentru randare 2D si operatiuni cu vectori)