# TV-Brands-Market-EDA
This project uses Television Dataset from Kaggle

# DATASET DESCRIPTION

*This dataset has 912 samples with 7 features 
Here is a list of the features in this dataset:
1. **Brand**: This gives a list of different Tv Products.
2. **Size**: This indicates the screen sizes in inches.
3. **Resolution**: This is simply the Tv display category i.e *LED*, *HD*, e.t.c.
4. **Original Price**: This column list the original price of the product from the manufacturer.
5. **Selling Price**: This Column consist of the Selling price or the discounted price of the Tv.
6. **Operating System**: This gives the list of different OS used by the Tv, i.e *ANDROID*, *LINUS*, e.t.c.
7. **Rating**: Average customer rating of each product on a scale of 5.


# This project is intended to answer the following questions:.

*What are the Tv demands in the market based on brands\
*What are the top brands in the market based on demand\
*Relationship between Tv resolution and selling price\
*The Most available operating system in the market\
*Average selling price by Brand\
*Tv Rating by brand\
*Average discount price by brand.


## EXPLORATORY DATA ANALYSIS OF TV 

There are 912 rows and 7 columns in this dataset and this can be obtained using the python pandas library i.e *df.shape*.\
Based on the unique value of each attribute. Here is a summary of the unique values for each attribute and this can be obtained using this line of code: df.nunique().\
*Brand : 59 manufacturers in total.\
*Resolution: 5 resolution in total.\
*Size: 27 distinct Tv screen sizes in total.\
*Operating System: 7 Tv OS types in total.

#Top 5 Tv Brands in the Market based on count.


**SAMSUNG**: 146 products.\
**LG**: 122 products.\
**SONY**: 62 products.\
**TCL**: 44 products.\
**PANASONIC** 30 Products.

# Relationship between Tv resolution and selling price.

![Resolution](resolution.png).

![Average Selling Price Vs Resolution](Selling.png).

# The Most available operating system in the market.

![Distribution of operating system](OperatingSystem.png).


# Average selling price by Brand.

![Average Selling price by Brand](Averagesellingpricebybrand.png).


# Tv Rating by brand.

![Average Tv Rating By Brand](TvRatingbyBrand.png).


# Average Discount Price by brand.

**Discounted Price = Original Price - Selling Price **


![Distribution of Average Discount Price by Brand](Distribution.png).


