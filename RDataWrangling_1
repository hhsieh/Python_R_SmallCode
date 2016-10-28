#read in data
bikes <- read.csv("train_DCbikes.csv")

## separate the strings
datetime <- bikes$datetime
process_datetime <- as.character(datetime)
process_datetime <- strsplit(process_datetime, " ")

## transform the list into a data frame and set appropriate column names
library("plyr")
df <- ldply(process_datetime)
colnames(df) <- c("Date", "Time")

## separate month,date and year from Date
Date <- strsplit(df$Date,"/")
Month<- rep(0,length(Date))
for (i in 1:length(Date)) {
  Month[i] <- Date[[i]][1]
}

Day <- rep(0,length(Date))
for (i in 1:length(Date)) {
  Day[i] <- Date[[i]][2]
}

Year <- rep(0,length(Date))
for (i in 1:length(Date)){
  Year[i] <- Date[[i]][3]
}

##New bikes data
bikes <- data.frame(Month, Day, Year,df,bikes)
str(bikes)

## preliminary data exploration
## First rename seasons

x <- factor(bikes$season)
levels(x)
library(plyr)
season2 <- revalue(x, c("1"="spring", "2"="summer","3"="fall","4"="winter"))

## or do this
##mapvalues(x, from = c("1", "2","3","4"), to = c("spring", "summer", "fall", "winter"))

bikes <- data.frame(season2, bikes)
boxplot(humidity~season2, data=bikes)

## Rename Month
y <- factor(bikes$Month)
levels(y)
Month2 <- revalue(y, c("1"="Jan","2" = "Feb", "3"="March","4"="April","5"="May","6"="June","7"="July","8"="Aug","9"="Sep","10"="Oct","11"="Nov","12"="Dec"))
bikes <- data.frame(Month2, bikes)
boxplot(humidity~Month2, data=bikes, order="Month2")
