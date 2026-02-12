# CSL7110_Assignment1

Assignment 1 for CSL7110. This repository contains two parts:
1) An earlier submission using Apache Spark (PySpark)
2) The final submission using Apache Hadoop MapReduce (Q1–Q9)

Student Details  
Name: Pathlavath Vijay Bharath  
Roll No: M25CSA020  
Course: CSL7110  

Part 1 – Spark (Earlier Submission)  
Files:  
- wordcount.py  
- input.txt  
- output.png  

Run (Spark):  
python3 wordcount.py  

Part 2 – Hadoop (Final Submission – Q1 to Q9)  
Contents:  
- Question1-7/  
  - WordCount.java  
  - screenshots/  
- Question9/  
  - WordCountTimed.java  
  - run_experiments.sh  
  - results/  
- Report.pdf  

Run (Hadoop):  
hdfs dfs -mkdir -p /user/vbn/input  
hdfs dfs -put input.txt /user/vbn/input  
hadoop jar WordCount.jar WordCount /user/vbn/input /user/vbn/output  
hdfs dfs -cat /user/vbn/output/part-r-00000  

Note  
The final evaluated submission is the Hadoop MapReduce implementation (Q1–Q9) with Report.pdf and screenshots.  
The Spark (PySpark) files are included only as the earlier submission.
