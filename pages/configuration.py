import streamlit as st
import json
from configs import get_config
from utils import FILE_DIRECTORY, create_conversation_chain

def config_page():
    st.header('Configuration Page', divider= True)

    model_name = st.text_input("Change Model", value=get_config('model_name'))
    retrieval_search_type = st.text_input("Change Retrieval type",value=get_config('retrieval_search_type'))
    retrieval_kwargs = st.text_input("Change Retrieval Parameters", value=json.dumps(get_config('retrieval_kwargs')))
    prompt = st.text_area('Change the default prompt', height= 350, value=get_config('prompt'))

    if st.button('Change Parameters', use_container_width=True):
        retrieval_kwargs = json.loads(retrieval_kwargs.replace("'",'"'))
        st.session_state['model_name'] = model_name
        st.session_state['retrieval_search_type'] = retrieval_search_type
        st.session_state['retrieval_kwargs'] = retrieval_kwargs
        st.session_state['prompt'] = prompt

    if st.button('Atualizar ChatBot', use_container_width=True):
        if len(list(FILE_DIRECTORY.glob('*.pdf'))) == 0:
            st.error('Adicione arquivos .pdf para inicilizar o chatbot')
        else:
            st.success('Inicializando o Chatbot...')
            create_conversation_chain()
            st.rerun()

config_page()