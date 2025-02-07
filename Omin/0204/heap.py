#Heap
class HeapNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None  # 부모 노드 참조
        
        
class BinaryHeap:
    def __init__(self):
        self.root = None  # 루트 노드
        self.nodes = []   # 노드 리스트 (완전 이진 트리를 유지하기 위함)

    def insert(self, value):
        new_node = HeapNode(value)
        if not self.root:
            self.root = new_node
            self.nodes.append(new_node)
            return

        # 완전 이진 트리를 유지하기 위해 리스트에서 부모 찾기
        parent = self.nodes[(len(self.nodes) - 1) // 2]
        new_node.parent = parent

        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node

        self.nodes.append(new_node)

        # 힙 속성 유지 (Up-Heap / Heapify Up)
        self.heapify_up(new_node)

    def heapify_up(self, node):
        """새로 삽입된 노드를 힙 속성을 유지하도록 위로 이동"""
        while node.parent and node.value < node.parent.value:
            node.value, node.parent.value = node.parent.value, node.value
            node = node.parent

    def extract_min(self):
        """최소 힙에서 루트(최소값)를 제거하고 반환"""
        if not self.root:
            return None

        min_value = self.root.value
        last_node = self.nodes.pop()

        if not self.nodes:
            self.root = None
            return min_value

        # 루트 교체 (마지막 노드를 루트로)
        self.root.value = last_node.value
        if last_node.parent:
            if last_node.parent.left == last_node:
                last_node.parent.left = None
            else:
                last_node.parent.right = None

        # 힙 속성 유지 (Down-Heap / Heapify Down)
        self.heapify_down(self.root)

        return min_value

    def heapify_down(self, node):
        """루트에서 아래로 내려가면서 힙 속성을 유지"""
        while node.left:
            smallest = node.left
            if node.right and node.right.value < node.left.value:
                smallest = node.right

            if node.value > smallest.value:
                node.value, smallest.value = smallest.value, node.value
                node = smallest
            else:
                break

    def print_heap(self):
        """힙을 계층 구조로 출력"""
        for node in self.nodes:
            parent_val = node.parent.value if node.parent else "None"
            print(f"Node: {node.value}, Parent: {parent_val}")

# 실행 예제
heap = BinaryHeap()
heap.insert(10)
heap.insert(5)
heap.insert(15)
heap.insert(2)
heap.insert(7)
heap.insert(12)
heap.insert(20)

heap.print_heap()
print("Extracted Min:", heap.extract_min())
heap.print_heap()