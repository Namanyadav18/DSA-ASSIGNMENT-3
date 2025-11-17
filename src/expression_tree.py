from typing import Optional, Any, List

class ExprNode:
    def __init__(self, value: Any, left: Optional['ExprNode']=None, right: Optional['ExprNode']=None):
        self.value = value
        self.left = left
        self.right = right

class ExpressionTree:
    """
    Build from postfix tokens (list of strings). Supports + - * / and numeric tokens.
    Example postfix: ['3','4','+','2','*'] -> (3+4)*2
    """
    def __init__(self):
        self.root: Optional[ExprNode] = None

    def build_from_postfix(self, tokens: List[str]):
        stack: List[ExprNode] = []
        for tok in tokens:
            if tok in '+-*/':
                r = stack.pop()
                l = stack.pop()
                stack.append(ExprNode(tok, l, r))
            else:
                try:
                    val = int(tok)
                except ValueError:
                    val = float(tok)
                stack.append(ExprNode(val))
        self.root = stack.pop() if stack else None

    def evaluate(self) -> float:
        def _eval(node: Optional[ExprNode]) -> float:
            if node is None:
                return 0.0
            if node.left is None and node.right is None:
                return float(node.value)
            a = _eval(node.left)
            b = _eval(node.right)
            if node.value == '+': return a + b
            if node.value == '-': return a - b
            if node.value == '*': return a * b
            if node.value == '/': return a / b
            raise ValueError("Unknown operator")
        return _eval(self.root)
