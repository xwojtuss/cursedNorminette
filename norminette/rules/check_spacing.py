from norminette.rules import Rule, Check


class CheckSpacing(Rule, Check):
    def run(self, context):
        """
        Indentation (except for preprocessors) must be done with tabs
        There cannot be trailing spaces or tabs at the end of line
        """
        i = 0
        if context.history[-1] in ("IsEmptyLine", "IsPreprocessorStatement"):
            return False, 0
        space_tab_error = False
        space_error = False
        while i in range(len(context.tokens[: context.tkn_scope])):
            if context.check_token(i, "SPACE"):
                context.new_error("SPC_FOUND", context.peek_token(i))
                i += 1
            elif context.check_token(i, "TAB"):
                if context.peek_token(i).pos[1] == 1:
                    while context.check_token(i, "TAB"):
                        i += 1
                    if context.check_token(i, "NEWLINE"):
                        context.new_error("SPC_BEFORE_NL", context.peek_token(i - 1))
                else:
                    i += 1
            else:
                i += 1
        return False, 0
