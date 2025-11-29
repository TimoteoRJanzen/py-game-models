import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file:
        players = json.load(file)

    for player, data in players.items():

        race = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"])

        skills = []
        for skill in data["race"]["skills"]:
            set_skill = Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race[0])
            skills.append(set_skill)

        guild = (None, None)
        if data["guild"]:
            guild = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                description=data["guild"]["description"])

        Player.objects.get_or_create(
            nickname=player,
            email=data["email"],
            bio=data["bio"],
            guild=guild[0],
            race=race[0])


if __name__ == "__main__":
    main()
