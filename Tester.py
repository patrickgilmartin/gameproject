import pygame
import uvage

LevelsScreen_images = uvage.load_sprite_sheet("LevelsScreen.png", 1, 1)  #Mario's fireball
LevelsScreen = uvage.from_image(400, 300, LevelsScreen_images[0])
LevelsScreen.width = 800
LevelScreen.height = 600

def run_game():
    class SpriteObject(pygame.sprite.Sprite):
        def __init__(self, x, y, color, radius):
            super().__init__()
            self.original_radius = radius
            self.radius = radius
            self.color = color
            self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
            pygame.draw.circle(self.image, color, (radius, radius), radius)
            self.rect = self.image.get_rect(center=(x, y))
            self.selected = False
        def update(self, event_list, last_selected):
            for event in event_list:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rect.collidepoint(event.pos):
                        if self.selected:
                            if event.button == 1:  # Check for a left-click
                                # Deselect the circle
                                self.selected = False
                                self.radius = self.original_radius
                                last_selected[0] = None
                        else:
                            # Select the circle
                            self.selected = True
                            self.radius += 2
                            if last_selected[0] is not None:
                                # Deselect the previous circle
                                last_selected[0].selected = False
                                last_selected[0].radius = last_selected[0].original_radius
                            last_selected[0] = self
            ring_radius = self.radius + 2
            self.image = pygame.Surface((2 * ring_radius, 2 * ring_radius), pygame.SRCALPHA)
            pygame.draw.circle(self.image, self.color, (ring_radius, ring_radius), self.radius)
            if self.selected:
                pygame.draw.circle(self.image, (255, 255, 0), (ring_radius, ring_radius), ring_radius, 4)
            self.rect = self.image.get_rect(center=self.rect.center)

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    circles = [
        {'color': (128, 0, 0), 'radius': 5, 'position': (148, 408)},
        {'color': (64, 64, 64), 'radius': 6, 'position': (148, 315)},
        {'color': (64, 64, 64), 'radius': 6.5, 'position': (148, 261)},
        {'color': (64, 64, 64), 'radius': 5, 'position': (102, 241)},
        {'color': (64, 64, 64), 'radius': 6, 'position': (239, 186)},
        {'color': (64, 64, 64), 'radius': 6, 'position': (285, 222)},
        {'color': (64, 64, 64), 'radius': 6, 'position': (355, 55)},
        {'color': (64, 64, 64), 'radius': 6, 'position': (490, 90)},
        {'color': (64, 64, 64), 'radius': 6, 'position': (560, 93)},
        {'color': (64, 64, 64), 'radius': 6, 'position': (675, 65)},
        {'color': (64, 64, 64), 'radius': 6, 'position': (678, 180)},
        {'color': (64, 64, 64), 'radius': 6, 'position': (679, 305)},
        {'color': (64, 64, 64), 'radius': 5, 'position': (588, 350)},
        {'color': (64, 64, 64), 'radius': 6, 'position': (583, 406)},
        {'color': (64, 64, 64), 'radius': 6, 'position': (514, 502)},
        {'color': (64, 64, 64), 'radius': 6, 'position': (468, 502)},
        {'color': (64, 64, 64), 'radius': 6, 'position': (400, 502)},
        {'color': (64, 64, 64), 'radius': 6, 'position': (308, 482)},
        {'color': (64, 64, 64), 'radius': 9, 'position': (353, 427)}
    ]

    circle_sprites = pygame.sprite.Group()
    last_selected = [None]
    for circle_data in circles:
        color = circle_data['color']
        radius = circle_data['radius']
        position = circle_data['position']
        circle = SpriteObject(position[0], position[1], color, radius)
        circle_sprites.add(circle)
    running = True
    while running:
        event_list = pygame.event.get()  # Get the events
        for event in event_list:
            if event.type == pygame.QUIT:
                running = False
        circle_sprites.update(event_list, last_selected)
        screen.fill((LevelsScreen))
        circle_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()

