#!/usr/bin/python3
"""
    BaseCache module
"""
from base_caching import BaseCaching
class LIFOCache(BaseCaching):
    """ LIFOCache defines a LIFO (Last In, First Out) algorithm for the cache.   
    To use:
    >>> my_cache = LIFOCache()
    >>> my_cache.print_cache()
    Current cache:   
    >>> my_cache.put("A", "Hello")
    >>> my_cache.print_cache()
    A: Hello   
    >>> print(my_cache.get("A"))
    Hello
    Example:
    >>> print(self.cache_data)
    {A: "Hello", B: "World", C: "Holberton", D: "School"}   
    >>> my_cache.put("C", "Street")
    >>> print(self.cache_data)
    {A: "Hello", B: "World", C: "Street", D: "School"}
    >>> my_cache.put("F", "COD")
    DISCARD: D
    >>> print(self.cache_data)
    {A: "Hello", B: "World", C: "Holberton", F: "COD"}
    """
    def __init__(self):
        """ Initialize the LIFO cache """
        super().__init__()
    def put(self, key, item):
        """
            Add an item to the cache.
            Args:
                key: the key of the cache
                item: the value associated with the key
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    keydel = list(self.cache_data.keys())[-1] 
                    del self.cache_data[keydel]  
                    print(f"DISCARD: {keydel}")
            self.cache_data[key] = item  
    def get(self, key):
        """
            Retrieve an item from the cache by key.
            Args:
                key: the key of the cache
            Return:
                value associated with the key, or None if the key doesn't exist
        """
        return self.cache_data.get(key)
