from email import header
from venv import create
import streamlit as st
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import seaborn as sns

from american_library.main import create_heading
from american_library.main import create_text
from american_library.main import create_core_df
from american_library.main import create_subheading
from american_library.main import filter_df
from american_library.main import create_bins


create_heading("What were American values in Fall 2020?")

### CREATING OUR DATAFRAME

column_names = {"Q2_1":"Voting",
        "Q2_7":"Military Support",
        "Q2_9":"Believing in God",
        "Q2_10":"Protesting", "Q3_1": "Racism_US","Q3_2": "Racism_Policing"}

# Create the dataframe we'll then filter
df = create_core_df('nonvoters_data.csv', column_names)

label_values = ["22-26","27-31","32-36","37-41","42-46","47-51","52-56","57-61","62-66","67-71","72-76","77-81","82-86","87-91","92-94"]
bins = [21,26,31,36,41,46,51,56,61,66,71,76,81,86,91,94]

create_bins(df,'ppage','age',label_values, bins)

# Filter the dataframe with the columns we need for our analysis

column_selection = ["Voting","Military Support","Believing in God","Protesting","Racism_US","Racism_Policing","weight","age","educ","race","gender","income_cat","voter_category"]

demographic_columns = ["age","educ","race","gender", "income_cat","voter_category"]
demographic_df = filter_df(df, demographic_columns)



### INTERACTIVE EXPLORATORY HISTOGRAMS THAT HELP US EXPLORE OUR DATA

create_heading("Understanding our data")

x_values = ["educ","age","race","gender", "income_cat","voter_category"]

demographic_select = st.selectbox(label="Choose a way to sort the data",options = x_values)

def create_countplot(demographic_select, dataframe):
    """Creates distribution plot for categorical variables"""
    plt.figure(figsize=(8,5))
    plot_title = ("Distribution of "+demographic_select)
    plt.title(plot_title)
    sns.countplot(x=demographic_select,data = dataframe, palette='rainbow')

create_countplot(demographic_select, demographic_df)


st.write(filter_df)


## Create a dataframe that is grouped by values (with the counts)
## Graph it 




### INTERACTIVE EXPLORATORY HISTOGRAMS THAT HELP US EXPLORE OUR THE ANSWERES TO OUR QUESTIONS




### Being a good American
create_heading("Being a Good American")
create_subheading("***In your view, how important are each of the following to being a good American?***\n")
create_text("""
        1. Voting in elections 
        2. Supporting the military
        3. Believing in God
        4. Protesting if you believe government actions are wrong  
        """)
create_subheading("***Responses***\n\n")
create_text("""
        1. Very important
        2. Somewhat important
        3. Not so important
        4. Not at all important""")

### Systematic Racism






## What is means to be a good American

### General population

#### Create interactive histogram that allows the user to see how respondent's reported on this question. 
#### This will not breakdown the questions by demographic criteria

### Analysis by demograhic


### Education
### Age
### Race
### Gender
### Class
### Voting history

## Systemic racism

### General population
### Education
### Age
### Race
### Gender
### Class
### Voting history

# Our insights

# Ourtakeways