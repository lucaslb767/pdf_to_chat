# pdf_to_chat
Use a pdf to give context to a ChatBot to help you through. This project will start with OpenAI. Maybe in the future will have other LLM models

To start with, create a .env file with your OpenAI API key at: https://platform.openai.com/settings/organization/api-keys

**COPY THE API KEY**. You will only have one oportunity to copy. Otherwise you will have to create another (it's free, so it is not much problem). 

Once you have the api key, in the .env file, create a variable in UpperCase, `OPENAI_API_KEY = YOUR_API_HERE` 
![image](https://github.com/user-attachments/assets/e3a926ff-353d-469f-bb40-873b9fc0dd2c)

Install the required modules with the following command : `pip install -r requirements.txt`

To run the front-end part, use : `streamlit run home.py`
