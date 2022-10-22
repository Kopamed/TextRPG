from entity import *


def select_from_list(prompt: str, arr: List[Entity]) -> Entity:
    while True:
        print(prompt)
        # TODO: Display team[i] stats such as attack and health
        print(
            "\n".join(
                f"[{i}] {arr[i].type}: {arr[i].name}" for i in range(len(arr))
            )
        )
        try:
            n = int(input())
        except ValueError:
            continue

        if n < len(arr):
            return arr[n]


if __name__ == "__main__":
    player_turn = True

    player_team = [
        Barbarian(),
        Barbarian()
    ]

    ai_team = [
        Elf(),
        Barbarian(),
        Elf()
    ]

    entity = select_from_list("Select which entity you want to use:", player_team)
    action = Action.ATTACK if input(
        "Do you want to [a]ttack or use [s]pecial powerup? [a/s]: ").lower() == "a" else Action.SPECIAL_POWERUP
    target = select_from_list("Select which enemy do you want to attack:", ai_team)

    # entity.action(target)
