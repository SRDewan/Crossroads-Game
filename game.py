import pygame
import configparser
import math
import random
import sys

pygame.init()
pygame.font.init()

config = configparser.ConfigParser()
config.read('config.cfg')

screen = pygame.display.set_mode((1000, 800))
# creating a game surface 1000px x 800px

pygame.display.set_caption("Game")
# setting game screen caption


def msg(content, score):

    font = pygame.font.SysFont("Comic Sans MS", 72)
    text = font.render(config['msgs'][content], True, orange, dgreen)
    textRect = text.get_rect()
    textRect.center = (1000 // 2, 800 // 2)

    screen.blit(text, textRect)

    message = "Player " + str(pno) + " score = " + str(score)
    font = pygame.font.SysFont("Comic Sans MS", 52)
    text = font.render(message, True, orange, dgreen)
    textRect = text.get_rect()
    textRect.center = (1000 // 2, 900 // 2)

    screen.blit(text, textRect)

    font = pygame.font.SysFont("Comic Sans MS", 32)
    text = font.render(config['msgs']['key'], True, orange, dgreen)
    textRect = text.get_rect()
    textRect.center = (1000 // 2, 1000 // 2)

    screen.blit(text, textRect)


def disp(score, flg):

    if flg == 1:
        dtext = config['msgs']['score'] + str(score)
        font = pygame.font.SysFont("Comic Sans MS", 32)
        text = font.render(dtext, True, orange, dgreen)
        textRect = text.get_rect()
        textRect.center = (50, 20)

        return [text, textRect]

    elif flg == 2:

        screen.fill((0, 0, 0))

        if score[0] > score[1] or (score[0] == score[1] and score[2] > score[3]):
            btext = config['msgs']['winner1']

        elif score[0] < score[1] or (score[0] == score[1] and score[2] < score[3]):
            btext = config['msgs']['winner2']

        else:
            btext = config['msgs']['tie']

        font = pygame.font.SysFont("Comic Sans MS", 72)
        text = font.render(btext, True, orange, dgreen)
        textRect = text.get_rect()
        textRect.center = (1000 // 2, 800 // 2)

        screen.blit(text, textRect)

        stext1 = config['msgs']['p1score'] + str(score[2])

        font = pygame.font.SysFont("Comic Sans MS", 42)
        text = font.render(stext1, True, orange, dgreen)
        textRect = text.get_rect()
        textRect.center = (1000 // 2, 900 // 2)

        screen.blit(text, textRect)

        stext2 = config['msgs']['p2score'] + str(score[2])

        font = pygame.font.SysFont("Comic Sans MS", 42)
        text = font.render(stext2, True, orange, dgreen)
        textRect = text.get_rect()
        textRect.center = (1000 // 2, 1000 // 2)

        screen.blit(text, textRect)

        font = pygame.font.SysFont("Comic Sans MS", 32)
        text = font.render(config['msgs']['key'], True, orange, dgreen)
        textRect = text.get_rect()
        textRect.center = (1000 // 2, 1100 // 2)

        screen.blit(text, textRect)

        return

    if pno == 1:
        if pstatus[0] == 2:
            msg('w1', score)

        elif pstatus[1] == 2:
            msg('l1', score)
        else:
            msg('g', score)

    elif pno == 2:
        if pstatus[1] == 2:
            msg('w2', score)
        elif pstatus[0] == 2:
            msg('l2', score)
        else:
            msg('g', score)

    return


class Player:

    def __init__(self, location, x, y, winy):
        self.icon = pygame.image.load(location)
        self.x = x
        self.y = y
        self.newx = 0
        self.newy = 0
        self.winlx = x - 5
        self.winhx = x + 5
        self.winy = winy
        self. pts = 0

    def update(self, cross, pno):
        self.x += self.newx
        self.y += self.newy

        if self.x >= self.winlx and self.x <= self.winhx and self.y == self.winy:
            return 2

        if self.x <= -64:
            self.x = 1000

        elif self.x >= 1000:
            self.x = -63

        if self.y < 0:
            self.y = 0

        elif self.y > 768:
            self.y = 768

        self.points(cross, pno)

        return 0

    def setx(self, p):
        self.newx = p

    def sety(self, q):
        self.newy = q

    def points(self, cross, pno):
        for i in range(0, 3):
            for j in cross[i]:
                if j[0] == 0 and pno == 1 and (self.y + 32) <= j[1]:
                    self.pts += 5
                    j[0] = 1
                elif j[0] == 0 and pno == 2 and self.y >= j[1]:
                    self.pts += 5
                    j[0] = 1

        for i in range(3, 6):
            for j in cross[i]:
                if j[0] == 0 and pno == 1 and (self.y + 32) <= j[1]:
                    self.pts += 10
                    j[0] = 1
                elif j[0] == 0 and pno == 2 and self.y >= j[1]:
                    self.pts += 10
                    j[0] = 1


def collide(player_no, x, y, flag):
    distx = (player_no.x + 16) - (x + 16)
    distx *= distx
    disty = (player_no.y + 16) - (y + 16)
    disty *= disty
    dist = distx + disty
    dist = math.sqrt(dist)

    if dist < 27:
        flag = 1
        return 1

    return 0


class Fob:

    def __init__(self, name, low, high, ind):
        self.num = random.randrange(low, high)
        self.arr = []
        self.starty = self.rowno = self.flag = 0
        cross.append([])

        for i in range(0, self.num):

            cross[ind].append([0, self.starty])
            self.flag = 0

            while self.flag == 0:

                tempx = random.randrange(100, 937)

                for j in range(0, 32):
                    if available[self.rowno][tempx + j] == 1:
                        self.flag = 0
                        break
                    else:
                        self.flag = 1

                if self.flag == 1:
                    for j in range(0, 32):
                        available[self.rowno][tempx + j] = 1

            self.arr.append((pygame.image.load(name), tempx, self.starty))
            self.starty += 153
            ++self.rowno

            if self.starty > 765:
                self.starty = 0
                self.rowno = 0


class Mob:

    def __init__(self, name, low, high, itemno, ind):

        self.num = random.randrange(low, high)
        arr.append([])
        self.startx = random.randrange(-400, -32)
        self.starty = 32
        self.endy = 121
        self.rowno = 0
        cross.append([])

        for i in range(0, self.num):

            self.flag = store = 0

            tempy = random.randrange(self.starty, self.endy)
            cross[ind].append([0, tempy])

            for j in range(0, 32):
                if availabley[self.rowno][tempy + j - self.starty] != [0, 0]:
                    store = j
                    self.flag = 0
                    break
                else:
                    self.flag = 1

            if self.flag == 0:
                self.index = availabley[self.rowno][tempy +
                                                    store - self.starty][0] - 1
                tempi = availabley[self.rowno][tempy + store - self.starty][1]
                t = random.randrange(0, 3)
                t = 300 + t * 200
                self.startx = arr[tempi][self.index][1] - 500

            for j in range(0, 32):
                availabley[self.rowno][tempy + j -
                                       self.starty] = [i + 1, itemno]

            self.flag = 1

            arr[itemno].append([pygame.image.load(name), self.startx, tempy])
            self.starty += 153
            self.endy += 153
            self.rowno += 1

            if self.rowno > 4:
                self.starty = 32
                self.endy = 121
                self.rowno = 0

        itemno += 1

    def update(self, itemno, change):
        for i in range(0, self.num):
            arr[itemno][i][1] += (10 + change)

            if arr[itemno][i][1] >= 1000:
                arr[itemno][i][1] = -32


class Button():

    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, size=48):
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('Comic Sams MS', size)
            text = font.render(self.text, 1, black)
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                               self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True


class Iconpic():

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.num = 0

    def draw(self, loc):
        pygame.draw.rect(screen, (0, 0, 0),
                         (self.x, self.y, self.width, self.height), 0)
        self.icon = pygame.image.load(loc)
        screen.blit(self.icon, (self.x, self.y))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True


run = bool(config['global']['run'])


def func(flag, player_no, pno, tree, bush, log, fish, shark, boat):

    screen.fill(lblue)

    if event.type == pygame.KEYDOWN and flag == 0:
        if event.key == pygame.K_LEFT:
            player_no.setx(-5)
        elif event.key == pygame.K_RIGHT:
            player_no.setx(5)
        elif event.key == pygame.K_UP:
            player_no.sety(-5)
        elif event.key == pygame.K_DOWN:
            player_no.sety(5)

    elif event.type == pygame.KEYUP:
        player_no.setx(0)
        player_no.sety(0)

    if player_no.update(cross, pno) == 2:
        return 2

    for i in range(0, 765, 153):
        pygame.draw.rect(screen, black, (0, i, 1000, 32), 0)

    pygame.draw.rect(screen, black, (0, 765, 1000, 35), 0)

    pygame.draw.rect(screen, red, (484, 765, 32, 32), 0)
    pygame.draw.rect(screen, red, (484, 0, 32, 32), 0)

    tt = disp(player_no.pts, 1)

    screen.blit(tt[0], tt[1])

    for i in range(0, tree.num):
        screen.blit(tree.arr[i][0], (tree.arr[i][1], tree.arr[i][2]))
        flag = collide(player_no, tree.arr[i][1], tree.arr[i][2], flag)

        if flag == 1:
            return 1

    for i in range(0, bush.num):
        screen.blit(bush.arr[i][0], (bush.arr[i][1], bush.arr[i][2]))
        flag = collide(player_no, bush.arr[i][1], bush.arr[i][2], flag)

        if flag == 1:
            return 1

    for i in range(0, log.num):
        screen.blit(log.arr[i][0], (log.arr[i][1], log.arr[i][2]))
        flag = collide(player_no, log.arr[i][1], log.arr[i][2], flag)

        if flag == 1:
            return 1

    if pno == 1:
        change = change1
    else:
        change = change2

    fish.update(0, change)
    shark.update(1, change)
    boat.update(2, change)

    for i in range(0, fish.num):
        screen.blit(arr[0][i][0], (arr[0][i][1], arr[0][i][2]))
        flag = collide(player_no, arr[0][i][1], arr[0][i][2], flag)

        if flag == 1:
            return 1

    for i in range(0, shark.num):
        screen.blit(arr[1][i][0], (arr[1][i][1], arr[1][i][2]))
        flag = collide(player_no, arr[1][i][1], arr[1][i][2], flag)

        if flag == 1:
            return 1

    for i in range(0, boat.num):
        screen.blit(arr[2][i][0], (arr[2][i][1], arr[2][i][2]))
        flag = collide(player_no, arr[2][i][1], arr[2][i][2], flag)

        if flag == 1:
            return 1

    screen.blit(player_no.icon, (player_no.x, player_no.y))
    return 0


flag = 0

l1 = config['global']['l1']
l2 = config['global']['l2']

p1 = Player(l1, 484, 765, 0)
p2 = Player(l2, 484, 0, 765)

orange = eval(config.get('color', 'orange'), {}, {})
dgreen = eval(config.get('color', 'dark_green'), {}, {})
black = eval(config.get('color', 'black'), {}, {})
white = eval(config.get('color', 'white'), {}, {})
pink = eval(config.get('color', 'pink'), {}, {})
green = eval(config.get('color', 'green'), {}, {})
red = eval(config.get('color', 'red'), {}, {})
blue = eval(config.get('color', 'blue'), {}, {})
purple = eval(config.get('color', 'purple'), {}, {})
lblue = eval(config.get('color', 'light_blue'), {}, {})

color1 = red
color2 = color3 = green
color4 = dgreen

diff = Button(purple, 100, 100, 200, 50, 'DIFFICULTY')
easy = Button(red, 100, 200, 200, 50, 'NOOB')
medium = Button(green, 100, 300, 200, 50, 'AMATEUR')
hard = Button(green, 100, 400, 200, 50, 'PRO')
nextpg = Button(white, 400, 700, 200, 50, 'CONTINUE')
iconmsg = Button(purple, 524, 144, 450, 50, 'Select an icon for player 1')
picon = Iconpic(621, 244, 256, 256)
select = Button(dgreen, 524, 600, 450, 50, 'SELECT DISPLAYED ICON')
p1icon = Iconpic(711, 550, 32, 32)
p2icon = Iconpic(916, 550, 32, 32)
p1text = Button(pink, 550, 550, 160, 32, 'Player 1 Icon:')
p2text = Button(pink, 755, 550, 160, 32, 'Player 2 Icon:')

player_no = p1

pno = int(config['global']['pno'])
ino = int(config['global']['ino'])
prev = int(config['global']['prev'])
time = int(config['global']['time'])
ctr1 = int(config['global']['ctr1'])
ctr2 = int(config['global']['ctr2'])
pts1 = int(config['global']['pts1'])
pts2 = int(config['global']['pts2'])
change1 = int(config['global']['change1'])
change2 = int(config['global']['change2'])
c1 = int(config['global']['c1'])
c2 = int(config['global']['c2'])
page_no = int(config['global']['page_no'])

cross = []
pstatus = [2, 2]
cur = pygame.time.get_ticks()
tree = bush = log = fish = boat = shark = 0


while run:

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False

        elif page_no == 0 and event.type == pygame.MOUSEMOTION:
            if easy.isOver(pos):
                easy.color = red
            else:
                easy.color = color1

            if medium.isOver(pos):
                medium.color = red
            else:
                medium.color = color2

            if hard.isOver(pos):
                hard.color = red
            else:
                hard.color = color3

            if nextpg.isOver(pos):
                nextpg.color = blue
            else:
                nextpg.color = white

            if select.isOver(pos):
                select.color = red
            else:
                select.color = color4

        elif page_no == 0 and event.type == pygame.MOUSEBUTTONDOWN:

            if easy.isOver(pos):
                change1 = change2 = 0
                c1 = c2 = 0
                color1 = red
                color2 = green
                color3 = green

            elif medium.isOver(pos):
                change1 = change2 = 5
                c1 = c2 = 1
                color2 = red
                color1 = green
                color3 = green

            elif hard.isOver(pos):
                change1 = change2 = 10
                c1 = c2 = 2
                color3 = red
                color2 = green
                color1 = green

            elif nextpg.isOver(pos):
                page_no = 1

            elif picon.isOver(pos):
                picon.num += 1
                if picon.num == 3:
                    picon.num = 0

            elif select.isOver(pos):
                if l1 == 'icons/ghost.png':
                    l1 = 'icons/' + str(picon.num) + 's.png'
                    picon.num = 0

                else:
                    l2 = 'icons/' + str(picon.num) + 's.png'
                    picon.num = 0

    if page_no == 0:
        diff.draw()
        easy.draw()
        medium.draw()
        hard.draw()
        nextpg.draw()
        iconmsg.draw()
        picon.draw('icons/' + str(picon.num) + '.png')
        select.draw()
        p1text.draw(32)
        p1icon.draw(l1)
        p2text.draw(32)
        p2icon.draw(l2)

    if page_no == 1:

        if ino == 0:

            if pno == 1:
                player_no.__init__(l1, 484, 765, 0)
            else:
                player_no.__init__(l2, 484, 0, 765)

            available = []
            for i in range(0, 6):
                available.append([])

            for i in range(0, 1000):
                available[0].append(0)
                available[1].append(0)
                available[2].append(0)
                available[3].append(0)
                available[4].append(0)
                available[5].append(0)

                if (i >= 484 and i <= 516):
                    available[0][i] = 1
                    available[5][i] = 1

            availabley = []
            for i in range(0, 5):
                availabley.append([])

            for i in range(0, 121):
                availabley[0].append([0, 0])
                availabley[1].append([0, 0])
                availabley[2].append([0, 0])
                availabley[3].append([0, 0])
                availabley[4].append([0, 0])

            arr = []
            cross = []
            tree = Fob('icons/tree.png', 5, 8, 0)
            bush = Fob('icons/bush.png', 5, 8, 1)
            log = Fob('icons/log.png', 3, 6, 2)

            if pno == 1:
                c = c1
            else:
                c = c2

            fish = Mob('icons/ocean.png', 5 + c, 11 + c, 0, 3)
            shark = Mob('icons/shark.png', 5 + c, 11 + c, 1, 4)
            boat = Mob('icons/boat.png', 5 + c, 11 + c, 2, 5)

        ino = 1

        if flag == 0:
            flag = func(flag, player_no, pno, tree,
                        bush, log, fish, shark, boat)
            cur = pygame.time.get_ticks()
            time = (cur - prev) / 1000

        else:
            if pno == 1:

                if flag == 2:
                    ctr1 += 1
                    pstatus[0] = 2
                    disp(player_no.pts - time, 0)

                else:
                    pstatus[0] = 1
                    disp(player_no.pts - time, 0)

                if event.type == pygame.KEYDOWN:
                    pts1 += (player_no.pts - time)
                    prev = cur
                    change1 += 5
                    c1 += 1

                    if pstatus[1] == 2:
                        flag = 0
                        player_no = p2
                        pno = 2
                        ino = 0

                    elif pstatus[0] == 2:
                        flag = 0
                        player_no = p1
                        pno = 1
                        ino = 0

                    else:
                        disp([ctr1, ctr2, pts1, pts2], 2)
                        run = False

            elif pno == 2:

                if flag == 2:
                    ctr2 += 1
                    pstatus[1] = 2
                    disp(player_no.pts - time, 0)

                else:
                    pstatus[1] = 1
                    disp(player_no.pts - time, 0)

                if event.type == pygame.KEYDOWN:
                    pts2 += (player_no.pts - time)
                    prev = cur
                    change2 += 5
                    c2 += 1

                    if pstatus[0] == 2:
                        flag = 0
                        player_no = p1
                        pno = 1
                        ino = 0

                    elif pstatus[1] == 2:
                        flag = 0
                        player_no = p2
                        pno = 2
                        ino = 0

                    else:
                        disp([ctr1, ctr2, pts1, pts2], 2)
                        pygame.event.clear()

                        running = True
                        while running:
                            for e in pygame.event.get():
                                if e.type == pygame.KEYDOWN:
                                    running = False
                        run = False

    pygame.display.update()

    pygame.time.delay(40)

