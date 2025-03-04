# TTL Cache

A function-level memory cache that supports Time To Live (TTL).

- **Per-function argument caching**: Caching is possible based on the data passed to function arguments. The cache key is composed of the function name, argument names, and the values of the arguments.
- **Automatic expiration**: Cached data expires and is automatically deleted after the specified TTL (in seconds).
- **LRU policy**: When the cache exceeds its maximum size (`max_size`), the Least Recently Used (LRU) policy is applied to delete items.
- **Easy application**: Simply add the `@TtlCache(ttl=seconds)` decorator to the function you want to cache.

## Parameters:

- **ttl**: TTL for the cached data (in seconds).
- **max_size**: Maximum number of cache entries.
- **applying_params**: List of parameter names to use as the cache key. If `None`, all parameters are used. If `[]`, only the function name is used.

## Member Functions:

- **force_expire(key)**: Forces expiration of the cache entry for the specified key.
- **is_exist(key)**: Checks if a specific key exists in the cache.
- **get_item(key)**: Returns the cache item for the specified key.
  - *Note*: The key can include partial elements of the cache key.

## Usage:
1. Install the package using `pip install parametric-ttl-cache`.
2. Import the `TtlCache` class `from parametric_ttl_cache.ttl_cache import TtlCache`.
2. Add the `@TtlCache(ttl=seconds)` decorator to the function you want to cache.
3. Cache keys are generated in the format `"{class_name.}method_name(param1=value1, param2=value2, ...)"`.
4. To call the member functions of `TtlCache`, create an instance of `TtlCache` and use that instance as the decorator.

## Source code installation:
```bash
git clone https://github.com/jogakdal/python_ttl_cache.git
cd python_ttl_cache
pip install -r requirements.txt
```

### Example:
```python
from parametric_ttl_cache.ttl_cache import TtlCache


some_cache = TtlCache(ttl=5)

@some_cache
def some_function(x):
    return x * 2

@TtlCache(ttl=5, max_size=10, applying_params=['key'])
def another_function(key, value):
    return f'{key} = {value}'

# Usage
result = some_function(1)
some_cache.force_expire('some_function(x=1)')
```

### Test:
```python
import unittest
import time

from parametric_ttl_cache.ttl_cache import TtlCache


class TestTtlCache(unittest.TestCase):
    __increment = 0
    def test_ttl_cache(self):
        ttl = 2  # 2 seconds
        cache = TtlCache(ttl)

        def incrementer():
            self.__increment += 1
            return self.__increment

        @cache
        def func(x=1):
            return x + incrementer()

        self.assertEqual(func(1), 2, '첫 번 째 호출은 정상적으로 실행')
        self.assertEqual(func(1), 2, '두 번 째 호출은 캐시에서 가져와야 하고 incrementer가 호출되지 않아야 함')
        self.assertEqual(func(x=1), 2, '명시적인 키워드 인자도 동일한 캐시 키로 사용되어야 함')
        self.assertEqual(func(), 2, '디폴트 인자와 캐시 키로 사용된 인자가 같으면 같은 캐시 키로 취급되어야 함')
        self.assertEqual(func(2), 4, '인자가 다르면 다른 캐시가 생성되어야 함')

        # 캐시 expire
        time.sleep(ttl + 1)

        self.assertEqual(func(1), 4, '캐시가 expire 되었으므로 incrementer가 호출되어야 함')
        self.assertEqual(func(1), 4, '이 전 호출에서 캐시가 다시 생성되어야 함')

        # 캐시 강제 expire
        cache.force_expire('x=1')

        self.assertEqual(func(1), 5, '강제로 캐시를 expire시키면 incrementer가 호출되어야 함')


if __name__ == '__main__':
    unittest.main()
```
