from norminette.context import GlobalScope
from norminette.rules import Rule, Check


class CheckLineCount(Rule, Check):
    def run(self, context):
        """
        Each function can only have 42 lines between its opening and closing brackets
        not including the lines with the brackets
        """
        for t in context.tokens[: context.tkn_scope]:
            if t.type == "NEWLINE" or t.type == "ESCAPED_NEWLINE":
                context.scope.lines += 1

        if type(context.scope) is GlobalScope:

            # if context.get_parent_rule() == "CheckFuncDeclarations" and context.scope.lines > 42:
            #     context.new_error("TOO_MANY_LINES", context.tokens[context.tkn_scope])
            # elif context.get_parent_rule() == "CheckFuncDeclarations" and context.scope.lines % 2 == 1:
            #     context.new_error("ODD_NBR_LINES", context.tokens[context.tkn_scope])
            return False, 0

        if context.get_parent_rule() == "CheckBrace":
            if "LBRACE" in [t.type for t in context.tokens[: context.tkn_scope + 1]]:
                if type(context.scope) is GlobalScope:
                    return False, 0
            else:
                if context.scope.lvl == 0:
                    return False, 0

        return False, 0
