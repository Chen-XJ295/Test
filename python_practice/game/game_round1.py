def fight():
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200

    my_final_hp = my_hp - enemy_power
    enemy_final_hp = enemy_hp - my_power

    print("我赢了") if my_final_hp > enemy_final_hp else print("我输了")

fight()

