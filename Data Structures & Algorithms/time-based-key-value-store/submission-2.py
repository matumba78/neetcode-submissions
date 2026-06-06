class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [[value, timestamp]]
        else:
            self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        store_value = self.store.get(key, [])
        if not store_value:
            return ""
        l, r = 0, len(store_value) - 1
        while l <= r:
            mid = (l + r) // 2
            if store_value[mid][1] < timestamp:
                l = mid + 1
            elif store_value[mid][1] > timestamp:
                r = mid - 1
            else:
                return store_value[mid][0]
    
        return store_value[l-1][0] if store_value[l-1][1] <= timestamp else ""