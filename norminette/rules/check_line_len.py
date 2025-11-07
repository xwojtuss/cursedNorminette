from norminette.rules import Rule, Check


class CheckLineLen(Rule, Check):
    def run(self, context):
        """
        Lines must be exactly 42 characters long
        """
        i = 0
        invalid_line = {}
        for tkn in context.tokens[: context.tkn_scope]:
            if tkn.type == "NEWLINE" and tkn.pos[1] != 43 and tkn.pos[0] not in invalid_line:
                context.new_error("INVALID_LINE_LENGTH", tkn)
                invalid_line[tkn.pos[0]] = True
            i += 1
        return False, 0
