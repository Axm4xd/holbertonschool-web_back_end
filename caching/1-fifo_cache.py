#!/usr/bin/python3
"""
    BaseCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache define a FIFO algorithm to use cache

      To use:
      >>> my_cache = FIFOCache()
      >>> my_cache.print_cache()
      Current cache:

      >>> my_cache.put("A", "Hello")
      >>> my_cache.print_cache()
      A: Hello

      >>> print(my_cache.get("A"))
      Hello

      Ex:
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
        """ Initialize """
        super().__init__()

    def put(self, key, item):
        """
            Modify cache data

            Args:
                key: key of the cache
                item: value of the key
        """
        if key is not None and item is not None:
            # If the key doesn't exist in cache, we check if we need to discard the first element
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # FIFO - Discard the first added item
                    keydel = list(self.cache_data.keys())[0]  # Get the first key in the cache
                    del self.cache_data[keydel]  # Delete it
                    print("DISCARD: {}".format(keydel))

            self.cache_data[key] = item  # Add the new item to the cache

    def get(self, key):
        """
            Get cache data by key

            Args:
                key: key of the cache

            Return:
                value of the key
        """
        return self.cache_data.get(key)
