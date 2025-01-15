from pathlib import Path
import streamlit as st
import os 


FILE_DIRECTORY = Path(__file__).parent / 'files'



def sidebar():
    uploaded_pdfs = st.file_uploader('Add pdf files', type=['.pdf'], accept_multiple_files=True)

    if not uploaded_pdfs is None:
        for file in FILE_DIRECTORY.glob('*.pdf'):
            file.unlink()
        for pdf in uploaded_pdfs:
            with open( FILE_DIRECTORY/pdf.name, 'wb') as f:
                f.write(pdf.read())

    

def main():
    if not FILE_DIRECTORY.exists():
        try:
            os.mkdir(FILE_DIRECTORY)
        except Exception as e:
            print(f'An error ocurred: {e}')

    with st.sidebar:
        sidebar()

if __name__ == '__main__':
    main()