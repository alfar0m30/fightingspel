import random
import time

def get_player_name():
    while True:
        name = input("Skriv in ditt namn (minst 3, max 15 tecken): ")
        if 3 <= len(name) <= 15:
            return name
        else:
            print("Ditt namn måste vara mellan 3 och 15 tecken. Skriv igen.")

def choose_opponent_name():
    names = ["Random 1", "Random 2", "Random 3"]
    return random.choice(names)

def fight(player_name, opponent_name):
    print(f"\n{player_name} vs {opponent_name}!")
    player_hp = 100
    opponent_hp = 100

    while player_hp > 0 and opponent_hp > 0:

        attack = input("Välj attack (1: Stark, 2: Svag): ")
        if attack == '1':
            hit_chance = 0.3
            damage = random.randint(15, 30)
        else:
            hit_chance = 0.7
            damage = random.randint(5, 15)
        time.sleep(0.3)
        if random.random() < hit_chance:
            opponent_hp -= damage
            print(" ")
            print(f"{player_name} träffade {opponent_name} och gjorde {damage} skada.")
        else:
            print(" ")
            print(f"{player_name} missade.")
        time.sleep(0.7)

        opponent_attack = random.choice(['1', '2'])
        if opponent_attack == '1':
            hit_chance = 0.3
            damage = random.randint(15, 30)
        else:
            hit_chance = 0.7
            damage = random.randint(5, 15)

        if random.random() < hit_chance:
            player_hp -= damage
            print(f"{opponent_name} träffade {player_name} och gjorde {damage} skada.")
        else:
            print(f"{opponent_name} missade.")
        time.sleep(0.7)
        print(f"\n{player_name} HP: {player_hp}")
        print(f"{opponent_name} HP: {opponent_hp}")
        print(" ")

    if player_hp <= 0 and opponent_hp <= 0:
        print("Det blev oavgjort!")
    elif player_hp <= 0:
        print(f"{opponent_name} vann!")
    else:
        print(f"{player_name} vann!")

def main():
    print("Välkommen till Slagsmålsspelet!")
    player_name = get_player_name()
    opponent_name = choose_opponent_name()

    while True:
        fight(player_name, opponent_name)
        restart = input("Vill du spela igen? (ja/nej): ")
        if restart.lower() != 'ja':
            print("Tack för att du spelade!")
            break

if __name__ == "__main__":
    main()