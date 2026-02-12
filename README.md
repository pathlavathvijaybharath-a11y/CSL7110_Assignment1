# CSL7110 - Assignment 1  
**Apache Hadoop MapReduce**

**Name:** Pathlavath Vijay Bharath  
**Roll No:** M25CSA020  
**Date:** Feb 2026

GitHub: https://github.com/pathlavathvijaybharath-a11y/CSL7110_Assignment1

## What was done

1. Ran classic **WordCount** example (small file)  
2. Analyzed **Map phase** → (offset, line) → (word, 1)  
3. Analyzed **Reduce phase** → (word, [1,1,1,...]) → (word, count)  
4–6. Wrote custom **WordCount.java**  
   - Removes punctuation  
   - Case insensitive  
   - Uses StringTokenizer  
   - Proper Writable types (LongWritable, Text, IntWritable)  

7. Ran WordCount on **Project Gutenberg 200.txt** (~8 MB)  
   → ~78,262 unique words

8. Explained why **directories in HDFS show -** (no replication)  
   → Only files/block have replication factor (data)  
   → Directories = pure metadata in NameNode

9. Split size performance test (8 MB file, single node)  

| Split Size | Maps | Time     | Comment               |
|------------|------|----------|-----------------------|
| 1 MB       | 8    | 4.82 s   | good parallelism      |
| 2 MB       | 4    | 5.91 s   | worst                 |
| 4 MB       | 2    | 5.96 s   | worst                 |
| 8 MB (default) | 1 | **4.90 s** | **fastest** (least overhead) |

**Key learning (single node, small file):**  
→ Default/big splits usually win because task startup overhead is significant.

