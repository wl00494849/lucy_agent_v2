from typing import List

class KV:
    def __init__(self,k:str,v:float):
        self.k = k
        self.v = v

class MaxHeap:
    def __init__(self):
        self.heap:List[KV] = []

    def push(self,val:KV):
        self.heap.append(val)
        self._heap_up(len(self.heap)-1)

    def pop(self)->KV:
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap[0]
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heap_down(0)
        return max_val

    def _heap_up(self,index:int):
        parent = (index - 1)//2
        if index > 0 and self.heap[index].v > self.heap[parent].v:
            self._swap(index,parent)
            self._heap_up(parent)
            
    def _heap_down(self,index:int):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left].v > self.heap[largest].v:
            largest = left
        if right < len(self.heap) and self.heap[right].v > self.heap[largest].v:
            largest = right
        if largest != index:
            self._swap(largest,index)
            self._heap_down(largest)

    def _swap(self,a:int,b:int):
        self.heap[a],self.heap[b] = self.heap[b],self.heap[a]