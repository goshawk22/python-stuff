import csv

tweets = []
with open('scrape/trump.csv', 'r') as trump:
    trumpreader = csv.reader(trump)
    for row in trumpreader:
        tweets.append(row[10])

print(tweets[5])