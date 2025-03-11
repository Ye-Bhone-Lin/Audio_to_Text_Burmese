import streamlit as st
import re
import pandas as pd

df = pd.read_csv('Audio Database - Sheet1.csv')

user_input = st.text_input('Keywords')

def extract_sentences_and_links(df, keyword):
    matching_results = []
    
    for index, row in df.iterrows():
        text = row['Text']
        audio_link = row['Audio Link']
        
        sentences = re.split(r'(?<=[။])', text)  
        
        matches = [sentence.strip() for sentence in sentences if keyword in sentence]
        
        if matches:
            matching_results.append({'Sentences': matches, 'Audio Link': audio_link})
    
    return matching_results

results = extract_sentences_and_links(df, user_input)

if user_input:
    if results:
        for result in results:
            for sentence in result['Sentences']:
                st.write(f"Sentence: {sentence}")
            st.write(f"Audio Link: {result['Audio Link']}\n")
    else:
        st.write("No matching sentence found.")
