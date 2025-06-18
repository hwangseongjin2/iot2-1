class terran:
    hp = 30
    power = 10
    atk = ""

    def attack(self):
        print(self.atk)


u1 = terran()
u2 = terran()

u1.atk="---->"
u2.atk="<----"

while u1.hp != 0 and u2.hp != 0:
    at= input ("attack(1 or 2):")
    if at == "1":
        u1.attack()
        u2.hp = u2.hp-u1.power
    elif at == "2":
        u2.attack()
        u1.hp = u1.hp-u2.power

    print("u1.hp=", u1.hp, ", u2.hp=", u2.hp)

if u1.hp == 0:
    print("u2 win!")
elif u2.hp == 0:
    print("u1 win!")