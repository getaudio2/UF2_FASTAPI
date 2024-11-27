def theme_schema(theme) -> dict:
    return {
        "option": theme[0]
    }

def themes_schema(themes) -> list[dict]:
    return [theme_schema(theme) for theme in themes]