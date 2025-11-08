from norminette.rules import Rule, Check

class CheckDigits(Rule, Check):
    def run(self, context):
        """
        The only number allowed is 42
        """
        i = context.skip_ws(0, nl=False)
        while context.peek_token(i) is not None and context.check_token(i, ["SEMI_COLON", "NEWLINE"]) is False:
            if (context.check_token(i, "CONSTANT") is True
                and context.peek_token(i).value != "42"):
                    context.new_error("NOT_42_DETECTED", context.peek_token(i))
            i += 1
        return False, 0
