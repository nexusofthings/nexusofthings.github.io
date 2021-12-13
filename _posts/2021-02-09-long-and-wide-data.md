---
title: "Managing long and wide data formats for data analysis"
date: 2021-01-03
categories:
  - Wrangling Data
tags:
  - Managing Data 
---


This is one of the most widely used operations in exploratory phase of any analysis. A proper understanding of data manipulation between long and wide formats of data will reduce a lot of pain - this is especially true when the data is unstructured.  

We can  utilize pivot_* functions in [tidyr R package](https://tidyr.tidyverse.org/articles/pivot.html) for these tasks (they were called as gather() and spread() functions before). 

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

[RStudio cheatsheets](https://github.com/rstudio/cheatsheets/blob/main/data-transformation.pdf) are a great way to start exploring more related functions. Like many other tasks in R, there are alternative ways to do these tasks and [data.table](https://cran.r-project.org/web/packages/data.table/vignettes/datatable-intro.html) package offers range of flexible functions. 


https://stackoverflow.com/questions/25925556/gather-multiple-sets-of-columns?answertab=active#tab-top


Additional Resources: Can find more detailed information [here](https://jhudatascience.org/tidyversecourse/wrangle-data.html#reshaping-the-data) and [here](https://rdatatable.gitlab.io/data.table/)





