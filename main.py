# use to create language game

import pygame, asyncio
import sys

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([800, 800])




async def main():

    #user's font
    base_font = pygame.font.Font(None, 32)
    user_text = ''

    #background
    background = pygame.image.load("background.jpg")

    #create rectangle
    input_rect = pygame.Rect(350, 375, 140, 32)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('darkgreen')
    color = color_passive

    active = False
    # more words: "tavolo", "forchetta", "cuore",

    #italian_word = ["che tempo fa", "e soleggiato", "noi dobbiamo", "tu puoi", "stanotte", "affollato", "sono stanca", "prezzo","cucchiaio", "ciotola", "il buio", "in fuga da", "uno starnuto", "la schiena", "mi prude", "apparecchio la tavola", "soltanto", "divano", "mettere"]
    #answer = ["what's the weather like", "it's sunny", "we must", "you can", "tonight", "crowded", "I'm tired", "price", "spoon", "bowl", "the dark", "on the run from", "a sneeze", "the back", "it itches me", "I set the table", "only", "sofa", "to put"]

    italian_word = ["hola", "ben", "espero", "que", "estas", "bien", "y", "no has", "olvidado", "tu espanol"]
    answer = ["hi", "ben", "I hope", "that","you are", "good", "and", "you haven't", "forgotten", "your spanish"]

    current_index = 0
    phase = 0
    end_time = 0
    score = 0
    total = 0

    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(background, (0,0))

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running =  False
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active =  False

            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        total += 1
                        if phase == 0:
                            if user_text.strip().lower() == answer[current_index].lower():
                                current_index += 1
                                user_text = ''
                                score +=1
                                if current_index >= len(italian_word):
                                    phase = 1
                                    current_index = 0
                            else:
                                screen.fill((200,0,0))
                                pygame.display.update()
                                user_text = ''
                                time = pygame.time.get_ticks()
                                while pygame.time.get_ticks() - time < 200:
                                    continue

                        elif phase == 1:
                            if user_text.strip().lower() == italian_word[current_index].lower():
                                current_index += 1
                                user_text = ''
                                score +=1
                                if current_index >= len(answer):
                                    end_time = pygame.time.get_ticks()
                            else:
                                screen.fill((200,0,0))
                                pygame.display.update()
                                user_text = ''
                                time = pygame.time.get_ticks()
                                while pygame.time.get_ticks() - time < 200:
                                    continue
                    else:
                        user_text += event.unicode



        if active:
            color = color_active
        else:
            color =  color_passive


        pygame.draw.rect(screen, color, input_rect, 2)
        text_surface = base_font.render(user_text, True, (255,255,255))
        screen.blit(text_surface, (input_rect.x +5, input_rect.y + 5))
        input_rect.w = max(100, text_surface.get_width() + 10)

        if phase == 0 and current_index < len(italian_word):
            italian_surface = base_font.render(f"Translate: {italian_word[current_index]}", True, (255, 255, 255))
            screen.blit(italian_surface, (300, 200))

        elif phase == 1 and current_index < len(answer):
            english_surface = base_font.render(f"Translate: {answer[current_index]}", True, (255, 255, 255))
            screen.blit(english_surface, (300, 200))

        else:
            end_surface = base_font.render("Congrats Ben, keep up the great work. Happy palindrome week!", True, (255, 255, 255))
            screen.blit(end_surface, (50, 200))
            rounded = round(score/total, 2)
            score_surface = base_font.render(f"Score: {rounded}", True, "white")
            screen.blit(score_surface, (50,50))
            if pygame.time.get_ticks() - end_time > 3000:
                running = False


        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)



        
asyncio.run(main())