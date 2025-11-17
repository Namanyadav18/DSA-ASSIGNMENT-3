from typing import Optional, List
from src.building import Building


class AVLNode:
    def __init__(self, building: Building):
        self.building = building
        self.left: Optional['AVLNode'] = None
        self.right: Optional['AVLNode'] = None
        self.height: int = 1

class AVL:
    def __init__(self):
        self.root: Optional[AVLNode] = None

    def _get_height(self, node: Optional[AVLNode]) -> int:
        return node.height if node else 0

    def _update_height(self, node: AVLNode):
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _balance_factor(self, node: AVLNode) -> int:
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_right(self, y: AVLNode) -> AVLNode:
        x = y.left
        assert x is not None
        T2 = x.right
        x.right = y
        y.left = T2
        self._update_height(y)
        self._update_height(x)
        return x

    def _rotate_left(self, x: AVLNode) -> AVLNode:
        y = x.right
        assert y is not None
        T2 = y.left
        y.left = x
        x.right = T2
        self._update_height(x)
        self._update_height(y)
        return y

    def _rebalance(self, node: AVLNode) -> AVLNode:
        self._update_height(node)
        bf = self._balance_factor(node)
        # Left heavy
        if bf > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)  # LR
            return self._rotate_right(node)
        # Right heavy
        if bf < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)  # RL
            return self._rotate_left(node)
        return node

    def insert(self, building: Building):
        def _insert(node: Optional[AVLNode], building: Building) -> AVLNode:
            if not node:
                return AVLNode(building)
            if building.id < node.building.id:
                node.left = _insert(node.left, building)
            elif building.id > node.building.id:
                node.right = _insert(node.right, building)
            else:
                return node
            return self._rebalance(node)
        self.root = _insert(self.root, building)

    def inorder(self) -> List[Building]:
        out: List[Building] = []
        def _in(node: Optional[AVLNode]):
            if not node: return
            _in(node.left)
            out.append(node.building)
            _in(node.right)
        _in(self.root)
        return out

    def height(self) -> int:
        return self._get_height(self.root)
