# CO2-Emission

********* You must import CO2.new and CO2_transpose into your Jupyter environment First!


I made a regression machine learning model for this data to predict CO2 emissions in the world with Scikit-learn and Neural Network in the JupyterLab environment.
CO2 emissions (metric tons per capita)
I made a regression machine learning model for this data to predict CO2 emissions in the world with Scikit-learn and Neural Network.

Fixing the data:

First, I checked for the indicators. The result was that they are all  'CO2 emissions (metric tons per capita)'. Then I removed the columns we don't need to train the model with ('Country Name', 'Country Code', 'Indicator Code', 'Indicator Name'). Then I filled the NaN values with the 'bfill' method and removed the rows in which all of their values were zero. Also, I replaced zero values with the 'bfill' method. 

Training and splitting the data:

I used both Sklearn and TensorFlow to train this model. For the Sklearn section, the X_train is 192 countries from 239 countries, and X_test is the values for other countries. I chose the SVR method and StandardScaler for preprocessing. The QuantileTransformer resulted in negative values in predicting, so the StandardScaler was a better choice. The GridSearch showed that epsilon= 0.1 and degree=1 are the best parameters for this model. The score for X_test and y_test was pretty good (0.9969)
For the Neural Network section, I split the data into three training/ Cross Validation/ Test lists. I made a function to calculate mean square error too. The model has three dense layers with 5, 5, and 1 unit. The loss is MeanSquaredError and the optimizer is Adam(0.01). After 100 epochs the error for training the data and CV data was: 0.082 and 0.138. It's great because they show that we don't have underfitting and overfitting. At the end, you can see the prediction for X_test in the pandas data frame.
