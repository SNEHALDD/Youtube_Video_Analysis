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

## Machine Learning Model
We are using machine learning to see if we can predict whether or not a YouTube video can reach 1 million views based on its subscriber count, channel video count, the topic of the video, the length of the video, and the day of week the video was published. We are using 1 million as our numeric value of whether the video has the potential to be 'viral' or not. Below is the code we used to add the viral or not column from our dataset we created using Youtube's API. 

![code_for_viral_column](https://user-images.githubusercontent.com/105755095/201196386-c460bdf2-3feb-4ae8-824c-d409fd4be99e.png)

![code_for_viral_col_2](https://user-images.githubusercontent.com/105755095/201196399-abcbed6b-ef87-45e9-9e08-0f5fac5feae8.png)

Our machine learning question is which features, from the YouTube video itself and the YouTube channel, are most important in helping a video gain this viral view count of 1 million views.

### Preprocessing Data
In order to begin the Machine Learning portion, we must preprocess the feature set of the data. First we encoded the categorical data. We did this for the topic category column and the day of week published column. This turned the categorical values into numerical values. However, for the day of week published column, we decided to go with custom encoding so that the days of week were not assigned random numbers, but instead 1 started with Sunday and 7 was Saturday. You can see the code we used below to encode the columns and then add custom encoding to the last column. 

![encoding_code](https://user-images.githubusercontent.com/105755095/201760770-6c0e4609-a698-4fd6-8b5f-a3ccd36617ba.png)


![encoding_data_table](https://user-images.githubusercontent.com/105755095/201760784-871ee8d6-9fce-4887-827e-6c9e3a0b4cac.png)


![custom_encoding](https://user-images.githubusercontent.com/105755095/201197039-dfad346b-38bf-4505-9b05-22d1e5e77de9.png)


![custom_encoding_day](https://user-images.githubusercontent.com/105755095/201760835-46005efc-bcf1-43d4-b154-3c751717aca0.png)


#### Scaling the Data
Because our columns had some very large numbers, we thought it would be best to scale each column so that every column was on the same playing field. We did this with Standard Scaler from the sklearn package. This standardizes a feature by subtracting the mean and then scaling to unit variance. Unit variance means dividing all the values by the standard deviation. 

![scaling_code](https://user-images.githubusercontent.com/105755095/201760916-98c6da6b-add9-42b3-8a41-431b1c43516e.png)


![scaled_table](https://user-images.githubusercontent.com/105755095/201760928-d3787885-fcb5-4daf-b7bd-aaacb8805fd9.png)


### Feature Selection
We selected the features for our machine learning by deciding what data points would effect how much a video is viewed. The first thing we thought of was the channel that posted the video. If the channel has many subscribers than the potential for the video being viewed increases. This can be affected by the amount of videos on their channel. We assumed that the more videos a channel posts, there is a potential that they one of those videos will get many views, so we included that in our machine learning model to test if this was true. FInally, from the channel data we chose topic category as a feature, as well. This would help us analyze whether or not certain topics attract more attention than others and if it was a large enough variable to affect the views a video gets.  We did not want to include the channel's total view count as that would skew the data. We are not only trying to decide if channels with already a large following can reach 1 million views, but also if videos that are random can also reach this threshold. 
 
The video data itself also seemed like a legitiment feature to include. How long the video was could have an affect of whether or not people click on the video to view. What day of the week the video was published was also a feature point we were curious about. We wanted to know if the day it was published could affect the amount of views a video gets. However, these were the only two features we chose from the video data. The amount of comments a video is getting and the like count on a video can be a predictor of whether or not the video will gain attraction, but these features occur after a video has already been posted and gets views. We did not include these as our features because we felt as though it may mess up the features importance and predicting skills of the machine learning model. If the video gets many comments and likes, the machine learning model is going to skew that way in terms that it will get many views and therefore do not become good measurements for a viral video.  

After selecting our features, we did a quick correlation matrix to see how our variables correlate with eachother. We did not want each variable to be highly correlated with one another because that leads to multicollinearity, where it becomes a problem because our independent variables should be independent of one another. If the degree of correlation is too high, it can cause problems when we run our machine learning model. As we can see below, our features are not highly correlated with eachother which makes proceeding with the machine learning model viable. 


![correlation_heatmap](https://user-images.githubusercontent.com/105755095/201760962-bd7bdb67-18e6-4a90-8347-6e01b035d49c.png)


### Splitting Data
We split the data using sklearn's train_test_split function. This split our data as the default 80% for training and 20% for testing.

![resample_shape](https://user-images.githubusercontent.com/105755095/201760992-b8b22c88-bf44-44ac-951b-3f94c613e65a.png)


We used this split the first time around for our machine learning portion, before we remebered that our data might be imbalanced. So with the value count function, we checked how many of the rows were given the 1 for 'viral' and how many were given the 0 for 'not viral' and this is what was shown:

![resample_count](https://user-images.githubusercontent.com/105755095/201761010-e71f228c-b248-4138-b58d-27355f0a7816.png)


![data_imbalanced_percent](https://user-images.githubusercontent.com/105755095/201761029-76ad842d-1a50-4fb5-9831-8c185ea90ede.png)


![graph_target](https://user-images.githubusercontent.com/105755095/201201658-e2d6abe6-268e-4700-8c79-ae75cc993bef.png)

Our data was very imbalanced and we needed to use a function that would balance this data. Our instructor suggested we use SMOTEENN as it does both undersampling and oversampling at the same time. After resampling our data, we rechecked the y values and the numbers we much more balanced than before. 

![resample_smoteenn](https://user-images.githubusercontent.com/105755095/201761068-aa4281a3-d567-4938-ae70-e6debc919575.png)


### Model Choices 
Our group choice 3 different machine learning models for our dataset. We started off with the most obvious choice for binary classification which was the Logistic Regression Model. It is an easy and simple model to use which will get the job done. However, this model is prone to overfitting on the training data which is something we kept in mind when navigating this model. 

The next model we chose was the Random Forest Model. It was a little slower than the Logistic Regression Model whne we used it to train our data, but was the most effective with the best accuracy, presicion, and recall score. We used this model because it is known for both regression and classification, while also preventing overfitting. Even though it takes a little longer, it seemed to be the best at getting the job done with the best scores. 

The last model we used was Adaboost. This was because we wanted to see if this model would be able to do a better job than the Random Forest Model. It did better than the Logistic Regression Model, however it took a longer time than any of the models to train and since our model has a lot of outliars, it was not the best fit for our dataset. We considered it beacause it is referred to as the best classifier, but due to the outliars in our model, it was not for our dataset. 

Random Forest did the best job in processing our features and performing on our testing data. 

### Changes in our Model
The biggest change we made to our model was when we decided to change our features. The first time we trained our models, we had much more features, including channel's view counts, video's comment counts, and video's like count. We later realized that this was skewing our machine learning data as it was really focusing on the like count of the video to determine if the video will go viral. We realized that if we include these features, our machine learning model will overfit and focus too much on criterias that are usually determine after a video already has many views. Therefore, it would not be accurate to include features that occur due to many views as opposed to what features cause the views. This showed a great change in our Classification Reports, especially when it came to the precision of our models. Although our models got a lower accuracy and precision score, it made our model make more sense to what we were trying to answer. 

The model was retrained using the fit function included in all 3 libraries of our machine learning models. We simply cleaned up our table to include the features we thought were better fit for this analysis and refit our models. 

Below are the classification reports and the changes that occured due to the new feature selection. 

#### Logistic Regression
Before better Feature Selection:

![ClassReport_LR](https://user-images.githubusercontent.com/105755095/201206248-13f8a908-6056-414e-b91d-a0e5bf9ac25b.png)


After Feature Selection:

![LR_ClassReport](https://user-images.githubusercontent.com/105755095/201761105-5b335728-ce77-4e9c-b683-cba9cf3ce9df.png)



#### Random Forest Model
Before better Feature Selection:

![CLassReport_RF](https://user-images.githubusercontent.com/105755095/201206363-226ac289-1b57-4377-94ae-5356479712d4.png)


After Feature Selection:

![RF_ClassReport](https://user-images.githubusercontent.com/105755095/201761127-209b39f1-2ff5-4e41-8fd5-009821c831aa.png)


#### Easy Ensemble AdaBoost Model
Before better Feature Selection:

![ClassReport_EE](https://user-images.githubusercontent.com/105755095/201206215-6c0452b4-3393-4cc3-b3a8-9672e189db49.png)


After Feature Selection:

![EE_ClassReport](https://user-images.githubusercontent.com/105755095/201761135-032164ca-f595-42d0-a878-ceb7e3c9aeb9.png)


### Trying for the Greatest Accuracy Score
Since our RandomForest model gave us the best results, we tried a couple times to make changes to the amount of nodes and trees in order to give us a better accuracy score. However, it seems like our first attempt at the default setting was the best model we could use.

![RF_Attempt2](https://user-images.githubusercontent.com/105755095/201761181-80662750-96ef-4b00-8269-935e3707d38d.png)


![RF_Attempt3](https://user-images.githubusercontent.com/105755095/201761186-1e94fbe9-7edf-46e9-9645-9e333ff95da9.png)


![RF_Attempt4](https://user-images.githubusercontent.com/105755095/201761208-3ab42e68-6537-4fed-bebd-38e686d298d4.png)


### Accuracy, Precision, and Recall of our Models
Below are the accuracy scores for all 3 models we used, along with the confusion matrix and classification report with an explanation of what these numbers mean;

#### Logistic Regression
The Accuracy Score of this model was fair. at 87.6%, it was able to categorize whether a video was going to reach that 1 million mark most of the time. 

![LR_Accuracy](https://user-images.githubusercontent.com/105755095/201761260-95bdad6f-fea1-400c-bc52-0c90d520288a.png)


We can see from the confusion matrix, that model confused 142 videos as viral when they were actually below the 1 million mark, these are the false positves. The model predicted 118 videos as not viral even though they actually did gain more than 1 million views, these are the false negatives. 

![LR_CM](https://user-images.githubusercontent.com/105755095/201761268-133c6983-daa4-47c5-9ac7-dde0cef9585b.png)


The precision and recall for when the model was to predict a video under 1 million views was great. However, when it came to the precision and recall of the viral videos, it has a little more difficulty, as we saw from the confusion matrix. Precision scores share what percent of predictions were correct. So, looking at the classification report, only 68% of the true positives were labeled correctly. The other 32% of videos that were labeled as viral were actually not viral. This is a large chunk of videos falsely labeled.  Recall shares what percent of viral videos did the model catch. From this model as we can see below, logistic regression model was able to correctly identify 72% of the viral instances as viral and labeled the rest as not viral, even though they were. 

![LR_ClassReport](https://user-images.githubusercontent.com/105755095/201761277-16fef56f-1e85-460e-8204-0de4bb92f453.png)


#### Random Forest Model
This model had the best accuracy score at 93.9%. This model was the best at predicting which video goes in the viral vs non-viral category. 

![RF_Accuracy](https://user-images.githubusercontent.com/105755095/201761318-796dfac7-70fa-4b1f-bb68-f624819eadd2.png)


We can see from this model's confusion matrix that 107 videos that were labeled as viral were actually below the 1 million views mark, the false positives. Furthermore, only 24 videos that were actually above the 1 million mark were labeled as not viral. This is the false negatives number.

![RF_CM](https://user-images.githubusercontent.com/105755095/201761335-702df89f-361c-4dc8-8b9c-13498923eead.png)


The recall for this model was much better than the last. 94% of videos that were viral were labeled correctly as viral. The precision is still a little low, however, it is the best of what all 3 models could do. The models are all having alittle trouble labeling a video as viral, when infact it did not actually gain over 1 million views. 

![RF_ClassReport](https://user-images.githubusercontent.com/105755095/201761347-c1c65d45-aa77-4d9f-ade8-a0d9ad2c1092.png)


#### Easy Ensemble AdaBoost Model
For our last model, the accuracy score was at 90.9%, which is not bad at all but definently not the best. 

![EE_Accuracy](https://user-images.githubusercontent.com/105755095/201761385-2d02f6cc-b387-4a41-be6a-930c58a1ef8d.png)


This confusion matrix showed that 146 videos that were not viral were labeled as viral and those are the false positives. Only 39 videos that were actually viral were labeled as not viral, which is not too bad. These are the false negatives. 

![EE_CM](https://user-images.githubusercontent.com/105755095/201761396-1be0090e-209c-456b-b73f-eb2239ba5d38.png)


From the Classification Report, we can see that the recall ability was pretty high. For the recall score of the 1 label, the videos that were actually viral and labeled as not viral were not too many. However, the precision of this model for the viral videos was still pretty low as seen with the other 2 models. 72% of videos that were labeled as viral were correctly labeled, however, the other 28% of videos that were labeled as viral but were not actually above the 1 million view mark. 

![EE_ClassReport](https://user-images.githubusercontent.com/105755095/201761404-b308e227-fa11-4a86-bb14-cd80543862e1.png)


### Results from our Machine Learning Model
The RandomForest model did the best job in training and learning which features make for a viral video. Giving us the best accuracy score at 93%, as well as the highest pression and recall score, the model is the best at being able to predict with the features which video will gain 1 million views. And with one simple function, we were able to categorize which features were the most important when making it's calculations. So going back to our original question, which YouTube video and channel metrics play the biggest role in creating a video that will gain the largest amount of views?, below the bar graph answers our question. Subscriber count and the amount of videos seem to have the strongest correlation.

![features_graph](https://user-images.githubusercontent.com/105755095/201761450-4717fe61-44a9-49a0-80eb-514fc0d0e5ca.png)


## Database Integration
We created a database in [Amazon Web Services](https://aws.amazon.com/) and connected the host,database, user, and password onto a new server on PostgreSQL. We created two tables, one which contains information regarding the 178 [channel data](https://raw.githubusercontent.com/SNEHALDD/Top_Youtube_Channels_Trend_Analysis/Zara/Database/ready_for_sql/channels_data.csv) and the other which contains information about the 50 videos we gathered from each channel, the [video data](https://raw.githubusercontent.com/SNEHALDD/Top_Youtube_Channels_Trend_Analysis/Zara/Database/ready_for_sql/video_data.csv). We joined these files on the primary key which is the channel_id. 

![Screen Shot 2022-11-03 at 9 31 28 PM](https://user-images.githubusercontent.com/105755095/199872500-743d437b-1383-4d2d-92d3-bc02be676567.png)

![Screen Shot 2022-11-03 at 9 32 15 PM](https://user-images.githubusercontent.com/105755095/199872556-285db30e-ad21-40b3-a94c-cabef001b8c7.png)

This [joined file](https://raw.githubusercontent.com/SNEHALDD/Top_Youtube_Channels_Trend_Analysis/main/Database/ready_for_sql/joined_data.csv) stores all the information we will need in order to begin to train our machine learning model and create the best visualizations possible. 

### ERD
Here is the [ERD](https://github.com/SNEHALDD/Youtube_Video_Analysis/blob/main/Resources/ERD.png) visual which makes the connection of both tables that we joined together to create our final dataframe.

![ERD](https://user-images.githubusercontent.com/105755095/199872407-748a5c31-53f4-4fd2-8765-d25994003606.png)

### Connecting to the database
As shown in this [file](https://raw.githubusercontent.com/SNEHALDD/Youtube_Video_Analysis/main/data_loader.py), we will be using psycopg to connect our database that is currently stored in the cloud, to our python file in order to do our machine learning model. 

## Dashboard

### Tools : 
1) Git Dash
 - Following Visuaizations and graphs have been added:
   - Channel Category Metrics,
   - Top Channels,
   - Video Length Metrics,
   - Comment Sentiment Analysis,
   - Video Publishing Metrics,
   - Machine Leaning Visualization.

- Interactive element(s):
  - Created multiple metrics such as View Count, Subscriber Count, Comment Count,
  - Option for Category selection as per the requirement.

 [Link to Dashboard](http://kwmdata.pythonanywhere.com/page-1) 

2) Tableau Public
 - Following Visuaizations and graphs have been added:
   - Total number of Subscribers, Views, Likes, Comments of each Category,
   - Total number of Subscribers, Views, Likes, Comments of the Channel,
   - Total number of Views according to Video Length,
   - Popular Categories on the basis of Like Count.

- Interactive element(s):
  - Dropdown menu which will show list of all the categories. Once you choose the category, graph will show corelation between Video length and number of   views.
  - Animation which shows which category was most viewed in particular year.

 [Link to Tableau Dashboard](https://public.tableau.com/views/YoutubeVideoAnalysis_16680643134020/Test_Dashboard?:language=en-US&:display_count=n&:origin=viz_share_link)

## Contact 
If you want to contact us, you can reach us at

 zaraxkhan - [zxkhan.99@gmail.com](mailto:zxkhan.99@gmail.com)

 macdkw89 - [macdkw@gmail.com](mailto:macdkw@gmail.com) 

 justint42 - [tapiajustin42@gmail.com](mailto:tapiajustin42@gmail.com)

 SNEHALDD - [snehaldesavle3@gmail.com](mailto:snehaldesavle3@gmail.com)
