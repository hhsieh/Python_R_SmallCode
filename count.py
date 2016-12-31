## count the replicates of "Sam" in the list

sentences = ["Same Sam", "Sam Sam", "Sam]

sam_count = 0
for sentence in sentences:
    sam_count += sentence.count("Sam")

print sam_count  #5

## this generates the exact appearance of string "Sam" in the list
print sentences.count("Sam") # 1


    
    
