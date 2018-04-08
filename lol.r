
slicedatamonth <-slicedata %>%
  mutate(date = as.Date(date, format="%Y-%m-%d")) %>%
  mutate(year = format(date,'%Y'))  %>%
  mutate(year = as.numeric(year, '%Y')) %>%
  filter(year == 2017)
slicedatamonth <-slicedatamonth %>%
  mutate(month = format(date,'%m'))  %>%
  mutate(month = as.numeric(month, '%m'))

slicedatamonthfilterlowerededucation$educationRequirement <- as.factor(slicedatamonthfilter$educationRequirement)
slicedatamonthfilterlowerededucation <- slicedatamonthfilterlowerededucation %>%
  mutate(edReq = case_when(  
    educationRequirement  == 0 ~ "None",
    educationRequirement  == 'None' ~ "None"
  ))



slicedatamonthfilterlowerededucation <- slicedatamonth %>%
  filter(edReq == "None", country == "US", stateProvince == "CA", 
         supervisingJob == 1, normTitleCategory == "finance", unique(jobId)) 

aggregate(clicks ~ month, slicedatamonthfilterlowerededucation, mean) %>%
  ggplot(aes(y = clicks, x = month )) + geom_point() +
  geom_smooth(method = "lm", aes(colour = "Linear"))
