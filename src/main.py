from termcolor import cprint


warn_emoji = "⚠️"
error_emoji = "❌"


def warn(msg: str, identifier_on: bool = True, emojis: bool = True) -> None:
    final_msg = ""

    if emojis:
        final_msg += warn_emoji + " "

    if identifier_on:
        final_msg += "[WARNING]: "

    final_msg += msg
    cprint(final_msg, (255, 165, 0))


def error(err_msg: str, identifier_on: bool = True, emojis: bool = True) -> None:
    final_err_msg = ""

    if emojis:
        final_err_msg += error_emoji + " "

    if identifier_on:
        final_err_msg += "[ERROR]: "

    final_err_msg += err_msg
    cprint(final_err_msg, "red")
