


personae_by_name = None
normal_spread = data["normal_spread"]
triple_spread = data["triple_spread"]

fusion_table




# Instead of storing the fusion table, could store by entry instead.

def get_recipes(persona_name):
    persona_data = personae_by_name[persona_name]
    arcana = persona["arcana"]
    recipes = []
    # Gets the persona's special fusion if one exists:
    if persona_data.get("special"):
        recipes.append(special_fusions[persona_name])
        # With the exception of Orpheus Telos, personas with special fusions
        # cannot be fused any other way.
        if persona_name.get("exclusive"):
            return recipes

    


def get_normal_spread_recipes(persona_name, arcana):
    """
    Takes a persona and its arcana and returns a list of all the possible
    normal spread fusion recipes that could make up that persona.
    """

    recipes = []
    for arcana_1, arcana_2 in normal_spread[arcana]:
        personae_1 = personae_by_arcana[arcana_1]
        personae_2 = personae_by_arcana[arcana_2]
        for p1 in personae_1:
            for p2 in personae_2:
                # The same Persona cannot be used multiple times in a fusion.
                if p1 is p2:
                    continue
                resultant_persona = normal_spread(p1, p2)
                if resultant_persona is None:
                    continue
                # Calculate costs?
                if resultant_persona["name"] == persona_name:
                    recipes.append(resultant_persona)
    return recipes


def get_triple_spread_recipes(arcana):
    pass





def normal_spread(persona_1, persona_2):
    """
    Fuses the two supplied personas (specified by name). Returns None if
    no fusion is possible.
    """


def triple_spread(persona_1, persona_2, persona_3):
    """
    Fuses the three supplied personas (specified by name). Treats the
    third persona as the persona with the highest current level.
    Returns None if no fusion is possible.
    """