import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

st.title("Predicting CO2 Emission of Car")
df = pd.read_csv("CO2 Emission of car.csv")
fig, ax = plt.subplots()
nav = st.sidebar.radio("Navigation", ["View Dataset", "Data Analysis", "Data Visualization", "Prediction"])
if nav == "View Dataset":
    choice = st.checkbox("Click here to view dataset...")
    if choice:
        st.write(df)
        st.write(f"The dataset has {df.shape[0]} rows and {df.shape[1]} columns")
if nav == "Data Analysis":
    st.header("1:Summary of the Data")
    st.write(df.describe())
    st.header("2:Shape of the Data")
    st.write(df.shape)
    st.header("3:Top 5 rows of the Data")
    st.write(df.head(5))
    st.header("4:Last 5 rows of the Data")
    st.write(df.tail(5))
    st.header("5:Random 5 rows of the Data")
    st.write(df.sample(5))
    st.header("6:Checking Null values present or not")
    st.write(df.isnull().sum())
    st.write(f"{df.isnull().sum().sum()} null values present")
    st.header("7:Checking Duplicated values present or not")
    st.write(df.duplicated().sum())
    st.write(f"{df.duplicated().sum()} duplicate  values present")
    st.header("8:Correlation of each column in data")
    st.write(df.corr())

if nav == "Data Visualization":
    plots = st.radio("Visualization", ["Univariate Analysis", "Bivariate Analysis"])
    if plots == "Univariate Analysis":
        st.header("1:Count of Cars and Car Model columns")
        st.subheader("Count of Cars")
        val_count1 = df["Car"].value_counts()
        st.write(val_count1)
        st.subheader("Count of Car Model")
        val_count2 = df["Model"].value_counts()
        st.write(val_count2)

        st.header("2:Histogram of Volume and Weight columns")
        st.subheader("Histogram of Volume Column")
        ax.hist(df["Volume"])
        plt.xlabel("Volume")
        st.pyplot(fig)

        st.subheader("Histogram of Weight Column")
        ax.hist(df["Weight"])
        plt.xlabel("Weight")
        st.pyplot(fig)


    if plots == "Bivariate Analysis":
        st.header("1:Scatter Plot of Volume and Weight columns")
        ax.scatter(df["Volume"], df["Weight"])
        plt.xlabel("Volume")
        plt.ylabel("Weight")
        st.pyplot(fig)

        st.header("2:Scatter Plot of Weight and Volume columns")
        ax.scatter(df["Weight"], df["Volume"])
        plt.xlabel("Weight")
        plt.ylabel("Volume")
        st.pyplot(fig)

        st.header("3:Bar Plot of Car and Weight columns")
        ax.bar(df["Car"].head(5), df["Weight"].head(5))
        plt.xlabel("Car")
        plt.ylabel("Weight")
        st.pyplot(fig)

        st.header("4:Bar Plot of Car and Volume columns")
        ax.bar(df["Car"].head(5), df["Volume"].head(5))
        plt.xlabel("Car")
        plt.ylabel("Volume")
        st.pyplot(fig)

if nav=="Prediction":
    x=df[["Weight","Volume"]].values
    y=df["CO2"].values
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)
    reg=LinearRegression()
    reg.fit(x_train,y_train)
    y_pred1 = reg.predict(x_test)
    weight=st.number_input("Enter the Weight of Car in kg")
    if weight:
        st.write(f"Weight of Car is {weight} kg")
    volume=st.number_input("Enter the Volume of Car in centimeter cube (cm3)")
    if volume:
        st.write(f"Volume of Car is {volume} cm3")

    button=st.button("Predict")
    if button:
        y_pred = reg.predict([[volume, weight]])
        st.success(f"The CO2 Emission of the Car is {round(y_pred[0],2)}")
