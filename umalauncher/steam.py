import os
import util
from loguru import logger

def start():
    logger.info("Launching Uma Musume via Steam.")
    os.system("Start steam://rungameid/3564400")

def get_steam_handle():
    steam_handle = util.get_window_handle("steamwebhelper.exe", type=util.EXEC_MATCH)
    if steam_handle:
        return steam_handle
    return None