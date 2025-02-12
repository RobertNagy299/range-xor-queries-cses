# range-xor-queries-cses

You can read the constraints and the description [here](https://cses.fi/problemset/task/1650/)


## Intuition:
When the problem consists of an array, and then `n` intervals which perform queries on the array, we can use a "Prefix sum" `auxiliary array` to first calculate every operation from 1 to n in `O(n)`, and then answer each `query` in `O(1)`

## Time complexity:
- `O(n)` - First we traverse the nums array once, if it contains `n` elements, it takes `O(n)` time
- `O(k)` - Process each query. We have `k` queries. Each query is processed in  constant time `O(1)`, because we just perform two read operations and one xor operation for each query.
- `O(k)` - Traverse the answer array, and print each value. This could be avoided in C++ with `cout.tie(0)`

  Overall complexity: `2 * O(k) + O(n) ` which is approximately `O(3 * n)` which is `linear time`, albeit, this could easily be improved to `O(2*n)`

## Space complexity:
- Auxiliary array to store the prefix xor values: `O(n)`, because we have `n` numbers
- Auxiliary array to store the answer for each query: `O(k)` - this could be avoided, as discussed above.

Overall space complexity: `O(2 * n)` which is `linear`, but could be improved.
