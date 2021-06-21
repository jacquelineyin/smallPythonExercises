from prettytable import PrettyTable


POKEMON_LIST = [
    {
        "name": "Pikachu",
        "type": "Electric",
    },
    {
        "name": "Squirtle",
        "type": "Water",
    },
    {
        "name": "Charmander",
        "type": "Fire",
    },
]


def parse_pokemon_info(pokemon_list):
    """Parses info from pokemon_list and returns an object with the parsed info

    Args:
        pokemon_list ([Array]): [description]

    Returns:
        [object]: {"names": [Array of pokemon names], "types": [Array of pokemon types]}
    """
    parsed_info = {
        "names": [],
        "types": [],
    }

    for pokemon in pokemon_list:
        parsed_info["names"].append(pokemon["name"])
        parsed_info["types"].append(pokemon["type"])

    return parsed_info


table_formatter = PrettyTable()
table_formatter.align = "l"

parsed_info = parse_pokemon_info(POKEMON_LIST)

table_formatter.add_column("Pokemon Name", parsed_info["names"])
table_formatter.add_column("Type", parsed_info["types"])


print(table_formatter)
