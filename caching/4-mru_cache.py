#!/usr/bin/python3
"""
    MRUCache module
"""
from base_caching import BaseCaching
from collections import OrderedDict

class MRUCache(BaseCaching):
    """ MRUCache defines a Most Recently Used algorithm for cache.
    
    To use:
    >>> my_cache = MRUCache()
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

    >>> my_cache.put("E", "Battery")
    DISCARD: C
    >>> print(self.cache_data)
    {A: "Hello", B: "World", D: "School", E: "Battery"}
    """

    def __init__(self):
        """ Initialize the MRU cache """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
            Add an item to the cache.

            Args:
                key: the key of the cache
                item: the value associated with the key
        """
        if key is None or item is None:
            return
        
        # If the cache is full, discard the most recently used item
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the most recently used (last) item
                discarded_key, discarded_value = self.cache_data.popitem(last=True)
                print(f"DISCARD: {discarded_key}")
        
        # Insert or update the key-value pair, making it the most recently used
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)  # Move the key to the end (most recently used)

    def get(self, key):
        """
            Get an item from the cache by key.

            Args:
                key: the key of the cache

            Return:
                value associated with the key, or None if the key doesn't exist
        """
        if key is None or key not in self.cache_data:
            return None
        
        # Move the accessed key to the end to mark it as most recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
