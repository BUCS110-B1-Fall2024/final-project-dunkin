import pygame
from src.game_controller import GameController

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Food Click Game")
clock = pygame.time.Clock()

images = {
    "donut": pygame.transform.scale(pygame.image.load("assets/donut.png"), (50, 50)),
    "bread": pygame.transform.scale(pygame.image.load("assets/bread.png"), (50, 50)),
    "fork": pygame.transform.scale(pygame.image.load("assets/fork.png"), (50, 50)),
    "knife": pygame.transform.scale(pygame.image.load("assets/knife.png"), (50, 50)),
}
gift_image = pygame.transform.scale(pygame.image.load("assets/gift.png"), (50, 50))

controller = GameController(screen)
controller.add_items(images)

start_ticks = pygame.time.get_ticks()
running = True

while running:
    screen.fill((135, 206, 235))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            controller.handle_click(event.pos)

    controller.update()

    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    if int(seconds) % 4 == 0 and int(controller.time_elapsed) != int(seconds):
        controller.score -= 1
        controller.time_elapsed = seconds

    if int(seconds) % 10 == 0 and seconds < 30:
        for item in controller.items:
            item.speed = min(item.speed + 0.5, 5)
        controller.gift.speed = min(controller.gift.speed + 0.5, 5)

    if controller.score <= 0 or seconds >= 30:
        running = False

    controller.render(images, gift_image)

    score_text = pygame.font.Font(None, 36).render(f"Score: {controller.score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

screen.fill((135, 206, 235))
game_over_text = pygame.font.Font(None, 72).render("Game Over", True, (255, 0, 0))
final_score_text = pygame.font.Font(None, 48).render(f"Final Score: {controller.score}", True, (0, 0, 0))
screen.blit(game_over_text, (300, 250))
screen.blit(final_score_text, (300, 320))
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()


