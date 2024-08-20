import streamlit as st
from llms import llms, llm_call
import dotenv
from st_utils import print_messages, append_and_print

dotenv.load_dotenv()

# Sets up the page
st.set_page_config(
    page_title="Anytime bites",
    page_icon="🥣"
)

# Update to relevant model and provider
# Find options in LLM library
MODEL = 'gpt-4o'
PROVIDER =  "GPT-4o"


if "messages" not in st.session_state:
    st.session_state.messages = []

if "user" not in st.session_state:
    st.session_state.user = ''

if "stream" not in st.session_state:
    st.session_state.stream = True

if "provider" not in st.session_state:
    st.session_state.provider = llms.get(next(iter(llms))).get('provider')
    
# Update title
st.title("Recipes, around the clock 🍽️ ")

# Import our local tool
from local_recipe_tool import th, recipe_tool, slider



st.logo(
    "logo.svg",
    link="https://toolhouse.ai")


with st.sidebar:
    # Update Title
    st.title("🥣 Anytime Bites")
    st.session_state.stream = st.toggle("Stream responses", True)

    # Update username 
    user = st.text_input("User", "Rebecca")
    st.divider()
    
    # Create slider
    enable_custom_tool = slider()   

    # Enables local tools 
    if enable_custom_tool == "Yes":
        tools = th.get_tools() + recipe_tool
    else:
        tools = th.get_tools()  

    # Allows user to select tools installed in Toolhouse 
    if not tools:
        st.subheader("No tools installed")
        st.caption("Go to the [Tool Store](https://app.toolhouse.ai/store) to install your tools.")    
    else:
        st.subheader("Installed tools")
        for tool in tools:
            tool_name = tool["function"]["name"]
            st.page_link(f"https://app.toolhouse.ai/store/{tool_name}", label=tool_name)
        
        st.caption("\n\nManage your tools in the [Tool Store](https://app.toolhouse.ai/store).")

th.set_metadata("timezone", -7)
if user:
    th.set_metadata("id", user)

print_messages(st.session_state.messages, st.session_state.provider)


# Update to relevant prompt based on demo
if prompt := st.chat_input(f"So you're pretty hungry?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with llm_call(
        provider=PROVIDER,
        model=MODEL,
        messages=st.session_state.messages,
        stream=st.session_state.stream,
        tools=tools,
        max_tokens=4096,
    ) as response:    
        completion = append_and_print(response)
        tool_results = th.run_tools(completion, stream=st.session_state.stream, append=False)

        
        while tool_results:
            st.session_state.messages += tool_results
            with llm_call(
                provider=PROVIDER,
                model=MODEL,
                messages=st.session_state.messages,
                stream=st.session_state.stream,
                tools=tools,
                max_tokens=4096,
            ) as after_tool_response:
                after_tool_response = append_and_print(after_tool_response)
                tool_results = th.run_tools(after_tool_response, stream=st.session_state.stream, append=False)
                