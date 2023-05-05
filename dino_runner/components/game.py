import pygame
import time
import random

from dino_runner.utils.constants import MENU, BG, DEAD, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, RESET, DEFAULT_TYPE, DEAD, BG2, BG3, BG4, BG5
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import Obstacle_Manager
from dino_runner.components.obstacles.cloud import Cloud
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
HI_COLOR = pygame.Color(202, 197, 196)
SCORE_COLOR = pygame.Color(202, 197, 196)
half_screen_heigh = SCREEN_HEIGHT // 2
half_screen_width = SCREEN_WIDTH // 2

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.start_time = None
        self.time_elapsed = None
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 5
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_bg2 = 0
        self.y_pos_bg2 = 0
        self.x_pos_bg3 = 0
        self.y_pos_bg3 = 0
        self.x_pos_bg4 = 0
        self.y_pos_bg4 = 0
        self.x_pos_bg5 = 0
        self.y_pos_bg5 = 0
        

        self.player = Dinosaur()
        self.obstacle_manager = Obstacle_Manager()
        self.cloud = Cloud()
        self.running = False
        self.score = 0
        self.death_count = 0
        self.power_ups_manager = PowerUpManager()
        self.best_score = 0 
        
        

    def execute(self):
        self.running = True
        while self.running:
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.3)
            if not self.playing:
                self.game_over = True
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Base sequencial - Eventos - Updates - Draw
        self.reset_game()
        self.playing = True
        self.start_time = time.time()  # tempo em que o jogo começou
        while self.playing:
            self.events() 
            self.update()
            self.draw()
            self.time_elapsed = int(time.time() - self.start_time)  # tempo que passou desde o início do jogo

    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                
    def update(self):
        self.update_score()
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.cloud.update(self.game_speed)
        self.power_ups_manager.update(self)
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((132, 209, 186))
        self.draw_background5() #Parallax 4
        self.draw_background4() #Parallax 3
        self.draw_background3() #Parallax 2
        self.draw_background2() #Parallax 1
        self.draw_background()  #Track
        self.draw_score()
        self.draw_power_up_time()
        self.draw_time()  # exibe o tempo na tela
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.cloud.draw(self.screen)
        self.power_ups_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_time(self, x=10, y=10):
        global time_str
        time_str = time.strftime("%H:%M:%S", time.gmtime(self.time_elapsed))
        font = pygame.font.Font(FONT_STYLE, 22)
        time_surf = font.render(f"Tempo: {time_str}", True, SCORE_COLOR)
        self.screen.blit(time_surf, (x, y))

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def draw_background2(self):
        image_width2 = BG2.get_width()
        self.screen.blit(BG2, (self.x_pos_bg2, self.y_pos_bg2))
        self.screen.blit(BG2, (image_width2 + self.x_pos_bg2, self.y_pos_bg2))
        self.screen.blit(BG2, (2*image_width2 + self.x_pos_bg2, self.y_pos_bg2))
        if self.x_pos_bg2 <= -image_width2*0.5:
            self.screen.blit(BG2, (3*image_width2 + self.x_pos_bg2, self.y_pos_bg2))
            if self.x_pos_bg2 <= -image_width2:
                self.x_pos_bg2 = 0
        self.x_pos_bg2 -= self.game_speed - 2
    
    def draw_background3(self):
        image_width3 = BG3.get_width()
        self.screen.blit(BG3, (self.x_pos_bg3, self.y_pos_bg3))
        self.screen.blit(BG3, (image_width3 + self.x_pos_bg3, self.y_pos_bg3))
        self.screen.blit(BG3, (2*image_width3 + self.x_pos_bg3, self.y_pos_bg3))
        if self.x_pos_bg3 <= -image_width3*0.5:
            self.screen.blit(BG3, (3*image_width3 + self.x_pos_bg3, self.y_pos_bg3))
            if self.x_pos_bg3 <= -image_width3:
                self.x_pos_bg3 = 0
        self.x_pos_bg3 -= self.game_speed - 4
    
    def draw_background4(self):
        image_width4 = BG4.get_width()
        self.screen.blit(BG4, (self.x_pos_bg4, self.y_pos_bg4))
        self.screen.blit(BG4, (image_width4 + self.x_pos_bg4, self.y_pos_bg4))
        self.screen.blit(BG4, (2*image_width4 + self.x_pos_bg4, self.y_pos_bg4))
        if self.x_pos_bg4 <= -image_width4*0.5:
            self.screen.blit(BG4, (3*image_width4 + self.x_pos_bg4, self.y_pos_bg4))
            if self.x_pos_bg4 <= -image_width4:
                self.x_pos_bg4 = 0
        self.x_pos_bg4 -= self.game_speed - 6

    def draw_background5(self):
        image_width5 = BG5.get_width()
        self.screen.blit(BG5, (self.x_pos_bg5, self.y_pos_bg5))
        self.screen.blit(BG5, (image_width5 + self.x_pos_bg5, self.y_pos_bg5))
        self.screen.blit(BG5, (2*image_width5 + self.x_pos_bg5, self.y_pos_bg5))
        if self.x_pos_bg5 <= -image_width5*0.5:
            self.screen.blit(BG5, (3*image_width5 + self.x_pos_bg5, self.y_pos_bg5))
            if self.x_pos_bg5 <= -image_width5:
                self.x_pos_bg5 = 0
        self.x_pos_bg5 -= self.game_speed - 8

    def draw_score(self):
        self.generate_text(f"Pontuação: {self.score}", 910, 15, 20, SCORE_COLOR)
        self.generate_text(f"Melhor pontuação: {self.best_score}", 950, 35, 20, HI_COLOR)
        
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks())/1000, 2)
            if time_to_show >= 0:
                self.generate_text(
                    f'{self.player.type.capitalize()}, disponível por {time_to_show} segundos',
                    550,
                    50,  
                    18,
                    SCORE_COLOR,
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def update_score(self):
        self.score += 1

        if self.death_count >= 0:
            if self.score % 100 == 0 and self.game_speed < 700:
                self.game_speed += 1
        
        if self.score >= self.best_score:
            self.best_score = self.score  


    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def generate_text(self, text, half_screen_width, half_screen_heigh, size, color):
        
        font = pygame.font.Font(FONT_STYLE, size)
        text = font.render(f"{text}", True, color)
        text_rec = text.get_rect()
        text_rec.center = (half_screen_width, half_screen_heigh)
        self.screen.blit(text, text_rec)

    def show_menu(self):
        self.screen.fill((63, 67, 112))
        half_screen_heigh = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.screen.blit(MENU, (0, 0))
        else:
            self.generate_text("VOCÊ PERDEU!",  half_screen_width , half_screen_heigh - 220, 70, (41, 136, 145))
            
            self.generate_text(f"PERDAS: {self.death_count}", half_screen_width, half_screen_heigh - 30, 25, SCORE_COLOR)
            
            self.generate_text(f"PONTUAÇÃO: {self.score}",  half_screen_width, half_screen_heigh + 20, 25, SCORE_COLOR)
            
            self.generate_text(f"MELHOR PONTUAÇÃO: {self.best_score}", half_screen_width, half_screen_heigh + 70, 25, (255, 187, 0))
            
            self.generate_text(f"TEMPO DE SOBREVIVÊNCIA: {time_str}", half_screen_width, half_screen_heigh + 120, 25, SCORE_COLOR)
            
            self.generate_text("TECLE ALGO PARA REINICIAR", half_screen_width, half_screen_heigh + 180, 50, (41, 136, 145))
            
            self.screen.blit(DEAD, ( half_screen_width - 70, half_screen_heigh - 150))
            self.screen.blit(RESET, ( half_screen_width - 55, half_screen_heigh + 227))
       
        pygame.display.update()
        self.handle_events_on_menu()

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.score = 0
        self.game_speed = 20
        self.power_ups_manager.reset_power_ups()
        
