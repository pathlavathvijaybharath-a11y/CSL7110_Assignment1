# CSL7110 - Assignment 1  
**MapReduce (Hadoop) + Apache Spark (PySpark) – Word Count**

**Name:** Pathlavath Vijay Bharath  
**Roll No:** M25CSA020  
**Date:** February 2026  

GitHub Repository: https://github.com/pathlavathvijaybharath-a11y/CSL7110_Assignment1

## Part 1 – Hadoop MapReduce

### What was implemented
- Classic WordCount example  
- Map & Reduce phase analysis (using song lyrics example)  
- Custom `WordCount.java`  
  - Removes punctuation  
  - Case-insensitive counting  
  - Uses `StringTokenizer`  
- Ran on Project Gutenberg file **200.txt** (~8 MB) → ~78,262 unique words  
- Explained why **HDFS directories show `-`** (no replication factor – only files/blocks are replicated)  
- Split size performance experiment on 8 MB file (single node)

### Split Size Results (most important finding)
| Split Size     | Number of Maps | Execution Time | Comment                        |
|----------------|----------------|----------------|--------------------------------|
| 1 MB           | 8              | 4.823 s        | Good parallelism               |
| 2 MB           | 4              | 5.905 s        | Worst                          |
| 4 MB           | 2              | 5.961 s        | Worst                          |
| Default (~8 MB)| 1              | **4.899 s**    | **Fastest** – least overhead   |

**Conclusion (single node + small file):** Default/big splits win because task scheduling & startup overhead dominates.

## Part 2 – PySpark Word Count

### Files in PySpark folder
- `wordcount.py`     → Main PySpark program  
- `input.txt`        → Sample input text file used for testing  
- `output.png`       → Screenshot of terminal output  

### What the program does
- Reads text from `input.txt`  
- Splits lines into words  
- Maps: each word → `(word, 1)`  
- Reduces: group by word and sum counts  
- Prints final word counts to console  

### How to Run
```bash
# Navigate to the folder
cd path/to/CSL7110_Assignment1/PySpark-Part    # or wherever your files are

# Option 1: Run directly (if pyspark is in environment)
python3 wordcount.py

# Option 2: Recommended – use spark-submit
spark-submit wordcount.py
