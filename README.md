# Gun Violence and Police Shootings in America

## Project Goal 

 The purpose for this project is to create a generalized pattern that will enhance our understanding of the relations of race, gun violence and police shootings in the United States through Data Science statistical analysis. The project follows data science pipeline  approach Planning >> Acquire >> Prepare >> Explore >> Model >> Delivery.

## Project Description 
Acquired data from the open-source Kaggle website (https://www.kaggle.com/code/gauravduttakiit/understanding-us-police-shootings/data) and saved a copy on local machine. Although the data appeared clean and well structured, some preparations were required such as dropping unnecessary columns, encoding categorical columns, drop duplicated columns- if any, and indexing the date column to datetime format. The data was split into train, validate and test sets in the ratios 55%:24%:20% respectively.

## Questions of Interest

- (1). Which crime category accounts for most gun related shootings in America?
- (2). Is there a relationship between race and gun violence?
- (3). With gun violence, is there a relationship between races and police level of lethal force (threat level)?
- (4). With gun violence, does the manner of death differ between races? 
- (5). With gun violence, does fleeing suspects likely to be shot based on race?

### project we followed the data science pipeline:

- Planning >> Acquire >> Prepare >> Explore >> Model >> Deliver

#### __Planning:__ 
- Reviwed project goals, brain-stormed the appropriate approach, deliverable and timeline. 

#### __Acquire:__
- Aquired data with module acquire.py from the open source Kaggle website through the link in the introduction and saved a .csv file under name 'shootings.csv'. 
- Data period covered by the data range from January 02, 2015 to June 13, 2020.

#### __Prepare:__
- Cleaned data by:
    - Dropping columns (id, and name)
    - Drop any duplicated data
    - Created new columns (year, month, day, week, quarter, gun_violence)
    - Encoded categorical data into numeric
    - Lower any upper case column name
    - Sploid the data into train, validate and test subsets.

#### __Explore:__
- Conducted exploration on the dataset to understand features relations to race, gun violence, suspect flee tendencies, threat level as perceived by police. 
- Summarized exploration findings backed by Chi^2 test reveal that race and gun violence share a relationship. This created the baseline approach for this project. 

#### __Model:__
- Conducted classification modeling techniques- Decision Tree, Random Forest, Linear Regression and K-Nearest Neighbor.
- Best model, Random Forest beat baseline in classifying gun violence by 99% to 56%. 

#### __Delivery:__
- The file named final_project.ipynb is the final notebook with summarized result for this project.

## Steps to Reproduce
- Create required file structure on your local machine.
- Using the acquire.py file, read the shootings.csv file using pandas pd.read_csv menthods.
- Prepare the data using the modules outlines in the prepare phase of this README.md file.
- In the explore.ipynb, use pandas, statistics, and visualizations techniques in the explore.py file to reproduce the same results.
- Review the Data dictionary below to match your variables with ones used in this project.
- Your final notebook should resemble the final_report.ipynb as mine.
- **Creativity has no measure- explore further and share your projects with me**.

## Key Findings
- With regards to gun violence, race and gun violence are related. Police 
-


## Future work
- 
- 

## Data Dictionary 




## Appendix
Project GitHub Repository: 


