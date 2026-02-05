from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("WordCount").getOrCreate()
    sc = spark.sparkContext

    # Read input file
    text_file = sc.textFile("input.txt")

    # Word count
    counts = (
        text_file
        .flatMap(lambda line: line.split())
        .map(lambda word: (word.lower(), 1))
        .reduceByKey(lambda a, b: a + b)
    )

    # Print result
    for word, count in counts.collect():
        print(word, count)

    spark.stop()
