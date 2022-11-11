# Youtube_Video_Analysis

![Yt](https://user-images.githubusercontent.com/106944351/201234042-db372118-b1d8-4b86-9ba5-79c52e7a63eb.jpeg)

## Overview

Our goal is to create a machine learning model that will be trained to predict whether or not a youtube video has the potential to be viral. This will be based on features which include amount of subscribers that channel has, total amount of views on the channel and video, which category the video belongs to, and total amount of likes on the video. From these features, we will have over 7,000 videos to train and test this algorithm on so the model can learn which features best predict if the video will be viral. We are basing the term viral as a video that gets over 1 million views. If the video can get over 1 million views than it will be given the value of 1 which equates to viral. If the video would get less than 1 million views then it would be given the value of 0, for not viral.

We chose 1 million views as our differentiating point of viral vs. not viral. Due to a growing number of Internet and social media users, while still a big achievement, reaching that mythical million is no longer as much of a challenge. There are simply too many videos with that many views to make them all stand out. It’s safe to assume that currently, it’s better to aim at gaining at least [1 million views](https://mint.intuit.com/blog/relationships/how-much-do-youtubers-make/) to reap the benefits of going viral. If you can get 1 million views on your video that is the equivialant to about $5,000. So, to answer the question of how many views is viral - there is no simple answer here. In reality, not all viral videos are created equal, so the more views you get, the better, but for our machine learning model's sake, we chose 1 million views. 

## Contributors: 
1. Zara Khan - zaraxkhan - Circle Role

2. Kevin MacDonald - macdkw89 - Triangle Role

3. Justin Tapia - justint42 - X Role

4. Snehal Desavale - SNEHALDD - Square Role

## Presentation 
[Link to Google slides presentation](https://docs.google.com/presentation/d/1Bu-T2ZBeTqTyPBRMq8CEh9HJIoqKXN8aQOd7c9k1PV0/edit?usp=sharing)

## Resources

1. Youtube v3 API (https://www.googleapis.com/youtube/v3)
    - All data used in this project is sourced directly from the Youtube API
    - API Resources used
      - Channels
      - Comments
      - CommentThreads
      - Videos

2. Dataset Category References: 
   1. [Best Youtube Channels for every category](https://blog.hubspot.com/marketing/best-youtube-channels)
      - Using this article, we obtained each channel listed under each category for our purposes
      - We opted to not use the "Yoga" category due to its similarity to the "Fitness" category.
   2. [List of most-subscribed YouTube channels - Wikipedia](https://en.wikipedia.org/wiki/List_of_most-subscribed_YouTube_channels)
      - Using this link, we sorted the table and grabbed the top 20 English Language channels by subscriber count for use in our analysis
      - There are a handful of duplicate channels in this data when compared to the categorical channel list mentioned above. Our analysis will drop these to avoid duplicate entries.


3. Software : 
    - Python 3.9.12
    - Scikit-learn 1.0
    - Numpy 1.21.5
    - pandas 1.4.2
    - psycopg2-binary-2.9.5
    - vaderSentiment - SentimentIntensityAnalyzer

4. Relational Database : PostgresSQL 11 connected to AWS database server. 

5. Tools / Software : Tableau public, git, pgAdmin, VS Code.

## Prerequisites

Before you begin, Please ensure you have met the following requirements:

You have installed updated version of Python, VS Code, and related dependencies   

You have PostgresSQL 11 installed. 

You have created a database in AWS. 

You have access to Tableau public. 

## Installation

## Machine Learning Model
We are using machine learning to see if we can predict whether or not a YouTube video can reach 1 million views based on its subscriber count, channel view count, channel video count, amount of comments on the video, amount of likes on the video, the topic of the video, and the day of week the video was published. We are using 1 million as our numeric value of whether the video has the potential to be 'viral' or not. Below is the code we used to add the viral or not column from our dataset we created using Youtube's API. 

![code_for_viral_column](https://user-images.githubusercontent.com/105755095/201196386-c460bdf2-3feb-4ae8-824c-d409fd4be99e.png)

![code_for_viral_col_2](https://user-images.githubusercontent.com/105755095/201196399-abcbed6b-ef87-45e9-9e08-0f5fac5feae8.png)

### Preprocessing Data
In order to begin the Machine Learning portion, we must preprocess the feature set of the data. First we encoded the categorical data. We did this for the topic category column and the day of week published column. This turned the categorical values into numerical values. However, for the day of week published column, we decided to go with custom encoding so that the days of week were not assigned random numbers, but instead 1 started with Sunday and 7 was Saturday. You can see the code we used below to encode the columns and then add custom encoding to the last column. 

![encoding](https://user-images.githubusercontent.com/105755095/201197005-4c819df7-2ba3-4332-9a6a-a1cda5c92744.png)

![custom_encoding](https://user-images.githubusercontent.com/105755095/201197039-dfad346b-38bf-4505-9b05-22d1e5e77de9.png)

![final_custom_encoding](https://user-images.githubusercontent.com/105755095/201197053-f6656825-f06e-40af-9297-fc0e43d008ca.png)

#### Scaling the Data
Because our columns had some very large numbers, we thought it would be best to scale each column so that every column was on the same playing field. We did this with Standard Scaler from the sklearn package. This standardizes a feature by subtracting the mean and then scaling to unit variance. Unit variance means dividing all the values by the standard deviation. 

![Screen Shot 2022-11-09 at 5 43 19 PM](https://user-images.githubusercontent.com/105755095/201197525-6971f879-26dd-468c-8fb8-8028bbeb0dc8.png)

![scaled_for_ml](https://user-images.githubusercontent.com/105755095/201197546-0f755aef-017f-43a7-9682-0d0374f87dff.png)

### Feature Selection
We selected the features for our machine learning by deciding what data points would effect how much a video is viewed. The first thing we thought of was the channel that posted the video. If the channel has many subscribers than the potential for the video being viewed increases. This is the same thought process we had for the total views the channel has ever had. The more views a channel has had can give a good idea that they are going to continue getting many views. But this can be affected by the amount of videos on their channel. We assumed that the more videos a channel posts, there is a potential that they one of those videos will get many views. 

We also thought categorical data was important to include in our feature selection process. We included the topic category of the channel because some topics may get more views than others. Same goes for the day of week the video was published. We wanted to see if there was a correlation between when a video was published to the amount of views that the video will get. 

The video data itself also seemed like a legitiment feature to include as the amount of comments a video is getting and being talked about can affect the amount of views a video gets. And finally, we felt as though the like count on a video can be a predictor of whether or not the video will gain attraction. 

![Correlation_Matrix](https://user-images.githubusercontent.com/105755095/201199625-ac2f5d9f-c37f-4db8-83ab-1cd9e040fe10.png)

Above shares how the numerical features correlate with one another. 

### Splitting Data
We split the data using sklearn's train_test_split function. This split our data as the default 80% for training and 20% for testing.

![train_test_split](https://user-images.githubusercontent.com/105755095/201200037-0217adac-3078-45ac-88c5-94e5fff53e3d.png)

We used this split the first time around for our machine learning portion, before we remebered that our data might be imbalanced. So with the value count function, we checked how many of the rows were given the 1 for 'viral' and how many were given the 0 for 'not viral' and this is what was shown:

![y_value_count](https://user-images.githubusercontent.com/105755095/201200265-1825b3d8-815a-426a-ac93-cfa2c2e8b38a.png)

![percent_targets](https://user-images.githubusercontent.com/105755095/201201604-0a60e710-2e34-4bf0-b954-3306d3b43b92.png)

![graph_target](https://user-images.githubusercontent.com/105755095/201201658-e2d6abe6-268e-4700-8c79-ae75cc993bef.png)

Our data was very imbalanced and we needed to use a function that would balance this data. Our instructor suggested we use SMOTEENN as it does both undersampling and oversampling at the same time. After resampling our data, we rechecked the y values and the numbers we much more balanced than before. 

![smoteenn_code](https://user-images.githubusercontent.com/105755095/201200693-6b314a72-9f8f-4cd7-b1aa-7cf092287b8d.png)

### Model Choice 
Our group choice 3 different machine learning models for our dataset. We started off with the most obvious choice for binary classification which was the Logistic Regression Model. It is a simple model to use and gave a great accuracy score, however, the precision of the viral target was the lowest of the 3 at 87%. This may be die to the fact that that this model is prone to overfitting on the training data. The next model we chose was the Random Forest Model. It was a little slower than the Logistic Regression Model to train, but was the most effective with the best accuracy, presicion, and recall score. We used this model because it is known for both regression and classification, while also preventing overfitting. The last model we used was Adaboost. This was because we wanted to see if this model would be able to do a better job than the Random Forest Model. It did better than the Logistic Regression Model, however it took a longer time than any of the models to train and since our model has a lot of outliars, it was not the best fit for our dataset. We considered it beacause it is refressed to as the best classifier, but due to the outliars in our model, it was not for our dataset. Random Forest did a great job in processing our features and performing on our testing data. 

### Changes in our Model
The biggest change we made to our model was when we resampled our data and redid the machine learning for all 3 models. This showed a great change in our Classification Reports, especially when it came to the precision of our models calculating if the video was viral. Below are the classification reports and the changes that occured due to the resampling. 
#### Logistic Regression
Before Resampling:

![ClassReport_LR](https://user-images.githubusercontent.com/105755095/201206248-13f8a908-6056-414e-b91d-a0e5bf9ac25b.png)


After Resampling:

![ClassReport_LR_RS](https://user-images.githubusercontent.com/105755095/201206278-5cf319b3-11e6-4bdd-b67a-0eb44465187c.png)


#### Random Forest Model
Before Resampling:

![CLassReport_RF](https://user-images.githubusercontent.com/105755095/201206363-226ac289-1b57-4377-94ae-5356479712d4.png)


After Resampling:

![ClassReport_RF_RS](https://user-images.githubusercontent.com/105755095/201206387-41423988-3526-465e-86ca-08daf3aa6173.png)

#### Easy Ensemble AdaBoost Model
Before Resample:

![ClassReport_EE](https://user-images.githubusercontent.com/105755095/201206215-6c0452b4-3393-4cc3-b3a8-9672e189db49.png)


After Resampling:

![CR_EE_RS](https://user-images.githubusercontent.com/105755095/201206472-db0b4660-9d28-4e48-881b-92bae96a77cc.png)


### Results from our Machine Learning Model
The RandomForest model did a great job in training and learning which features make for a viral video. Giving us an almost 98% accuracy score, the model is able to predict with the features which video will gain 1 million views. It was able to even categorize which features were the most important when making it's calculations:

![Feature_Importance](https://user-images.githubusercontent.com/105755095/201209337-1609cb8a-8209-46b5-8264-0f813bcbe025.png)

Below are the accuracy scores for all 3 models we used;

#### Logistic Regression
Before Resampling:

![AccuracyScore_LR](https://user-images.githubusercontent.com/105755095/201204409-790dad59-f1ea-4fe1-824d-6353902b1a0a.png)


After Resampling:

![accuracyscore_LR_RS](https://user-images.githubusercontent.com/105755095/201204415-13f1e1ab-1617-44bf-b2ff-7f6f61cd9f35.png)


#### Random Forest Model
Before Resampling:

![AccuracyScore_RF](https://user-images.githubusercontent.com/105755095/201204440-286a1556-99ff-490d-a411-3265f57eb218.png)


After Resampling:

![AccuracyScore_RF_RS](https://user-images.githubusercontent.com/105755095/201204461-dfc1b217-de1f-4c6b-b6d3-91a83f0132fb.png)


#### Easy Ensemble AdaBoost Model
Before Resample:

![AccuracyScore_EE](https://user-images.githubusercontent.com/105755095/201204358-c2d05b99-23a8-434b-aaaa-ffcfee964a18.png)

After Resample:

![AccuracyScore_EE_RS](https://user-images.githubusercontent.com/105755095/201204399-585b0d69-bda0-4249-95a9-c5f89449df3d.png)


## Database Integration
We created a database in [Amazon Web Services](https://aws.amazon.com/) and connected the host,database, user, and password onto a new server on PostgreSQL. We created two tables, one which contains information regarding the 178 [channel data](https://raw.githubusercontent.com/SNEHALDD/Top_Youtube_Channels_Trend_Analysis/Zara/Database/ready_for_sql/channels_data.csv) and the other which contains information about the 50 videos we gathered from each channel, the [video data](https://raw.githubusercontent.com/SNEHALDD/Top_Youtube_Channels_Trend_Analysis/Zara/Database/ready_for_sql/video_data.csv). We joined these files on the primary key which is the channel_id. 

![Screen Shot 2022-11-03 at 9 31 28 PM](https://user-images.githubusercontent.com/105755095/199872500-743d437b-1383-4d2d-92d3-bc02be676567.png)

![Screen Shot 2022-11-03 at 9 32 15 PM](https://user-images.githubusercontent.com/105755095/199872556-285db30e-ad21-40b3-a94c-cabef001b8c7.png)

This [joined file](https://raw.githubusercontent.com/SNEHALDD/Top_Youtube_Channels_Trend_Analysis/main/Database/ready_for_sql/joined_data.csv) stores all the information we will need in order to begin to train our machine learning model and create the best visualizations possible. 

### ERD
Here is the [ERD](https://github.com/SNEHALDD/Top_Youtube_Channels_Trend_Analysis/blob/main/Database/ERD.png) visual which makes the connection of both tables that we joined together to create our final dataframe.

![ERD](https://user-images.githubusercontent.com/105755095/199872407-748a5c31-53f4-4fd2-8765-d25994003606.png)

### Connecting to the database
As shown in this [file](https://github.com/SNEHALDD/Top_Youtube_Channels_Trend_Analysis/blob/Zara/Database/db_connection.ipynb), we will be using psycopg to connect our database that is currently stored in the cloud, to our python file in order to do our machine learning model. 

## Dashboard

### Tool : Tableau Public

We will add visualizations of:
- Total number of subscribers of the channel,
- Total number of views on the video,
- Total number of likes on the video.
- Total length of the video.
- Ratio of number of subscribers to number of views.

Interactive element(s):
- Dropdown menu which will list names of all the categories. Once you choose the category, dashboard will show above charts and information of videos.
- Animation which shows which category was most viewed in the particular year.

[Link to Tableau Dashboard](https://public.tableau.com/views/YoutubeVideoAnalysis_16680643134020/Dashboard?:language=en-US&:display_count=n&:origin=viz_share_link)

## Contact 
If you want to contact us, you can reach us at

 zaraxkhan - [zxkhan.99@gmail.com](mailto:zxkhan.99@gmail.com)

 macdkw89 - [macdkw@gmail.com](mailto:macdkw@gmail.com) 

 justint42 - [tapiajustin42@gmail.com](mailto:tapiajustin42@gmail.com)

 SNEHALDD - [snehaldesavle3@gmail.com](mailto:snehaldesavle3@gmail.com)
