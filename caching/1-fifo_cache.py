#!/usr/bin/python3
"""
    BaseCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines a FIFO (First In, First Out) algorithm for the cache.
    
    To use:
    >>> my_cache = FIFOCache()
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
    DISCARD: A
    >>> print(self.cache_data)
    {F: "COD", B: "World", C: "Holberton", D: "School"}
    """
    
    def __init__(self):
        """ Initialize the FIFO cache """
        super().__init__()

    def put(self, key, item):
        """
            Add an item to the cache.

            Args:
                key: the key of the cache
                item: the value associated with the key
        """
        if key is not None and item is not None:
            # If the key doesn't exist in cache, we check if we need to discard the first element
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # FIFO - Discard the first added item (first in)
                    keydel = list(self.cache_data.keys())[0]  # Get the first key in the cache
                    del self.cache_data[keydel]  # Delete the first element
                    print(f"DISCARD: {keydel}")
            self.cache_data[key] = item  # Add the new item to the cache

    def get(self, key):
        """
            Retrieve an item from the cache by key.

            Args:
                key: the key of the cache

            Return:
                value associated with the key, or None if the key doesn't exist
        """
        return self.cache_data.get(key)
