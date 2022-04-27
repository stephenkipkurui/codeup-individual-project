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
- With regards to gun violence, race and gun violence are related. 
- Gun related police shootings account for over 53% of all crimes explored in this dataset.
- White community population accounts for over 50% of sample in this set. It is possible that understanding race in other communities other than white may lack complete accuracy. With this in mind assuming the data represent America diversity, the Caucasian community are killed way more in police related shootings than any other enthnic community. 
- Predicting gun violence with classification modeling approach, resulted with Random Forest prediction accuracy of 99.90% over the baseline of 56.37%.


## Future work
- Would like to continue exploration with this dataset reviewing features such as location factors (city, state) of gun violence and how they differ with other crimes as well, the age of the victim/ suspect, how gender factors are in combinations with other factors(gender dis proportionally vary with gun violence. Over 95% of all gun violence incidents are perpetrated by male suspects).
- With more data, we can examine factors such as proximity to social institutions like schools and public places as these places have experienced a lot of attentions in the media lately. Lastly, social-economic factors of the perpetrators as well as police shooting incidents histories would be beneficial in exploring further development in this important topic.


## Data Dictionary 

| Variable | Defination |
| --- | --- |
| race | Enthnic Classification of race (White, Black, Hispanic, Asian, Native & Other) | 
| Caucasians | Same refference as white |
| enc_arm_category | Armed suspect class one-hot encoded as (Unarmed 0, Unknown 1, Blunt instruments 2, Other unusual objects 3, Sharp objects 4, Vehicles 5, Multiple 6, Electrical devices 7, Piercing objects 8, Explosives 9, Guns 10) |
| gun_violence_percentage | Percentage of gun-related violence |
| race_gun_violence | Gun-related race proportions |
| manner_of_death | How suspect died. Comprises and one-hot encoded as (shot 0, shot and Tasered 1) |
| enc_attack_level | Perceived level of attach as reported by police one-hot encoded as (undetermined 0, attack 1, other 2) |
| enc_flee | Suspect fleeing from arrest one-hot encoded as (Not fleeing 0, Foot 1, Car 2, other 3) |
| enc_gender | Suspect's gender. One-hot encoded as (F 0, M 1) |
| enc_body_camera | Police officer's body camera one-hot encoded as bool (F 0, T 1) |
| enc_race | Shot suspect identifying race. Encoded as (White 0, Black 1, Hispanic 2, Native 3, Asian 4, other 4) |


## Appendix
Project GitHub Repository: gh repo clone stephenkipkurui/codeup-individual-project


