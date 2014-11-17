from pygame import *
init()
my_font = font.SysFont("monospace", 20)


def load_image(name, colorkey=None):
    fullname = name
    try:
        loaded_image = image.load(fullname)
    except error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    loaded_image = loaded_image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = loaded_image.get_at((0,0))
        loaded_image.set_colorkey(colorkey, RLEACCEL)
    return loaded_image, loaded_image.get_rect()


class Pit(sprite.Sprite):

    def __init__(self, position):
        sprite.Sprite.__init__(self)
        self.count = 3
        self.position = position
        self.rect = Rect(position, (40, 40))

    def chosen(self):
        self.count += 1

    def update(self, background, pit):
        label = my_font.render(str(self.count), 1, (0, 0, 0))
        labelposx, labelposy = self.position
        labelposx += 20
        labelposy += 20
        draw.circle(background, (128, 50, 0), (labelposx, labelposy), 20)
        if self.count <= 10:
            background.blit(label, (labelposx-5, labelposy-10))
        else:
            background.blit(label, (labelposx-10, labelposy-10))


def main():
    screen = display.set_mode((1000, 800))
    display.set_caption('Click the Pits')
    mouse.set_visible(1)
    background = Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    screen.blit(background, (0, 0))
    display.flip()
    clock = time.Clock()
    pits = [None, None, None]
    for i in range(len(pits)):
        pits[i] = Pit((100*i, 0))
    while 1:
        clock.tick(60)
        for each in event.get():
            if each.type == QUIT:
                return
            elif each.type == KEYDOWN and each.key == K_ESCAPE:
                return
            elif each.type == MOUSEBUTTONDOWN:
                for i in pits:
                    if i.rect.collidepoint(mouse.get_pos()):
                        i.chosen()
        for m in pits:
            m.update(background, m)
        screen.blit(background, (0, 0))
        display.flip()

main()