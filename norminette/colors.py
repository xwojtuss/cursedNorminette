from typing import Optional

red = {
    "TOO_MANY_ARGS",
    "TOO_MANY_VARS_FUNC",
}
yellow = {
    "MIXED_SPACE_TAB",
    "BRACE_NEWLINE"
}
green = {
    "TOO_MANY_FUNCS",
}
blue = {
    "SPC_INSTEAD_TAB",
    "CONSECUTIVE_SPC",
    "CONSECUTIVE_WS",
    "TAB_BFR_OPERATOR",
    "TAB_AFTER_OPERATOR",
    "NO_TAB_BFR_OPR",
    "NO_TAB_AFR_OPR",
    "TAB_AFTER_PAR",
    "TAB_BFR_PAR",
    "NO_TAB_AFR_PAR",
    "NO_TAB_BFR_PAR",
    "SPC_AFTER_POINTER",
    "SPC_LINE_START",
    "SPC_BFR_POINTER",
    "SPACE_BEFORE_FUNC",
    "TOO_MANY_TABS_FUNC",
    "TOO_MANY_TABS_TD",
    "MISSING_TAB_FUNC",
    "MISSING_TAB_VAR",
    "TOO_MANY_TAB_VAR",
    "INVALID_LINE_LENGTH",
    "EXP_PARENTHESIS",
}
pink = {
    "COMMENT_ON_INSTR",
}
grey = {
}

_color_table = {
    "91": red,
    "92": green,
    "93": yellow,
    "94": blue,
    "95": pink,
    "97": grey,
}


def error_color(name: str) -> Optional[str]:
    for color, table in _color_table.items():
        if name in table:
            return color
    return None
