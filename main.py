import pygame
import Button as Button
import CollisionDetection as Collision
import Particle
import Sound

def main():
    pygame.init()
    screen = pygame.display.set_mode((1600, 800))
    pygame.display.set_caption("My Game Engine")
    clock = pygame.time.Clock()

    crash_sound = Sound.Sound()
    sound_interval = 300 # 사운드 재생 간격 0.3초 (300ms)
    last_sound_time = 0


    # 파티클 생성
    particle_system = Particle.ParticleSystem()

    # 두 AABB 생성
    rect1 = Collision.AABB(x=600, y=400, width=100, height=100)
    rect2 = Collision.AABB(x=800, y=400, width=150, height=150)
    
    # font
    font = pygame.font.Font(None, 36)
    
    # set_collision_enabled 버튼 생성 
    enable_button = Button.Button(
        x=1200 , y=100, width=300, height=50,
        text="set collision enabled"
    )
    disable_button = Button.Button(
        x=1200, y=200, width=300, height=50,
        text="set collision disabled"
    )
    is_collide = "enabled"

    # sound 버튼 생성
    sound1_button = Button.Button(
        x=1200, y=300, width=300, height=50,
        text="Crash sound 1"
    )
    sound2_button = Button.Button(
        x=1200, y=400, width=300, height=50,
        text="Crash sound 2"
    )
    sound_name = "1"

    # 파티클 버튼 생성
    particle_on_button = Button.Button(
        x=1200, y=500, width=300, height=50,
        text="particle ON"
    )
    particle_off_button = Button.Button(
        x=1200, y=600, width=300, height=50,
        text="particle OFF"
    )
    is_particle_activate = "Activated"

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 키 입력으로 rect1 이동
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rect1.x -= 2
        if keys[pygame.K_RIGHT]:
            rect1.x += 2
        if keys[pygame.K_UP]:
            rect1.y -= 2
        if keys[pygame.K_DOWN]:
            rect1.y += 2

        # 충돌 감지
        collision = Collision.is_colliding_aabb(rect1, rect2)

        # 시간 측정 (사운드)
        current_time = pygame.time.get_ticks()

        # 화면 그리기
        screen.fill((0, 0, 0))
        rect1.draw(screen)
        rect2.draw(screen)

        # 버튼 그리기
        enable_button.draw(screen)
        disable_button.draw(screen)
        sound1_button.draw(screen)
        sound2_button.draw(screen)
        particle_on_button.draw(screen)
        particle_off_button.draw(screen)

        # 상단 정보 표시
        text_collision = font.render("Set Collision {0}".
                                     format(is_collide), True, 
                                     (255,255,255))
        screen.blit(text_collision, (700, 50))
        
        text_sound = font.render("Crash Sound {0}".
                                     format((sound_name)), True, 
                                     (255,255,255))
        screen.blit(text_sound, (700, 100))

        text_particle = font.render("Particle System {0}".
                                     format(is_particle_activate), True, 
                                     (255,255,255))
        screen.blit(text_particle, (700, 150))
                    
                    

        # 버튼 이벤트 처리
        if enable_button.input_event(event):
            is_collide = "Enabled"
            rect1.set_collision_enabled(True)

        if disable_button.input_event(event):
            is_collide = "Disabled"
            rect1.set_collision_enabled(False)

        if sound1_button.input_event(event):
            sound_name = "1"
            sound_interval = 300
            crash_sound.selecte_sound("Sound 1")
        
        if sound2_button.input_event(event):
            sound_name = "2"
            sound_interval = 1000
            crash_sound.selecte_sound("Sound 2")

        if particle_on_button.input_event(event):
            is_particle_activate = "Activated"
            particle_system.is_activate = True
        
        if particle_off_button.input_event(event):
            is_particle_activate = "DeActivated"
            particle_system.is_activate = False

        # 충돌 시 처리
        if collision:
            text_surface = font.render("Collision Detected!!!", True, (255,255,255))
            screen.blit(text_surface, (700, 600))

            if (current_time - last_sound_time) > sound_interval: # 사운드
                crash_sound.play_sound() 
                last_sound_time = current_time
            
            if particle_system.is_activate: # 파티클 시스템
                particle_system.create_particles(rect1.x , 
                                             rect1.y , 
                                             count=20)
                particle_system.update()
                particle_system.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()