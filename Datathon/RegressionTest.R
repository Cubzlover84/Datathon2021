# Illini Datathon 2021
# Proctor and Gamble Dataset

getwd()
setwd("C:/Users/Cubzl/Documents/Spring 2021/Datathon")
data <- read.csv("SheetPullData.csv")
head(data)
fit <- lm(data$Sheets ~ data$Time_since_last_pull + data$Roll_Type+ data$Roll_ID)
summary(fit)