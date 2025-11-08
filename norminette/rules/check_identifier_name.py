import string

from norminette.rules import Rule, Check
from norminette.scope import GlobalScope, UserDefinedType


assigns = ["ASSIGN"]

def is_valid(to_check):
    if (not to_check.startswith("ft_")
        or len(to_check) != 4
        or to_check[3] not in string.ascii_lowercase):
        return False
    return True

class CheckIdentifierName(Rule, Check):
    def run(self, context):
        """
        Function can only be declared in the global scope
        User defined identifiers have to start with 'ft_'
        and after the prefix have only one lowercase letter
        """
        legal_characters = string.ascii_lowercase + string.digits + "_"
        if context.history[-1] == "IsFuncDeclaration":
            sc = context.scope
            if type(sc) is not GlobalScope and type(sc) is not UserDefinedType:
                context.new_error("WRONG_SCOPE_FCT", context.peek_token(0))
            while type(sc) is not GlobalScope:
                sc = sc.outer()
            if not is_valid(sc.fnames[-1]):
                context.new_error(
                    "FORBIDDEN_CHAR_NAME", context.peek_token(context.fname_pos)
                )
        if len(context.scope.vars_name) > 0:
            for val in context.scope.vars_name[::]:
                if not is_valid(val.value):
                    context.new_error(
                        "FORBIDDEN_CHAR_NAME", context.peek_token(context.fname_pos)
                    )
                context.scope.vars_name.remove(val)
        return False, 0
