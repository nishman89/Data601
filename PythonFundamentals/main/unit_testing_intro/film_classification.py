"""Film classification system based on viewer age."""

"""Film classification system based on viewer age."""


def get_classifications_by_age(age_of_viewer: int) -> str:
    """
    Return available film classifications based on viewer's age.

    Args:
        age_of_viewer: Age of the person viewing films

    Returns:
        str: Available film classifications
    """
    if age_of_viewer < 12:
        return "U, PG & 12 films are available."
    elif age_of_viewer < 15:
        return "U, PG, 12 & 15 films are available."
    else:
        return "All films are available."