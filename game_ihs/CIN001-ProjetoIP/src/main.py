import pygame
import sys
from level import Level
from PIL import Image, ImageFilter
from settings import *
from integracao import *
import time

YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

class Game:
    def __init__(self, io):
        pygame.init()
        self.screen = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption('FRAGM')
        self.clock = pygame.time.Clock()
        self.io = io
        self.level = Level(self.io)
       
        pygame.mixer.music.load("../assets/gameplay/sounds/fundo.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
   
    def draw_text(self, text, font, color, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect(topleft=(x, y))
        self.screen.blit(textobj, textrect)
   
    def run(self):
        font = pygame.font.Font(None, 36)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_p:
                        take_screenshot(self.screen)
           
            self.screen.fill('white')
            self.level.run()
           
            x_offset = LARGURA - 120
            y_offset = 10
            spacing = 40

            score = self.level.collected_items.get('pieces', 0)
            score_text = str(score).zfill(4)
            self.io.put_DP(1, score_text)
           
            led_list = list(range(score))
            self.io.put_ar_LD(led_list)
           
            for item, count in self.level.collected_items.items():
                self.draw_text(f"{item.capitalize()}: {count}", font, YELLOW, x_offset, y_offset)
                y_offset += spacing
           
            timer_int = int(self.level.timer)
            timer_text_display = str(timer_int).zfill(4)
            self.io.put_DP(0, timer_text_display)
           
            timer_text_screen = f"Time: {timer_int}"
            self.draw_text(timer_text_screen, font, YELLOW, x_offset, y_offset + spacing)
           
            pygame.display.update()
            self.clock.tick(FPS)

def take_screenshot(screen):
    screenshot = pygame.Surface(screen.get_size())
    screenshot.blit(screen, (0, 0))
    pygame.image.save(screenshot, f"screenshot_{pygame.time.get_ticks()}.png")

def apply_blur(image_path, blur_radius=10):
    image = Image.open(image_path)
    blurred_image = image.filter(ImageFilter.GaussianBlur(blur_radius))
    return pygame.image.fromstring(blurred_image.tobytes(), blurred_image.size, blurred_image.mode)

def about_screen(game, io):
    font = pygame.font.Font(None, 74)
    about_image = pygame.image.load("../assets/gameplay/about.png").convert_alpha()
    about_image = pygame.transform.scale(about_image, (LARGURA, ALTURA))
   
    prev_pb1_state = 1
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        current_pb1_state = io.get_PB(1)
        if prev_pb1_state == 0 and current_pb1_state == 1:
            return
        prev_pb1_state = current_pb1_state

        game.screen.blit(about_image, (0, 0))
        game.draw_text("Pressione ESC ou Botao 1 para voltar", font, WHITE, LARGURA // 2 - 400, ALTURA - 100)
       
        pygame.display.update()
        game.clock.tick(FPS)

def main_menu():
    io = IO()
    game = Game(io)
    font = pygame.font.Font(None, 74)
   
    background_image = pygame.image.load("../assets/gameplay/FRAGMENTADO.png").convert_alpha()
    background_image = pygame.transform.scale(background_image, (LARGURA, ALTURA))
   
    options = ["START", "ABOUT", "QUIT"]
    selected_option = 0
   
    prev_pb_states = [1, 1, 1, 1]

    while True:
        game.screen.blit(background_image, (0, 0))
       
        start_y = ALTURA // 2 + 50
        spacing = 60
       
        for i, option in enumerate(options):
            if i == selected_option:
                game.draw_text(">", font, WHITE, LARGURA // 2 - 130, start_y + i * spacing)
            game.draw_text(option, font, WHITE, LARGURA // 2 - 100, start_y + i * spacing)

        current_pb_states = [io.get_PB(i) for i in range(4)]
       
        if prev_pb_states[3] == 0 and current_pb_states[3] == 1:
            selected_option = (selected_option - 1) % len(options)
       
        if prev_pb_states[2] == 0 and current_pb_states[2] == 1:
            selected_option = (selected_option + 1) % len(options)
           
        if prev_pb_states[1] == 0 and current_pb_states[1] == 1:
            if options[selected_option] == "START":
                game.run()
            elif options[selected_option] == "ABOUT":
                about_screen(game, io)
            elif options[selected_option] == "QUIT":
                pygame.quit()
                sys.exit()

        prev_pb_states = current_pb_states

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if options[selected_option] == "START":
                        game.run()
                    elif options[selected_option] == "ABOUT":
                        about_screen(game, io)
                    elif options[selected_option] == "QUIT":
                        pygame.quit()
                        sys.exit()
                elif event.key == pygame.K_p:
                    take_screenshot(game.screen)
       
        pygame.display.update()
        game.clock.tick(FPS)

if __name__ == '__main__':
    main_menu()
