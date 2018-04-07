setwd("/Users/grayson/Desktop/datafest")
#rm(list = ls())
#alldata <- read.csv("datafest2018.csv")
slicevector <- runif(nrow(alldata)) > .999
slicedata <- alldata[slicevector,]
clicknums <- c()
cors <- c()
for(start in 0:9)
{
  currentvector <- (slicedata$jobAgeDays > start*10) & (slicedata$jobAgeDays < start*10 + 10)
  currentcut <- slicedata[currentvector,]
  print(start)
  print(cor(currentcut$jobAgeDays,currentcut$localClicks))
  print(nrow(currentcut))
  clicknums <- c(clicknums,mean(currentcut$localClicks))
  cors <- c(cors,cor(currentcut$jobAgeDays,currentcut$localClicks))
}
plot(clicknums)
plot(cors)
abline(h=0)