import random


def fight(enemy_hp, enemy_power):
    my_hp = 1000
    my_power = 200
    print(f'敌人的血量{enemy_hp}，攻击力为{enemy_power}')

    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        if my_hp <= 0:
            print(f'我剩余血量为{my_hp}')
            print(f'敌人剩余血量为{enemy_hp}')
            print("我输了")
            break
        elif enemy_hp <= 0:
            print(f'我剩余血量为{my_hp}')
            print(f'敌人剩余血量为{enemy_hp}')
            print("我赢了")
            break


if __name__ == "__main__":
    hp = [x for x in range(990, 1010)]
    enemy_hp = random.choice(hp)
    # print(enemy_hp)
    enemy_power = random.randint(190, 210)
    # print(enemy_power)

    fight(enemy_hp, enemy_power)
