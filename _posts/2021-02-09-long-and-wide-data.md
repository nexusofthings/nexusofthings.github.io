---
title: "Managing long and wide data formats for data analysis"
date: 2021-01-03
categories:
  - Wrangling Data
tags:
  - Managing Data 
---


This is one of the most widely used operations in exploratory phase of any analysis. A proper understanding of data manipulation between long and wide formats of data will reduce a lot of pain - this is especially true when the data is unstructured.  

Load [tidyverse](https://www.tidyverse.org/) set of packages to replicate things below.

![image](/assets/images/managing-long-and-wide-data-formats-for-data-analysis1.png)

```
library(tidyverse)

df1 <- tribble(~ID, ~x,
               "A", 1,
               "B", 2,
               "C", 3)

df2 <- tribble(~ID, ~y,
               "D", 4,
               "E", 5,
               "F", 6)

combined <- df1 %>% dplyr::full_join(df2)

```



https://stackoverflow.com/questions/25925556/gather-multiple-sets-of-columns?answertab=active#tab-top

https://jhudatascience.org/tidyversecourse/wrangle-data.html#reshaping-the-data

https://tidyr.tidyverse.org/articles/pivot.html

https://rdatatable.gitlab.io/data.table/





