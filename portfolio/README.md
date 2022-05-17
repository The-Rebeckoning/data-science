# What the enneagram says about the traits we value most


This is a Jupyter Notebook where I'll explore the relationship between an individual's enneagram and the likelihood that they agree with their type's description. 

See Emmy Kegler's [crowd-sourced database of individuals' personality sets](https://docs.google.com/forms/d/e/1FAIpQLScyC83C8slwxbbryc4bGHoM3SVGeDg6-o0Yos3FMF7zN5nquw/viewform) for the original data.


The dependencies for are pandas, regex, pandasql and seaborn.


    import pandas as pd
    from pandasql import sqldf
    import seaborn as sns 
    import regex as re

