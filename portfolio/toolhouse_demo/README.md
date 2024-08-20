# Set up

1. Create a `.env` file by copying `.env.template`.
2. Add the relevant API Keys for any of the LLM providers you want to use (to run this app, you need an OpenAI key).

You will also need `TOOLHOUSE_API_KEY`. If you don't provide an API key for a specific LLM provider, the Playground will throw an exception when you attempt to use it.

# How to run it on your own machine


1. Also clone the Toolhouse Repo:
   ```
   $ git clone https://github.com/toolhouseai/toolhouse-playground.git
   ```

2. Install the required dependencies:

   ```
   $ pip install -r requirements.txt
   ```

3. Launch the app:

   ```
   $ streamlit run toolhouse_Rebecca_demo.py
   ```

# Other helpful links

https://docs.toolhouse.ai/toolhouse/working-with-your-local-tools

