from typing import Optional, List
from src.building import Building


class BSTNode:
    def __init__(self, building: Building):
        self.building = building
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None

class BST:
    def __init__(self):
        self.root: Optional[BSTNode] = None

    def insert(self, building: Building):
        def _insert(node: Optional[BSTNode], building: Building) -> BSTNode:
            if node is None:
                return BSTNode(building)
            if building.id < node.building.id:
                node.left = _insert(node.left, building)
            elif building.id > node.building.id:
                node.right = _insert(node.right, building)
            else:
                # duplicate id -> ignore
                pass
            return node
        self.root = _insert(self.root, building)

    def search(self, building_id: int) -> Optional[Building]:
        node = self.root
        while node:
            if building_id == node.building.id:
                return node.building
            elif building_id < node.building.id:
                node = node.left
            else:
                node = node.right
        return None

    def inorder(self) -> List[Building]:
        out: List[Building] = []
        def _in(node: Optional[BSTNode]):
            if not node: return
            _in(node.left)
            out.append(node.building)
            _in(node.right)
        _in(self.root)
        return out

    def preorder(self) -> List[Building]:
        out: List[Building] = []
        def _pre(node: Optional[BSTNode]):
            if not node: return
            out.append(node.building)
            _pre(node.left)
            _pre(node.right)
        _pre(self.root)
        return out

    def postorder(self) -> List[Building]:
        out: List[Building] = []
        def _post(node: Optional[BSTNode]):
            if not node: return
            _post(node.left)
            _post(node.right)
            out.append(node.building)
        _post(self.root)
        return out

    def height(self) -> int:
        def _h(node: Optional[BSTNode]) -> int:
            if not node: return 0
            return 1 + max(_h(node.left), _h(node.right))
        return _h(self.root)
