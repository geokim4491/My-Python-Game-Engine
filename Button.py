import pygame
import sys

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.text_color = (255, 255, 255)
        self.button_color = (0, 128, 255)
        self.hover_color = (0, 255, 128)
        self.clicked = False

    def draw(self, screen):
        """
        버튼을 화면에 그립니다.
        """
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.button_color
        pygame.draw.rect(screen, color, self.rect)

        # 텍스트 렌더링
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    
    def input_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 왼쪽 버튼 클릭
            if self.rect.collidepoint(event.pos) and not self.clicked:
                self.clicked = True
                return True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # 왼쪽 버튼 떼기
            self.clicked = False

        return False
    
    def print_input(self, screen, text):
        text_surface = self.font.render(self.text, True, self.text_color)
        screen.blit(text_surface, (800, 100))
    