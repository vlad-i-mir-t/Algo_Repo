from pygame import *
from random import *
lost = 0
shoots = 0
class gamesprite(sprite.Sprite):
    def __init__(self, speed, pimage, rect_x, rect_y, size_x, size_y):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(pimage), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class player(gamesprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x  > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 635:
            self.rect.x += self.speed
    def fire(self):
        sprite_bullet1 = bullet(10, 'bullet.png', self.rect.centerx, self.rect.top, 15, 25
        )
        bult.add(sprite_bullet1)
class enemy(gamesprite):
    def update(self):
        global lost 
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.rect.y = -50
            self.rect.x = randint(0, 620)
            lost += 1
    
class asteroid(gamesprite):        
    def update(self):
            global lost 
            self.rect.y += self.speed
            if self.rect.y >= 500:
                self.rect.y = -50
                self.rect.x = randint(0, 620)





class bullet(gamesprite):
    def update(self): 
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()
        


font.init()
font = font.SysFont(None, 35)

shoot = font.render('Cчет:' + str(shoots), True,  (255, 255, 255 ))
lose = font.render('Пропущено:' + str(lost), True,  (255, 255, 255 ))
win = font.render('Проиграл', True,  (255, 255, 255 ))
not_win = font.render('Выиграл', True,  (255, 255, 255 ))

bult = sprite.Group()
ens = sprite.Group()
ast = sprite.Group()
window = display.set_mode((700, 500))
display.set_caption('Шутер')
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
sprite_rocket = player(10, 'rocket.png', 250, 400, 80, 100)
for i in range(1, 6):
    sprite_enemy = enemy(randint(1, 5), 'ufo.png', randint(80, 620), -50, 80, 50)
    ens.add(sprite_enemy)
for i in range(1, 6):
    sprite_asteroid = enemy(randint(1, 5), 'asteroid.png', randint(80, 620), -50, 80, 50)
    ast.add(sprite_asteroid)
sprite_bullet = bullet(10, 'bullet.png', 250, 400, 15, 25)
bult.add(sprite_bullet)
game = True
finish = False 
clock = time.Clock()
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        if i.type == KEYDOWN and i.key == K_SPACE:
                sprite_rocket.fire()
    if finish != True:
        window.blit(background, (0, 0))

        sprite_rocket.update()
        sprite_rocket.reset()
        lose = font.render('Пропущено:' + str(lost), True,  (255, 255, 255 )) 
        window.blit(lose, (0, 0))
        shoot = font.render('Cчет:' + str(shoots), True,  (255, 215, 0 ))
        window.blit(shoot, (0, 50))
        ens.update()
        bult.update()
        bult.draw(window)
        ens.draw(window)
        ast.draw(window)
        ast.update()
        sprites_list = sprite.groupcollide(bult, ens, True, True)
        sprites_list1 = sprite.groupcollide(bult, ast, True, False)
        sprites_list2 = sprite.spritecollide(sprite_rocket, ast, True, False)
        for c in sprites_list:
            shoots += 1
            sprite_enemy = enemy(randint(1, 5), 'ufo.png', randint(80, 620), -50, 80, 50)
            ens.add(sprite_enemy)
    for q in sprites_list2:
        window.blit(win, (250, 250))
        finish = True
    if shoots >= 15:
        window.blit(not_win, (250, 250))
        finish = True
    
    if lost >= 5 :
        window.blit(win, (250, 250))
        finish = True
    
    display.update()
    clock.tick(60)
    
    
    