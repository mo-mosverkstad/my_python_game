class Game_status:
    GAME_CONTINUE = 0
    GAME_FAIL     = -1
    GAME_WIN      = 1
    GAME_DRAW     = 2

    def __init__(self):
        self.game_status = Game_status.GAME_CONTINUE

    def get_status(self): return self.game_status
    def set_status(self, status): self.game_status = status

class Game_text:
    def __init__(self, screen, font, text, color, pos):
        self.screen = screen
        self.font = font
        self.pos  = pos
        self.text = self.font.render(text, False, color)

    def draw(self):
        self.screen.blit(self.text, self.pos)