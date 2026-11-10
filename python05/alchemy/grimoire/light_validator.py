from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    normalized_input = ingredients.lower()
    allowed_lower = map(str.lower, allowed)

    is_valid = any(item in normalized_input for item in allowed_lower)
    return "VALID" if is_valid else "INVALID"
