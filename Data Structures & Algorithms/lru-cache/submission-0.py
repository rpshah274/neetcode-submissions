class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev,self.next=None,None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}
        self.oldest=Node(0,0)
        self.latest=Node(0,0)
        self.oldest.prev=self.latest
        self.latest.next=self.oldest
    #Helper
    def insert(self,node):
        prev,nxt=self.latest,self.latest.next
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def remove(self,node):
        prev,nxt=node.prev,node.next
        prev.next,nxt.prev=nxt,prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap:
            lru=self.oldest.prev
            self.remove(lru)
            del self.cache[lru.key]
