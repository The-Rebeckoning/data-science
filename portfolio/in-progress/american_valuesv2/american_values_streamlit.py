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

# Create the dataframe we'll then filter- this needs to be finalized for our analysis (eventually)
df = create_core_df('nonvoters_data.csv', column_names)

label_values = ["22-26","27-31","32-36","37-41","42-46","47-51","52-56","57-61","62-66","67-71","72-76","77-81","82-86","87-91","92-94"]
bins = [21,26,31,36,41,46,51,56,61,66,71,76,81,86,91,94]

create_bins(df,'ppage','age',label_values, bins)

# Filter the dataframe with the columns we need for our analysis

column_selection = ["Voting","Military Support","Believing in God","Protesting","Racism_US","Racism_Policing","weight","age","educ","race","gender","income_cat","voter_category"]

# Rename demographic columns for readibility
df = df.rename(columns = {"age":"Age","educ":"Education","race":"Race","gender":"Gender","income_cat":"Income","voter_category":"VotingFrequency"})

# Filter dataframe by demographic info for initial exploration of data
demographic_columns = ["Age","Education","Race","Gender", "Income","VotingFrequency"]



### INTERACTIVE EXPLORATORY HISTOGRAMS THAT HELP US EXPLORE OUR DATASET

demographic_df = filter_df(df, demographic_columns)

create_subheading("Understanding our data")
create_text("Learn more about the respondents in our dataset.")



demographic_select = st.selectbox(label="Choose a way to sort the data",options = demographic_columns)


demographic_df_filtered = demographic_df.loc[:,[demographic_select]].value_counts()
reset_df = demographic_df_filtered.reset_index()


fig = px.histogram(reset_df, x=demographic_select, y = 0) 
# Update y axis label
fig.update_layout(yaxis_title="Distribution in dataset")
st.write(fig)

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