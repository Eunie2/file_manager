import pyxel as px


class App:
    def __init__(self):
        px.init(160, 120, title="Hello Pyxel")
        px.image(0).load(0, 0, "assets/pyxel_logo_38x16.png")
        px.run(self.update, self.draw)

    def update(self):
        if px.btnp(px.KEY_Q):
            px.quit()

    def draw(self):
        px.cls(0)
        px.text(55, 41, "Hello, Pyxel!", px.frame_count % 16)
        px.blt(61, 66, 0, 0, 0, 38, 16)


App()