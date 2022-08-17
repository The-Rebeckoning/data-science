import streamlit as st
import pandas as pd
import numpy as np

def create_heading (text):
    """Creates a heading"""
    heading = st.header(text)
    print (heading)

def create_subheading (text):
    """Creates a subheading"""
    subheader = st.subheader(text)
    print (subheader)

def create_text (text):
    """Creates a text"""
    text = st.text(text)
    print (text)

def create_core_df (filepath, column_names):
    """Creates dataframe that has all columns"""
    df = pd.read_csv(filepath)
    # Take the column names dictionary parameter and use those values to rename our columns
    df = df.rename(columns=column_names)
    return df

def create_bins(dataframe, column, new_column_name, label_values, bins):
    """Function to create bins for our data"""
    dataframe[new_column_name] = pd.cut(dataframe[column], bins, labels = label_values)

def filter_df (dataframe, column_selection):
    """Filter the dataframe for the columns we want"""
    core_df = dataframe.copy().loc[:,column_selection]
    return (core_df) 

 


