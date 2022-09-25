
import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd

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

good_american_columns = ["Voting","Military Support","Believing in God","Protesting"]
racism_columns = ["Racism_US","Racism_Policing"]

answer_columns = good_american_columns+racism_columns


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


### INTERACTIVE EXPLORATORY HISTOGRAMS THAT HELP US EXPLORE OUR THE ANSWERES TO OUR QUESTIONS
create_subheading("What does the general population think about American values?")
create_text("Learn more about the respondents in our dataset.")

### Create dataframe for specific questions 

full_column_list = demographic_columns+good_american_columns+racism_columns

# Will need to relabel 1-4 as agree and disagree and then group by demographic variables


full_df = filter_df(df,full_column_list)


# Try with voting

conditions = [
  np.logical_and(df['Voting'].gt(1), np.less_equal(df['Voting'], 2)),
  np.logical_and(df['Voting'].gt(2), np.less_equal(df['Voting'], 3)),
  np.logical_and(df['Voting'].gt(3), np.less_equal(df['Voting'], 4)),
]

outputs = ["Somewhat important","Not so important","Not at all important"]


full_df['Voting-new'] = pd.Series(np.select(conditions, outputs, 'Very important'))

voting_columns = ['Voting-new','Age']

voting_df = filter_df(full_df, voting_columns)

st.write(voting_df.value_counts())

voting_df = voting_df.query('Age=="72-76"')

st.write(voting_df)
fig = px.histogram(voting_df, x = "Voting-new",color = "Age",barmode="group")
st.write(fig)
voting_df = filter_df(full_df, voting_columns)
fig = px.histogram(voting_df, x = "Voting-new",color = "Age",barmode="group")
st.write(fig)

st.write(voting_df)




### Being a good American
# Select the columns we want for our dataset
good_american_columns = good_american_columns
good_american_df = filter_df(full_df, good_american_columns)

# Restructure dataframe so that we can have number of responses for reach question
good_american_df = good_american_df.melt(var_name="Response",value_name="Value")
good_american_df  = good_american_df[good_american_df["Value"] > 0]

create_subheading("Being a Good American")
create_subheading("**In your view, how important are each of the following to being a good American?**\n")
create_subheading("***Responses***\n\n")
create_text("""
        1. Very important
        2. Somewhat important
        3. Not so important
        4. Not at all important""")
create_subheading("Voting in elections")
chart_data = good_american_df[ (good_american_df['Response'] == "Voting" )]

#fig = px.histogram(chart_data, x = "Value", nbins=4,labels=[1,2,3,4],barmode="group")
fig = px.histogram(chart_data, x = "Value", barmode="group")
st.write(fig)

create_subheading("Supporting the military")
chart_data = good_american_df[ (good_american_df['Response'] == "Military Support" )]
fig = px.histogram(chart_data, x = "Value", nbins=4,labels=[1,2,3,4],barmode="group")
st.write(fig)
create_subheading("Believing in God")
chart_data = good_american_df[ (good_american_df['Response'] == "Believing in God" )]
fig = px.histogram(chart_data, x = "Value", nbins=4,labels=[1,2,3,4],barmode="group")
st.write(fig)
create_subheading("Protesting if you believe government actions are wrong ")
chart_data = good_american_df[ (good_american_df['Response'] == "Protesting" )]
fig = px.histogram(chart_data, x = "Value", nbins=4,labels=[1,2,3,4],barmode="group")
st.write(fig)




### Systematic Racism
# Select the columns we want for our dataset
racism_columns = racism_columns
racism_df = filter_df(df, racism_columns)

# Restructure dataframe so that we can have number of responses for reach question
racism_df = racism_df.melt(var_name="Response",value_name="Value")
racism_df = racism_df[racism_df["Value"] > 0]


create_heading("Systematic Racism")
create_subheading("How much do you agree or disagree with the following statements?")
create_subheading("***Responses***\n\n")

create_text("""
        1. Strongly agree
        2. Somewhat agree
        3. Somewhat disagree
        4. Strongly disagree""")
create_subheading("1. Systemic racism is a problem in the United States.")

chart_data = racism_df[ (racism_df['Response'] == "Racism_US" )]
fig = px.histogram(chart_data, x = "Value", nbins=4,labels=[1,2,3,4],barmode="group")
st.write(fig)

create_subheading("""2. Systemic racism in policing is a bigger problem than violence and vandalism in protests.""")

chart_data = racism_df[ (racism_df['Response'] == "Racism_Policing" )]
fig = px.histogram(chart_data, x = "Value", nbins=4,labels=[1,2,3,4],barmode="group")
st.write(fig)





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