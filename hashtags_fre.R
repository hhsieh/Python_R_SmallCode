## frequency analysis of twitter hashtags in social movements

setwd("") ## working directory is where 20110917.csv is located
data <- read.csv("20110917.csv", header = T, stringsAsFactors = F)
head(data)
#tail(data)
dim(data)
colnames(data)
hashtags <- data$hashtags

library(stringr)
A = strsplit(hashtags, "#")
B = unlist(A)
B = B[ B!="" ]
C <- str_replace_all(B, " ", "")
movement  <- rep("occupy wall street", length(C))
ows <- data.frame(movement , hashtag = C)
head(ows)


## Below shows similiar operations
dk <- read.csv("mniwiconi.csv", header = T, stringsAsFactors = F)
head(dk)
hashtags_dk <- dk$Hashtags[1:40]
hashtags_dk <- hashtags_dk[-c(35)]
hashtags_dk <- strsplit(hashtags_dk, " ")
hashtags_dk
hashtags_dk <- unlist(hashtags_dk)
hashtags_dk
movement <- rep("north dakota pipeline", length(hashtags_dk))
ndp <- data.frame(movement, hashtag = hashtags_dk)
head(ndp)

blm <- read.csv("blacklivematters.csv", header = T, stringsAsFactors = F)
head(blm)
hashtags_blm <- blm$Hashtags
hashtags_blm <- strsplit(hashtags_blm, " ")
hashtags_blm <- unlist(hashtags_blm)
hashtags_blm
movement <- rep("black lives matter", hashtags = hashtags_blm)
black <- data.frame(movement, hashtag = hashtags_blm)
black

water <- read.csv("waterislife.csv", header = T, stringsAsFactors = F)
head(water)
hashtags_water <- water$Hashtags
hashtags_water <- hashtags_water[-c(25, 54, 62, 63, 75)]
hashtags_water <- hashtags_water[-c(538, 541, 548, 549)]
hashtags_water <- hashtags_water[1:680]
hashtags_water <- strsplit(hashtags_water, " ")
hashtags_water <- unlist(hashtags_water)
hashtags_water
movement <- rep("water is life", length(hashtags_water))
wil <- data.frame(movement, hashtag = hashtags_water)
head(wil)

DATA <- rbind(ows, ndp, black, wil)
head(DATA)

#network visualization


#hashtags_frequencies <- sort(table(C), decreasing = TRUE)[1:20]
#hashtags_frequencies
