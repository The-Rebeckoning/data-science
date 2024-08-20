import streamlit as st
from toolhouse import Toolhouse
import requests


def slider():
    # Create a toggle switch with two options: "Yes" and "No"
    option = st.radio(
        'Enable better recipes?',
        options=['Yes', 'No'],
        index=None  # No default selection
    )

    # Display conditional text in the output only if an option is selected
    if option is not None:
        if option == 'No':
            st.write('Not enabled')
        else:
            st.write('Enabled')
    else:
        # Optional: If you want to explicitly show that no option is selected
        st.write('')

    return option


th = Toolhouse()

# The parameter must match the name of the tool in your tool definition
@th.register_local_tool("recipe_tool")
def recipe_tool (
   # Must match the name of the parameters in your tool definition
   keyword: str) -> str:
   
    url = f"https://www.allrecipes.com/search?q={keyword}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Error: {response.status_code} - {response.text}"
        

   
recipe_tool = [
    {
        "type": "function",
        "function": {
            "name": "recipe_tool",
            "description": "Get unique recipes based on your specific keyword for meals at differenet times of the day.",
            "parameters": {
                "type": "object",
                "properties": {
                    "keyword": {
                        "type": "string",
                        "description": "The keyword to search.",
                    },
                   
                },
            },
        }, 
        "required": [
            "keyword"
        ]
    }
]

