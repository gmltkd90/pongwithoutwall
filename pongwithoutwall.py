import pygame, sys, time, random
from pygame.locals import*

def wait_for_player_to_press_key():
    pressed = False
    while not pressed:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                return  # start game for any other key down

def draw_text(text, font, surface, x, y):
    textobj = font.render(text, 1, WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = x, y
    surface.blit(textobj, textrect)

# Set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# Set up the window.
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Pong without Wall')
pygame.mouse.set_visible(False)

#color
WHITE = (255, 255, 255)

#dashed line
#pygame.draw.line(window_surface, WHITE, (200, 0), (200, 400), 1)

#paddles
PAD_LENGHTH = 100
PAD_SPEED = 3
PAD_WIDTH = 10

p_pad_y = 300
p_pad_x = 700

c_pad_y = 300
c_pad_x = 0


# score
p_score = 0
c_score = 0
p_point = 0
c_point = 0

#ball
BALL_RADIUS = 6
ball_speed_x = random.randint(2, 4)
ball_speed_y = random.randint(2, 4)
ball_x = 300
ball_y = 300



# Set up Keyboard
move_left = False
move_right = False
move_up = False
move_down = False

c_move_left = False
c_move_right = False
c_move_up = False
c_move_down = False

# sound
game_over_sound = pygame.mixer.Sound('losing.wav')
winning_sound = pygame.mixer.Sound('winning.wav')
beep_sound = pygame.mixer.Sound('beep.wav')

#bar image
bar_image = pygame.image.load('yellow.png')
side_bar = pygame.transform.scale(bar_image, (PAD_WIDTH, PAD_LENGHTH))
up_bar = pygame.transform.scale(bar_image, (PAD_LENGHTH, PAD_WIDTH))

play_game_again = True
while play_game_again:

    window_surface.fill(pygame.Color(0, 0, 0, 255))
    pygame.draw.line(window_surface, WHITE, (400, 0), (400, 50), )
    pygame.draw.line(window_surface, WHITE, (400, 100), (400, 150), )
    pygame.draw.line(window_surface, WHITE, (400, 200), (400, 250), )
    pygame.draw.line(window_surface, WHITE, (400, 300), (400, 350), )
    pygame.draw.line(window_surface, WHITE, (400, 400), (400, 450), )
    pygame.draw.line(window_surface, WHITE, (400, 500), (400, 550), )
    pygame.draw.circle(window_surface, WHITE, (ball_x, ball_y), BALL_RADIUS)

    sidebar = side_bar.get_rect()
    sidebar = sidebar.move((300, 400))

    window_surface.blit(side_bar, (WINDOWWIDTH - PAD_WIDTH, p_pad_y))
    window_surface.blit(up_bar, (p_pad_x, 0))
    window_surface.blit(up_bar, (p_pad_x, WINDOWHEIGHT - PAD_WIDTH))
    window_surface.blit(side_bar, (0, c_pad_y))
    window_surface.blit(up_bar, (c_pad_x, 0))
    window_surface.blit(up_bar, (c_pad_x, WINDOWHEIGHT - PAD_WIDTH))
    pygame.display.update()
    wait_for_player_to_press_key()

    play_game = True
    while c_point < 3 or p_point < 3:

        #computer event
        if ball_y > c_pad_y + 50:
            c_move_down = True
            c_move_up = False
        elif ball_y < c_pad_y + 50:
            c_move_up = True
            c_move_down = False

        if ball_x > c_pad_x + 50:
            c_move_right = True
            c_move_left = False
        elif ball_x < c_pad_x + 50:
            c_move_right = False
            c_move_left = True
        if ball_x > WINDOWWIDTH / 2:
            c_move_right = False
        if c_pad_x < 0:
            c_move_left = False

        #playeer event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    move_down = False
                    move_up = True
                if event.key == K_DOWN:
                    move_down = True
                    move_up = False
                if event.key == K_LEFT:
                    move_left = True
                    move_right = False
                if event.key == K_RIGHT:
                    move_left = False
                    move_right = True
            if event.type == pygame.KEYUP:
                if event.key == K_UP:
                    move_up = False
                if event.key == K_DOWN:
                    move_down = False
                if event.key == K_RIGHT:
                    move_right = False
                if event.key == K_LEFT:
                    move_left = False

        #player
        if move_up:
            p_pad_y -= PAD_SPEED
            if p_pad_y < 0:
                p_pad_y = 0
        elif move_down:
            p_pad_y += PAD_SPEED
            if p_pad_y > WINDOWHEIGHT - PAD_LENGHTH:
                p_pad_y = WINDOWHEIGHT - PAD_LENGHTH

        if move_right:
            p_pad_x += PAD_SPEED
            if p_pad_x + PAD_LENGHTH > WINDOWWIDTH:
                p_pad_x = WINDOWWIDTH - PAD_LENGHTH
        elif move_left:
            p_pad_x -= PAD_SPEED
            if p_pad_x < WINDOWWIDTH / 2:
                p_pad_x = WINDOWWIDTH / 2

        #computer
        if c_move_up:
            c_pad_y -= PAD_SPEED
            if c_pad_y < 0:
                c_pad_y = 0
        elif c_move_down:
            c_pad_y += PAD_SPEED
            if c_pad_y > WINDOWHEIGHT - PAD_LENGHTH:
                c_pad_y = WINDOWHEIGHT - PAD_LENGHTH

        if c_move_right:
            c_pad_x += PAD_SPEED
            if c_pad_x + PAD_LENGHTH > WINDOWWIDTH / 2:
                c_pad_x = (WINDOWWIDTH / 2) - PAD_LENGHTH
        elif c_move_left:
            c_pad_x -= PAD_SPEED
            if c_pad_x < 0:
                c_pad_x = 0


        #ball move
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        #ball position check

        if ball_x < WINDOWWIDTH / 2 and (ball_y < 0 + PAD_WIDTH or ball_y > WINDOWHEIGHT - PAD_WIDTH):
            if c_pad_x < ball_x < c_pad_x + PAD_LENGHTH:
                ball_speed_y = -ball_speed_y
                beep_sound.play()
            else:
                p_score += 1
                ball_x = 400
                ball_y = 300
                ball_speed_x = random.randint(2, 4)
                ball_speed_y = random.randint(2, 4)
        elif ball_x > WINDOWWIDTH / 2 and (ball_y < 0 + PAD_WIDTH or ball_y > WINDOWHEIGHT - PAD_WIDTH):
            if p_pad_x < ball_x < p_pad_x + PAD_LENGHTH:
                ball_speed_y = -ball_speed_y
                beep_sound.play()
            else:
                c_score += 1
                ball_x = 400
                ball_y = 300
                ball_speed_x = -random.randint(2, 4)
                ball_speed_y = -random.randint(2, 4)



        #point check
        if ball_x < 0 + PAD_WIDTH:
            if c_pad_y < ball_y < c_pad_y + PAD_LENGHTH:
                ball_speed_x = -ball_speed_x
                beep_sound.play()
            else:
                p_score += 1
                ball_x = 400
                ball_y = 300
                ball_speed_x = random.randint(2, 4)
                ball_speed_y = random.randint(2, 4)
        elif ball_x > WINDOWWIDTH - PAD_WIDTH:
            if p_pad_y < ball_y < p_pad_y + PAD_LENGHTH:
                ball_speed_x = -ball_speed_x
                beep_sound.play()
            else:
                c_score += 1
                ball_x = 400
                ball_y = 300
                ball_speed_x = -random.randint(2, 4)
                ball_speed_y = -random.randint(2, 4)

        if p_score >= 11 and p_score > c_score + 2:
            p_point += 1
            p_score = 0
            c_score = 0

        if c_score >= 11 and c_score > p_score + 2:
            c_point += 1
            p_score = 0
            c_score = 0

        if p_point == 3:
            play_game = False
            winning_sound.play()
            break
        if c_point == 3:
            play_game = False
            game_over_sound.play()
            break


        window_surface.fill(pygame.Color(0, 0, 0, 255))

        pygame.draw.line(window_surface, WHITE, (400, 0), (400, 50), )
        pygame.draw.line(window_surface, WHITE, (400, 100), (400, 150), )
        pygame.draw.line(window_surface, WHITE, (400, 200), (400, 250), )
        pygame.draw.line(window_surface, WHITE, (400, 300), (400, 350), )
        pygame.draw.line(window_surface, WHITE, (400, 400), (400, 450), )
        pygame.draw.line(window_surface, WHITE, (400, 500), (400, 550), )


        pygame.draw.circle(window_surface, WHITE, (ball_x, ball_y), BALL_RADIUS)

        window_surface.blit(side_bar, (WINDOWWIDTH - PAD_WIDTH, p_pad_y))
        window_surface.blit(up_bar, (p_pad_x, 0))
        window_surface.blit(up_bar, (p_pad_x, WINDOWHEIGHT - PAD_WIDTH))

        window_surface.blit(side_bar, (0, c_pad_y))
        window_surface.blit(up_bar, (c_pad_x, 0))
        window_surface.blit(up_bar, (c_pad_x, WINDOWHEIGHT - PAD_WIDTH))

        #score
        score_font = pygame.font.Font(None, 30)
        p_score_text = str(p_score)
        p_point_text = str(p_point)
        p_score_render = score_font.render(p_score_text, 1, WHITE)
        p_point_render = score_font.render(p_point_text, 1, WHITE)
        window_surface.blit(p_score_render, (550, 50))
        window_surface.blit(p_point_render, (550, 20))

        c_score_text = str(c_score)
        c_point_text = str(c_point)
        c_score_render = score_font.render(c_score_text, 1, WHITE)
        c_point_render = score_font.render(c_point_text, 1, WHITE)
        window_surface.blit(c_score_render, (150, 50))
        window_surface.blit(c_point_render, (150, 20))

        draw_text('score', score_font, window_surface, 50, 50)
        draw_text('point', score_font, window_surface, 50, 20)
        draw_text('score', score_font, window_surface, 450, 50)
        draw_text('point', score_font, window_surface, 450, 20)

        pygame.display.update()
        mainClock.tick(60)

    draw_text('GAME OVER', score_font, window_surface, WINDOWWIDTH / 3, WINDOWHEIGHT / 3)
    draw_text('Press a key to play again.', score_font, window_surface, WINDOWWIDTH / 3 - 80, WINDOWHEIGHT / 3 + 50)
    pygame.display.update()
    wait_for_player_to_press_key()
    c_point = 0
    p_point = 0

                

      

pygame.display.flip()
mainClock.tick(60)


