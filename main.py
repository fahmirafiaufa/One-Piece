import pygame

#mengatur Ukuran Layar
screen_width = 600
screen_height = 600
screen_title = 'Game Gabut'

clock = pygame.time.Clock()

#mengatur Warna Background
white_color = (255, 255, 255)
balck_color = (0, 0, 0)
pygame.font.init()
font = pygame.font.SysFont('ComicSans', 75)

class Game :
    Tict_rate = 60

    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        #menampilkan screen
        self.game_screen = pygame.display.set_mode((screen_width, screen_height))
        self.game_screen.fill(white_color)

        pygame.display.set_caption(screen_title)
        background_gambar = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_gambar, (width, height))

    def run_game_loop(self, level_cepat):
        is_game_over = False
        menang = False
        direction = 0

        player_1 = CharakterPlayer('asset/pemain.png', 284, 500, 30, 30)
        musuh_1 = CharakterMusuh('asset/musuh1.png', 20, 400, 30, 30)
        musuh_1.speed *= level_cepat

        musuh_2 = CharakterMusuh('asset/musuh2.png', self.width - 40, 150, 30, 30)
        musuh_2.speed *= level_cepat

        musuh_3 = CharakterMusuh('asset/musuh3.png', 20, 90, 30, 30)
        musuh_3.speed *= level_cepat

        Onepiece = GameObject('asset/onepiece.png', 284, 35, 35, 35)

        while not is_game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_UP :
                        direction = 1
                    elif event.key == pygame.K_DOWN :
                        direction = -1
                elif event.type == pygame.KEYUP :
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                        direction = 0
                print(event)

            self.game_screen.fill(white_color)
            self.game_screen.blit(self.image, (0, 0))
            Onepiece.draw(self.game_screen)

            player_1.move(direction, self.height)
            player_1.draw(self.game_screen)

            musuh_1.move(self.width)
            musuh_1.draw(self.game_screen)

            if level_cepat > 1.5 :
                musuh_2.move(self.width)
                musuh_2.draw(self.game_screen)
            if level_cepat > 2 :
                musuh_3.move(self.width)
                musuh_3.draw(self.game_screen)

            if player_1.nabrak(musuh_1):
                is_game_over = True
                menang = False
                text = font.render('NT LURR :((', True, balck_color)
                self.game_screen.blit(text, (150, 250))
                pygame.display.update()
                clock.tick(1)
                break
            elif player_1.nabrak(Onepiece) :
                is_game_over = True
                menang = True
                text = font.render('Lu Menang Ngab :D', True, balck_color)
                self.game_screen.blit(text, (55, 250))
                pygame.display.update()
                clock.tick(1)
                break

            pygame.display.update()
            clock.tick(self.Tict_rate)

        if menang :
            self.run_game_loop(level_cepat + 0.8)
        else:
            return

class GameObject :
    def __init__(self, image_path, x, y, width, height):
        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

        objectPlayer= pygame.image.load(image_path)
        self.Player = pygame.transform.scale(objectPlayer, (width, height))

    def draw(self, background):
        background.blit(self.Player, (self.x_pos, self.y_pos))

class CharakterPlayer(GameObject) :

    speed = 10
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, direction, max_height):
        if direction > 0 :
            self.y_pos -= self.speed
        elif direction < 0 :
            self.y_pos += self.speed

        if self.y_pos <= max_height - 530 :
            self.y_pos = max_height - 530

    def nabrak(self, orang_lain):
        if self.y_pos > orang_lain.y_pos + orang_lain.height:
            return False
        elif self.y_pos + self.height < orang_lain.y_pos:
            return False
        if self.x_pos > orang_lain.x_pos + orang_lain.width:
            return False
        elif self.x_pos + self.width < orang_lain.x_pos:
            return False

        return True

class CharakterMusuh(GameObject) :

    speed = 10
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, max_width):
        if self.x_pos <= 20 :
            self.speed = abs(self.speed)
        elif self.x_pos >= max_width - 40 :
            self.speed= -abs(self.speed)
        self.x_pos += self.speed

pygame.init()
new_game = Game('asset/background.png',screen_title, screen_width, screen_height)
new_game.run_game_loop(1)
pygame.quit()
quit()



# pygame.draw.rect(game_screen, balck_color, [200, 200, 70, 70] )
# pygame.draw.circle(game_screen, balck_color, (200, 100), 40)