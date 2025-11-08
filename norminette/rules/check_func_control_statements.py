from norminette.rules import Rule, Check

class CheckFuncControlStatements(Rule, Check):
    depends_on = (
        "IsFuncDeclaration",
        "IsControlStatement",
        "IsExpressionStatement",
    )

    def run(self, context):
        """
        There must be an even number of for and switch keywords
        in the function scope
        """
        # print("TEST", context.sub)
        pos = None
        while_count = 0
        if_count = 0
        if context.scope.name == "GlobalScope":
            if context.sub is None:
                return False, 0
            i = 0
            while context.check_token(i, "IDENTIFIER") is False:
                i += 1
            pos = context.peek_token(i)
            if not pos:
                return False, 0
            while context.check_token(i, "LBRACE") is False:
                i += 1
            if context.peek_token(i) is None:
                return False, 0
            try:
                max_i = context.skip_nest(i)
            except:
                return False, 0
            while i < max_i:
                if context.check_token(i, "FOR") is True:
                    while_count += 1
                elif context.check_token(i, "SWITCH") is True:
                    if_count += 1
                i += 1
            if while_count % 2 == 0:
                context.new_error("EVEN_FORS", pos)
            if if_count % 2 == 0:
                context.new_error("EVEN_SWITCHES", pos)
        # print("ran", context.scope.name, context.tokens)

