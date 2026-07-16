class MyHashMap:

    def __init__(self):
        self.keys: List[int] = []
        self.values: List[int] = []
        

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            index = self.keys.index(key)
            self.values[index] = value
        else:
            self.keys.append(key)
            self.values.append(value)

    def get(self, key: int) -> int:
        if key in self.keys:
            index = self.keys.index(key)
            return self.values[index]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.keys:
            index = self.keys.index(key)
            self.keys.pop(index)
            self.values.pop(index)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)