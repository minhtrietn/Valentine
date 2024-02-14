import os
from random import *
from pygame import *


class LOVE_vl:
    def __init__(self):
        self.r = True
        self.w = Vector2(1000, 1000)
        self.b = Vector2(200, 100)
        self.chu = [80, 80]

    def box_chon(y):
        y.yes_b = Vector2(y.b.x, y.b.y)
        y.no_b = Vector2(y.b.x, y.b.y)
        y.b_yes = Vector2(y.w.x // 2 - (3 / 2) * y.b.x, y.w.y // 2 + (3 / 2) * y.b.y)
        y.b_no = Vector2(y.w.x // 2 + y.b.x // 2, y.w.y // 2 + (3 / 2) * y.b.y)
        y.chu_yes = Vector2(y.b_yes.x + y.yes_b.x // 2 - 50, y.b_yes.y + y.yes_b.y // 4)
        y.chu_no = Vector2(y.b_no.x + y.b.x // 2 - 50, y.b_no.y + y.b.y // 4)


class LOVE(LOVE_vl):
    def __init__(self):
        init()
        super().__init__()
        self.box_chon()
        self.scr = display.set_mode((self.w.x, self.w.y))
        self.cl = "black"
        self.clchu = "white"
        self.tim = self.timmouse = "red"
        self.d = 0
        self.dr_scr = True
        self.a = Rect([420, 200, 500, 150])
        self.p = 0

    def mes_mouse(ms):
        ms.d = -1
        B = Vector2(1, 2)
        M = Vector2(ms.m.x - 29 * B.x // 2, ms.m.y - 6 * B.y // 2)
        for i in range(2):
            draw.rect(ms.scr, Color(ms.timmouse), [M.x + (3 - 2 * i) * B.x, M.y + i * B.y, (9 + 4 * i) * B.x, B.y])
            draw.rect(ms.scr, Color(ms.timmouse),
                      [M.x + (3 - 2 * i) * B.x + (9 + 4 * i) * B.x + (5 - 4 * i) * B.x, M.y + i * B.y,
                       (9 + 4 * i) * B.x, B.y])
        for i in range(3):
            draw.rect(ms.scr, Color(ms.timmouse), [M.x, (M.y + 2 * B.y) + i * B.y, 29 * B.x, B.y])
        for i in range(7):
            draw.rect(ms.scr, Color(ms.timmouse),
                      [M.x + (3 + 2 * ms.d) * B.x, (M.y + 5 * B.y) + i * B.y, B.x * (23 - 4 * ms.d), B.y])
            ms.d += 1

    def main(m):
        for m.e in event.get():
            if m.e.type == KEYDOWN:
                if m.e.key == K_g: m.r = False
            if m.e.type == MOUSEBUTTONDOWN:
                if m.dr_byes.collidepoint(m.e.pos):
                    m.dr_scr = False
                if m.dr_scr == False and m.a.collidepoint(m.e.pos):
                    m.r = False
                if m.dr_bno.collidepoint(m.e.pos):
                    m.yes_b.x += 100
                    m.yes_b.y += 100
                    m.b_yes.x -= 25
                    m.b_yes.y -= 50
                    m.chu[0] += 20
                    m.b_no.x = randint(m.b_yes.x + m.yes_b.x, m.w.x) - 5
                    m.b_no.y = randint(m.no_b.y, m.w.y - 3 * m.no_b.y)
                    m.chu[1] -= 5
                    m.no_b.x -= 5
                    m.no_b.y -= 5
                    m.d += 1
                    m.p += 1
            if m.dr_bno.collidepoint(m.m): m.timmouse = "white"
            if m.dr_byes.collidepoint(m.m): m.timmouse = "red"
            if m.a.collidepoint(m.m) and m.dr_scr == False: m.timmouse = "green"

    def dr_yes(dy):
        dy.u = [
            "ban lam ny minh nhe ❤ ", "tai sao ban lai tu choi:((", "nooo", "dong y di moa =(( ",
            "dung phu phang nhu the 🙁", "noo",
            "bam yes đi", "dung bam no", "cau dong y di ma  =(( ", "dong y ikkk =(( ", "why???", "huhu",
        ]
        dy.scr.blit(font.SysFont(None, 50).render(dy.u[dy.p], True, Color("red")), [330, 200])
        if dy.d == 3:
            dy.dr_byes = Rect(dy.b_no.x, dy.b_no.y, dy.no_b.x, dy.no_b.y)
            draw.rect(dy.scr, Color(dy.cl), dy.dr_byes)
            dy.scr.blit(font.SysFont(None, dy.chu[1]).render(f"yes", True, Color(dy.clchu)),
                        [dy.b_no.x + dy.b.x // 2 - 50, dy.b_no.y + dy.b.y // 4])
        else:
            dy.dr_byes = Rect(dy.b_yes.x, dy.b_yes.y, dy.yes_b.x, dy.yes_b.y)
            draw.rect(dy.scr, Color(dy.cl), dy.dr_byes)
            dy.scr.blit(font.SysFont(None, dy.chu[0]).render(f"yes", True, Color(dy.clchu)), dy.chu_yes)

    def dr_no(dy):
        if dy.d == 3:
            dy.dr_bno = Rect(dy.b_yes.x, dy.b_yes.y, dy.yes_b.x, dy.yes_b.y)
            draw.rect(dy.scr, Color(dy.cl), dy.dr_bno)
            dy.scr.blit(font.SysFont(None, dy.chu[0]).render(f"no", True, Color(dy.clchu)), dy.chu_yes)
        else:
            dy.dr_bno = Rect(dy.b_no.x, dy.b_no.y, dy.no_b.x, dy.no_b.y)
            draw.rect(dy.scr, Color(dy.cl), dy.dr_bno)
            dy.scr.blit(font.SysFont(None, dy.chu[1]).render(f"no", True, Color(dy.clchu)),
                        [dy.b_no.x + dy.b.x // 2 - 50, dy.b_no.y + dy.b.y // 4])

    def dr_hr(h):
        h.d = -1
        B = Vector2(5, 10)
        M = Vector2(h.w.x // 2 - 29 * B.x // 2, 250)
        for i in range(2):
            draw.rect(h.scr, Color(h.tim), [M.x + (3 - 2 * i) * B.x, M.y + i * B.y, (9 + 4 * i) * B.x, B.y])
            draw.rect(h.scr, Color(h.tim),
                      [M.x + (3 - 2 * i) * B.x + (9 + 4 * i) * B.x + (5 - 4 * i) * B.x, M.y + i * B.y,
                       (9 + 4 * i) * B.x, B.y])
        for i in range(3):
            draw.rect(h.scr, Color(h.tim), [M.x, (M.y + 2 * B.y) + i * B.y, 29 * B.x, B.y])
        for i in range(7):
            draw.rect(h.scr, Color(h.tim),
                      [M.x + (3 + 2 * h.d) * B.x, (M.y + 5 * B.y) + i * B.y, B.x * (23 - 4 * h.d), B.y])
            h.d += 1

    def end(h):
        h.scr.fill(Color("white"))
        h.scr.blit(font.SysFont(None, 50).render("        yeu ban nhieu nhieu ❤ ", True, Color("red")), [330, 200])
        h.scr.blit(font.SysFont(None, 20).render("     bam vào giua trai tim đe thoat ❤ ", True, Color("red")), h.m)
        h.dr_hr()

    def run(r):
        while r.r:
            r.m = Vector2(mouse.get_pos())
            r.scr.fill(Color("white"))
            if r.dr_scr:
                r.dr_yes()
                r.dr_no()
            else:
                r.end()
            r.main()
            r.dr_hr()
            r.mes_mouse()
            display.update()


LOVE().run()


def _(d1, d2, d3, d4, d5): return d1 * " " + d2 * " " + d3 * "" + d4 * " " + d5 * "*"


n = 10
f = open("love.out", "w", encoding="utf-8")
f.write(5 * "\n")
for i in range(2): f.write(f"{_(n, 3 - 2 * i, 9 + 4 * i, 5 - 4 * i, 9 + 4 * i)} \n")
for i in range(3): f.write(f"{_(n, 0, 15, 0, 14)} \n")
for i in range(-1, 6): f.write(f"{_(n, 3 + 2 * i, 23 - 4 * i, 0, 0)} \n")
f.write("\n" + (9 + n) * " " + "i love you ❤")
os.popen("love.out", "w").write("\n")
