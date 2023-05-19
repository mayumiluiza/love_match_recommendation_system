import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


image_match = Image.open('match_image_okcupid.png')
st.image(image_match)

st.write("Now it's time to select your preferences regarding your match.")
st.write("Remember: everytime you choose something as a 'dealbreaker' the model restricts your answers.")

with st.form("match_form"):
    st.write("💕 Answer the questions below regarding what you are looking for in a match 💕")
    
    ## Match | Gender
    match_gender = st.multiselect("What's your gender preference? (I apologize in advance for the gender limitation of this recommendation model. Since we are using a fixed dataset, these are the only options available for the match)", ["m","f"],key="gender_match")
    st.session_state['sex'] = match_gender

    ## Match | Age
    match_age = st.select_slider('Slide to select the age of your match.', options=np.arange(18,81,1),value=(18,80), key="age_match")
    st.session_state['age'] = match_age

    ## Match | Status
    match_status = st.multiselect('What status you are looking for in your match?', ["single", "married or seeing someone", "unknown"], key="status_match")
    match_status_dealbreaker = st.radio('Is what you are looking for regarding status preference a dealbreaker?',["yes", "no"], key="status_choice_match")
    st.session_state['status'] = match_status
    st.session_state['status_dealbreaker'] = match_status_dealbreaker

    ## Match | Languages

    ## Match | Pets
    match_pets = st.radio('What opinion about pets you are looking for in your match?', ["likes dogs and likes cats","likes dogs","likes dogs and has cats","has dogs","has dogs and likes cats","likes dogs and dislikes cats","has dogs and has cats","has cats","likes cats","has dogs and dislikes cats","dislikes dogs and likes cats","dislikes dogs and dislikes cats","dislikes cats","dislikes dogs and has cats","dislikes dogs"], key="pets_match")
    match_pets_dealbreaker = st.radio('Is what you are looking for regarding pet preference a dealbreaker?',["yes", "no"], key="pets_choice_match")
    st.session_state['pets'] = match_pets
    st.session_state['pets_dealbreaker'] = match_pets_dealbreaker

    ## Match | Kids
    match_kids = st.radio("What opinion about kids you are looking for in your match?", ["doesn't have kids","doesn't have kids, but might want them","doesn't have kids, but wants them","doesn't want kids","has kids","has a kid","doesn't have kids, and doesn't want any","has kids, but doesn't want more","has a kid, but doesn't want more","has a kid, and might want more","wants kids","might want kids","has kids, and might want more","has a kid, and wants more","has kids, and wants more"
    ], key="kids_match")
    match_kids_dealbreaker = st.radio('Is what you are looking for regarding kids preference a dealbreaker?',["yes", "no"], key="kids_choice_match")
    st.session_state['kids'] = match_kids
    st.session_state['kids_dealbreaker'] = match_kids_dealbreaker

    ## Match | Diet
    match_diet =  st.radio("What type of diet would you like your match to follow?",["anything","vegetarian","other","vegan","kosher","halal"], key="diet_match")
    match_diet_dealbreaker = st.radio('Is what you are looking for regarding diet preference a dealbreaker?',["yes", "no"], key="diet_choice_match")
    st.session_state['diet'] = match_diet
    st.session_state['diet_dealbreaker'] = match_diet_dealbreaker

    ## Match | Drinks
    match_drinks = st.radio("What type of drinkings habits would you like your match to follow?", ["desperately","very often", "often", "socially", "rarely", "not at all"], key="drinks_match")
    match_drinks_dealbreaker = st.radio('Is what you are looking for regarding drinking preference a dealbreaker?',["yes", "no"], key="drinks_choice_match")
    st.session_state['drinks'] = match_drinks
    st.session_state['drinks_dealbreaker'] = match_drinks_dealbreaker

    ## Match | Smokes
    match_smoke = st.radio("Can your match smoke?", ["yes", "sometimes", "when drinking", "trying to quit", "no"], key="smoke_match")
    match_smoke_dealbreaker = st.radio('Is what you are looking for regarding smoking preference a dealbreaker?',["yes", "no"], key="smoke_choice_match")
    st.session_state['smokes'] = match_smoke
    st.session_state['smokes_dealbreaker'] = match_smoke_dealbreaker

    ## Match | Drugs
    match_drug = st.radio("Can you match use drugs?", ["often", "sometimes","never"], key="drug_match")
    match_drug_dealbreaker = st.radio('Is what you are looking for regarding drugs preference a dealbreaker?',["yes", "no"], key="drugs_choice_match")
    st.session_state['drugs'] = match_drug
    st.session_state['drugs_dealbreaker'] = match_drug_dealbreaker

    ## Match | Education
    match_education = st.multiselect("What's the highest level of education do you look for in your match?", ["Working on or Finished Bachelor Degree","Working on or Finished Graduate Degree (Masters, Law or Med School)","Working on or Finished High School","Working on or Finished ph.d Program","Working on or Finished Space Camp","Dropped out of High School or Space Camp"], key="education_match")
    match_education_dealbreaker = st.radio('Is what you are looking for regarding education preference a dealbreaker?',["yes", "no"], key="education_choice_match")
    st.session_state['education'] = match_education
    st.session_state['education_dealbreaker'] = match_education_dealbreaker

    ## Match | Job
    match_job = st.multiselect("What's the dream working area do you picture for your match?", ["student", "art/music/writing", "banking/finance", "administration", "technology", "construction", "education", "entertainment/media", "management", "hospitality", "law", "medicine", "military", "politics/government", "sales/marketing", "science/engineering", "transportation", "unemployed", "other", "rather not say", "retire"], key="job_match")
    match_job_dealbreaker = st.radio('Is what you are looking for regarding job preference a dealbreaker?',["yes", "no"], key="job_choice_match")
    st.session_state['job'] = match_job
    st.session_state['job_dealbreaker'] = match_job_dealbreaker

    ## Match | Income
    match_income = individual_income = st.multiselect("What' the dream income do you picture for your match?? (US$ -1 means rather not say)",[-1, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 100000, 150000, 250000, 500000, 1000000], key="income_match")
    match_income_dealbreaker = st.radio('Is what you are looking for regarding income preference a dealbreaker?',["yes", "no"], key="income_choice_match")
    st.session_state['income'] = match_income
    st.session_state['income_dealbreaker'] = match_income_dealbreaker

    ## Match | Religion
    match_religion = individual_religion = st.radio("What's the religion of you ideal match?", ["atheist or agnostic","buddhism serious","buddhism not serious","christianity serious","christianity not serious","catholicism serious","catholicism not serious","hinduism not serious","hinduism serious","islam serious","islam not serious","judaism serious","judaism not serious","other"], key="religion_match")
    match_religion_dealbreaker = st.radio('Is what you are looking for regarding religion preference a dealbreaker?',["yes", "no"], key="religion_choice_match")
    st.session_state['religion'] = match_religion
    st.session_state['religion_dealbreaker'] = match_religion_dealbreaker

    # Submit button
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.write("Thank you for answering 🥰. Now you can move on to the Matched Profile page")

        match_profile_dict = {'sex': str(match_gender), 'age': str(match_age), 'status': str(match_status), 'pets': match_pets, 'kids': match_kids, 'drinks': match_drinks, 'smokes': match_smoke, 'drugs': match_drug, 'education':str(match_education), 'job': str(match_job), 'income': str(match_income), 'religion': match_religion}

        #df = pd.DataFrame(columns=['sex', 'orientation','age', 'status', 'pets', 'kids', 'drinks', 'smokes', 'drugs', 'education', 'job', 'income', 'religion'])
        #df.to_csv("match_profile_df.csv", index=False)

        match_profile_df = pd.read_csv("match_profile_df.csv")
        df_extended = pd.DataFrame(match_profile_dict, index=[len(match_profile_df)])
        st.write(df_extended)

        combined_df = pd.concat([match_profile_df, df_extended])

        combined_df.to_csv(f"data/match_profile_df_{st.session_state['individual_id']}.csv", index=False)