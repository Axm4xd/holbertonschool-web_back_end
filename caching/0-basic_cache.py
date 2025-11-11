#!/usr/bin/python3
"""
    BaseCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache define a intro to use cache

      To use:
      >>> my_cache = BasicCache()
      >>> my_cache.print_cache()
      Current cache:

      >>> my_cache.put("A", "Hello")
      >>> my_cache.print_cache()
      A: Hello

      >>> print(my_cache.get("A"))
      Hello
    """

    def put(self, key, item):
        """
            Add an item in the cache

            Args:
                key: key of the dict
                item: value of the key
        """
        # Only add to cache if key and item are not None
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
            Get an item by key

            Args:
                key: key of the dict

            Return:
                value of the key
        """
        # Return the value from the cache, or None if the key doesn't exist
        return self.cache_data.get(key)

