import config

def custom_id(view: str, id: int) -> str:
    return f"{config.BOT_NAME}:{view}:{id}"

def custom_id2(view: str, id: int) -> str:
    return f"{config.BOT_NAME}:{view}:{id}"