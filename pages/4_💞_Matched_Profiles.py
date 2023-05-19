import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from love_recommendation_system import dataset_recommendation, dataset_filter, grouping_categories, columns_enconder
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import pairwise_distances
import secrets
import string

image_matching = Image.open('matchingtime_image_okcupid.png')
st.image(image_matching)

st.write("Now it's time to select the profiles.")


# Get the dataset
#ok_cupid = pd.read_csv("okcupid_profiles 2.csv")
#ok_cupid_clean = grouping_categories(ok_cupid)
#ok_cupid_clean.to_csv("ok_cupid_clean.csv", index=False)

ok_cupid_clean = pd.read_csv("ok_cupid_clean.csv")

# Organizing preferences
filters = []
recommendations = {}

## Match | Sexual Orientation
if len(st.session_state['sex'])>1:
    match_sexual_orientation = "bisexual"
else: 
    if (st.session_state["individual_gender_binary"]=="m" and "m" in st.session_state['sex']) or (st.session_state["individual_gender_binary"]=="f" and "f" in st.session_state['sex']):
        match_sexual_orientation = "gay"
    elif (st.session_state["individual_gender_binary"]=="m" and "f" in st.session_state['sex']) or (st.session_state["individual_gender_binary"]=="f" and "m" in st.session_state['sex']):
        match_sexual_orientation = "straight"
st.session_state['orientation'] = match_sexual_orientation
    
## sex_orientation
if len(st.session_state['sex'])==1:
    if st.session_state["individual_gender_binary"]=="m" and st.session_state['sex'][0]=="m":
        filters.append({'column': 'sex', 'value': 'm'})
        filters.append({'column': 'orientation', 'value': ['gay','bisexual']}) 
    elif st.session_state["individual_gender_binary"]=="f" and st.session_state['sex'][0]=="f":
        filters.append({'column': 'sex', 'value': 'f'})
        filters.append({'column': 'orientation', 'value': ['gay','bisexual']})  
    elif st.session_state["individual_gender_binary"]=="m" and st.session_state['sex'][0]=="f":
        filters.append({'column': 'sex', 'value': 'f'})
        filters.append({'column': 'orientation', 'value': ['straight','bisexual']})
    else:
        filters.append({'column': 'sex', 'value': 'm'})
        filters.append({'column': 'orientation', 'value': ['straight','bisexual']})
else:
    if st.session_state["individual_gender_binary"]=="f":
        filters.append({'column': 'to_exclude', 'value': "(sex=='m' and orientation=='straight' or orientation=='bisexual') or (sex=='f' and orientation=='gay' or orientation=='bisexual')"})
    else:
        filters.append({'column': 'to_exclude', 'value': "(sex=='m' and orientation=='gay' or orientation=='bisexual') or (sex=='f' and orientation=='straight' or orientation=='bisexual')"})

## age
filters.append({'column': 'age', 'value':[int(st.session_state['age'][0]),int(st.session_state['age'][1])]})

#status
if st.session_state['status_dealbreaker'] == "yes":
    filters.append({'column': 'status', 'value': st.session_state['status']})
else:
    recommendations['status'] = st.session_state['status']

#pets
if st.session_state['pets_dealbreaker'] == "yes":
    filters.append({'column': 'pets', 'value': st.session_state['pets']})
else:
    recommendations['pets'] = st.session_state['pets']

#kids
if st.session_state['kids_dealbreaker'] == "yes":
    filters.append({'column': 'kids', 'value': st.session_state['kids']})
else:
    recommendations['kids'] = st.session_state['kids']

#diet
if st.session_state['diet_dealbreaker'] == "yes":
    filters.append({'column': 'diet', 'value': st.session_state['diet']})
else:
    recommendations['diet'] = st.session_state['diet']

#drinks
if st.session_state['drinks_dealbreaker'] == "yes":
    filters.append({'column': 'drinks', 'value': st.session_state['drinks']})
else:
    recommendations['drinks'] = st.session_state['drinks']

#smokes
if st.session_state['smokes_dealbreaker'] == "yes":
    filters.append({'column': 'smokes', 'value': st.session_state['smokes']})
else:
    recommendations['smokes'] = st.session_state['smokes']

#drugs
if st.session_state['drugs_dealbreaker'] == "yes":
    filters.append({'column': 'drugs', 'value': st.session_state['drugs']})
else:
    recommendations['drugs'] = st.session_state['drugs']

#education
if st.session_state['education_dealbreaker'] == "yes":
    filters.append({'column': 'education', 'value': st.session_state['education']})
else:
    recommendations['education'] = st.session_state['education']

## Match | Job
if st.session_state['job_dealbreaker'] == "yes":
    filters.append({'column': 'job', 'value': st.session_state['job']})
else:
    recommendations['job'] = st.session_state['job']

## Match | Income
if st.session_state['income_dealbreaker'] == "yes":
    filters.append({'column': 'income', 'value': st.session_state['income']})
else:
    recommendations['income'] = st.session_state['income']

## Match | Religion
if st.session_state['religion_dealbreaker'] == "yes":
    filters.append({'column': 'religion', 'value': st.session_state['religion']})
else:
    recommendations['religion'] = st.session_state['religion']

# Filter e Recommendation
recommendations_dummy = columns_enconder(recommendations)

order_recommendations = dataset_recommendation(ok_cupid_clean, filters, recommendations_dummy,columns=recommendations.keys())
order_recommendations_intermediate = ok_cupid_clean.loc[order_recommendations.index].head()
order_recommendations_intermediate['Like/Dislike Match'] = False

opinion = st.experimental_data_editor(order_recommendations_intermediate)

order_recommendations["Like/Dislike Match"] = opinion['Like/Dislike Match']

button = st.button("Submit")

if button:
    order_recommendations.to_csv(f"data/recommendatio_evaluation_{st.session_state['individual_id']}.csv", index=True)
    st.balloons()





