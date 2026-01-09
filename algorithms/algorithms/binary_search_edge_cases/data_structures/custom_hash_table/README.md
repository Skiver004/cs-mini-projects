## Custom Hash Table – Collision Handling

### Problem
Standard hash tables may have collisions when multiple keys map to the same index.  
Handling collisions efficiently is crucial for performance.

### Approach
- Implemented a hash table using **chaining** (lists in each bucket)  
- Tested multiple keys to deliberately cause collisions

### Observations
- Collisions occur when two keys hash to the same index  
- Chaining allows multiple values in one bucket  
- Performance degrades if many collisions happen (longer chains)

### Lesson Learned
Hash table design requires:
- Good hash functions  
- Proper collision handling  
- Understanding trade-offs between speed, memory, and complexityCustom hash table mini project
