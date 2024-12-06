import pygame
import random

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(2, 6)  # 파티클 크기
        self.color = (random.randint(200, 255), random.randint(100, 200), random.randint(100, 200))  # 랜덤 색상
        self.vx = random.uniform(-2, 2)  # 속도 x
        self.vy = random.uniform(-2, 2)  # 속도 y
        self.gravity = 0.1  # 중력 효과
        self.life = random.randint(20, 40)  # 수명 (프레임 단위)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += self.gravity  # 중력 적용
        self.life -= 1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

# 파티클 시스템
class ParticleSystem:
    def __init__(self):
        self.particles = []
        self.is_activate = True

    def create_particles(self, x, y, count=20):
        for _ in range(count):
            self.particles.append(Particle(x, y))

    def update(self):
        for particle in self.particles[:]:
            particle.update()
            if particle.life <= 0:
                self.particles.remove(particle)

    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)
