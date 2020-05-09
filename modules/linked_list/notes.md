## Notes

### Differences between Linked Lists and Lists

| Operation          | Linked List | List | notes            |
| :--------          | :--------:- | :--: | :---             |
| access             | O(n)        | O(1) |                  |
| insert (at head)   | O(1)        | O(n) |                  |
| insert (at tail)   | O(n)        | O(n) | `append` is O(1) |
| deletion (at head) | O(1)        | O(n) |                  |
| deletion (at tail) | O(n)        | O(n) | `pop` is O(1)    |

xxx: memory layout - contiguous vs sparse
xxx: insertion and deletion: list (shift list to accommodate) vs linked list (use node pointer to determine location)
