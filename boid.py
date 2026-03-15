import pygame
import random
import math
import config

class Boid:
    def __init__(self, x, y):
        #vector pentru pozitie
        self.position = pygame.math.Vector2(x, y)

        #vector pentru viteza cu valori rationale
        self.velocity = pygame.math.Vector2(random.uniform(-2, 2), random.uniform(-2, 2))

        #culoare si marime
        self.color = config.BOID_COLOR
        self.size = config.BOID_SIZE

    def separation(self, flock):
        steering = pygame.math.Vector2(0, 0)
        total = 0
        perception_radius = 40

        #calc. distanta fata de ceilalti si verific daca e prea aproape
        for other in flock:
            #sa nu se compare cu ea insasi
            if other != self:
                distance = self.position.distance_to(other.position)

                if distance < perception_radius and distance > 0:
                    #vector care fuge de pasari, arata de la pasarea intrusa la mine
                    diff = self.position - other.position

                    #au aceeasi lungime, deci obtin doar directia
                    diff /= distance
                    steering += diff
                    #nr de pasari prea aproape
                    total += 1

        #calculez viraju in functie de numaru de pasari pentru o ruta optima
        if total > 0:
            steering /= total

            #viteza maxima 4
            if steering.length() > 0:
                steering = steering.normalize() * 4
                steering -= self.velocity

                #sa nu fie miscari prea bruste
                if steering.length() > 0.2:
                    steering.scale_to_length(0.2)

        return steering
    
    def alignment(self, flock):
        #cam la fel ca cea de separare structural cumva
        steering = pygame.math.Vector2(0, 0)
        total = 0
        perception_radius = 50

        for other in flock:
            if other != self:
                distance = self.position.distance_to(other.position)
                
                if distance < perception_radius:
                    steering += other.velocity
                    total += 1

        if total > 0:
            steering /= total

            if steering.length() > 0:
                steering = steering.normalize() * 4

                steering -= self.velocity

                if steering.length() > 0.2:
                    steering.scale_to_length(0.2)

        return steering
    
    def cohesion(self, flock):
        steering = pygame.math.Vector2(0, 0)
        center_of_mass = pygame.math.Vector2(0, 0)
        total = 0
        perception_radius = 50

        for other in flock:
            if other != self:
                distance = self.position.distance_to(other.position)

                if distance < perception_radius:
                    center_of_mass += other.position
                    total += 1

        #aflu unde e mijlocu grupului
        if total > 0:
            center_of_mass /= total

            steering = center_of_mass - self.position

            if steering.length() > 0:
                steering = steering.normalize() * 4

                steering -= self.velocity

                if steering.length() > 0.2:
                    steering.scale_to_length(0.2)
        
        return steering
    
    def update(self, flock):
        separation_velocity = self.separation(flock)
        alignment_velocity = self.alignment(flock)
        cohesion_velocity = self.cohesion(flock)

        self.velocity += separation_velocity * 1.5
        self.velocity += alignment_velocity 
        self.velocity += cohesion_velocity

        if self.velocity.length() > 4:
            self.velocity.scale_to_length(4)

        #schimb pozitia adunand viteza
        self.position += self.velocity

        #iese pe o parte intra pe cealalta
        if self.position.x > config.SCREEN_WIDTH:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = config.SCREEN_WIDTH

        if self.position.y > config.SCREEN_HEIGHT:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = config.SCREEN_HEIGHT
    
    def draw(self, screen):
        #unghiu de rotatie pe baza vectorului de viteza
        angle = math.atan2(self.velocity.y, self.velocity.x)

        #punctele triunghiului
        #varfu
        p1 = (self.position.x + math.cos(angle) * self.size * 2,
              self.position.y + math.sin(angle) * self.size * 2)
        
        #coltu din stanga spate
        p2 = (self.position.x + math.cos(angle + 2.5) * self.size * 1.5, 
              self.position.y + math.sin(angle + 2.5) * self.size * 1.5)
        
        #coltu din dreapta spate
        p3 = (self.position.x + math.cos(angle - 2.5) * self.size * 1.5, 
              self.position.y + math.sin(angle - 2.5) * self.size * 1.5)

        #desenez triunghiu
        pygame.draw.polygon(screen, self.color, [p1, p2, p3])