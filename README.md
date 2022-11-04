# Top_Youtube_Channels_Trend_Analysis

![Image_Youtube_Trending](https://user-images.githubusercontent.com/106944351/199649897-df66341d-4029-40dd-b173-17aee2148b42.jpeg)

Image downloaded form : [How do youtube videos become trending?](https://medium.com/@melodyfs/how-do-videos-become-trending-on-youtube-2690a6622b7d)
## Overview

Our goal is to create a machine learning model that will be trained to predict whether or not a youtube video has the potential to be viral. This will be based on features which include amount of subscribers that channel has, total amount of views on the channel and video, which category the video belongs to, and total amount of likes on the video. From these features, we will have over 50,000 videos to train and test this algorithm on so the model can learn which features best predict if the video will be viral. We are basing the term viral as a video that gets over 200,000 views. If the video can get over 200,000 views than it will be given the value of 1 which equates to viral. If the video would get less than 200,000 views then it would be given the value of 0, for not viral. 

## Contributors: 
1. Zara Khan - zaraxkhan - Circle Role

2. Kevin MacDonald - macdkw89 - Triangle Role

3. Justin Tapia - justint42 - X Role

4. Snehal Desavale - SNEHALDD - Square Role

## Communication:

1. Slack - Created slack channel to share ideas, make decisions, have video calls, and move work forward with the assignments.

2. Google Drive - Used google drive to keep necessary files and folders in organized manner. We also share next meeting's agenda on this.

## Resources

1. Youtube v3 API (https://www.googleapis.com/youtube/v3)

2. Dataset : [Best Youtube Channels for every category](https://blog.hubspot.com/marketing/best-youtube-channels)

3. Software : 
    - Python 3.9.12
    - Scikit-learn 1.0
    - Numpy 1.21.5
    - pandas 1.4.2
    - psycopg2-binary-2.9.5

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
We are using machine learning to see if we can predict what category a channel belongs to based on its subscriberCount, viewCount, and videoCount.

Features: viewCount, subscriberCount, videoCount
Targer variable: category_title
![features](Resources/ml_features.png)

RandomForestClassifier
![ml_code](Resources/ml_code.png)

## Database Integration
We created a database in [Amazon Web Services](https://aws.amazon.com/) and connected the host,database, user, and password onto a new server on PostgreSQL. We created two tables, one which contains information regarding the 178 [channel data](https://raw.githubusercontent.com/SNEHALDD/Top_Youtube_Channels_Trend_Analysis/Zara/Database/ready_for_sql/channels_data.csv) and the other which contains information about the 50 videos we gathered from each channel, the [video data](https://raw.githubusercontent.com/SNEHALDD/Top_Youtube_Channels_Trend_Analysis/Zara/Database/ready_for_sql/video_data.csv). We joined these files on the primary key which is the channel_id. 

![Screen Shot 2022-11-03 at 9 31 28 PM](https://user-images.githubusercontent.com/105755095/199872500-743d437b-1383-4d2d-92d3-bc02be676567.png)

![Screen Shot 2022-11-03 at 9 32 15 PM](https://user-images.githubusercontent.com/105755095/199872556-285db30e-ad21-40b3-a94c-cabef001b8c7.png)

This [joined file]() stores all the information we will need in order to begin to train our machine learning model and create the best visualizations possible. 

### ERD
Here is the ERD visual which makes the connection of both tables that we joined together to create our final dataframe.

![ERD](https://user-images.githubusercontent.com/105755095/199872407-748a5c31-53f4-4fd2-8765-d25994003606.png)

## Dashboard

### Tool : Tableau Public

## Contact 
If you want to contact us, you can reach us at

 zaraxkhan - [zxkhan.99@gmail.com](mailto:zxkhan.99@gmail.com)

 macdkw89 - [macdkw@gmail.com](mailto:macdkw@gmail.com) 

 justint42 - [tapiajustin42@gmail.com](mailto:tapiajustin42@gmail.com)

 SNEHALDD - [snehaldesavle3@gmail.com](mailto:snehaldesavle3@gmail.com)
