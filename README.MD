# Why Sentiment Analysis on Monuments?

The tourism sector, with a raising economic importance, has increased the importance of understanding how and why tourists evaluate the attributes that contribute to the attractiveness of a tourist location like cultural heritage and monuments of one’s country.

Although there is research on the feedback of those who visit particularly few tourist places across Europe, this project stands out of the rest and seeks to be innovative in the objective of obtaining insights about the top most famous 123 monuments and cultural heritage sites attractiveness across the world as a tourist destination, based on the feedback of tourists in the Google Maps Reviews, and get the most famous monuments based on their sentiment scores as well as ratings.

# Data Collection

The source of data collection is Google Maps reviews, from which a minimum of 1000 reviews has been collected per monument along with rating and other details.

The data is scraped from Google Maps with the help of a customized coded scraper which extracts the information like the monument name, reviewer name, review time and rating along with the complete text review. The data collected is stored in csv format which is further used for analysis.

Kindly download the datatsets from Kaggle. The link is: https://www.kaggle.com/datasets/karanagrawal7/monument-sentiment-analysis-dataset

- Final.csv: There are 123 famous monuments and cultural heritages in total from all across the world with 35+ places from India in the CSV.
Some of the famous ones are as follows:
 - Taj Mahal - Agra 
 - The Colosseum - Rome, Italy 
 - Potala Palace – Lhasa, Tibet, China 
 - Acropolis of Athens - Athens, Greece 
 - Eiffel Tower - France Paris 
 - Burj Khalifa — Dubai, UAE 

- Monument_List: Contains the entire monument list

- Reviews_Cleaned: Cleaned CSV with all cleaned reviews 

- Reviews_With_Scores: Cleaned CSV with all cleaned reviews and the sentiment scores 

# Scraper

Dynamic Web Scraping is done using Selenium package. Home is the main python file whereas Analysis is the second subset file which can be put inside the folder "pages"

# Dashbaord

Dashboard has been created using Streamlit package








