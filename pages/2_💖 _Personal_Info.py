import streamlit as st
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
from love_recommendation_system import zodiadic_sign
from PIL import Image
import secrets
import string


image_personal = Image.open('personal_image_okcupid.png')
st.image(image_personal)

st.write("To start building our model. We need to know a little bit about yourself.")

st.write("The information you provide is only used to train this matchmaker recommendation model. Your responses will be kept private, secure and annonymous. The information will not be used for a discriminatory purpose.")

id = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(7))
st.session_state['individual_id'] = id

with st.form("personal_form"):
    st.write("❣️ Answer the questions below ❣️")
   ## Individual | Gender
    individual_gender = st.selectbox('Which of the following most accurately describe(s) yourself?', [
    "agender","androgy","demigen","genderqueen or gender fluid","intersex","man", "questioning or unsure", "trans man","trans woman","woman","prefer not to disclose", "additional gender category/identity"], key="gender_individual")
    if individual_gender == "additional gender category/identity":
        gender_other = st.text_input('Please specify: ', key="gender2_individual")

    ## Individual | Gender_Dataset
    individual_gender_binary = st.selectbox('However, if you had to choose between a binary genre. What would you choose? (I apologize in advance for the gender limitation of this recommendation model. Since we are using a fixed dataset, these are the only options available for the match)', ["m","f"], key="binary_gender")
    st.session_state['individual_gender_binary'] = individual_gender_binary

    ## Individual | Birthday
    min_value = datetime.date.today() - datetime.timedelta(weeks=5200)
    max_value = datetime.date.today() - datetime.timedelta(weeks=940)
    individual_birthday = st.date_input("What's your date of birth?", min_value = min_value, max_value=max_value, value=max_value, key="birthday_individual")
    individual_day = individual_birthday.day
    individual_month = individual_birthday.month

    ## Individual | Zodiadic Sign
    individual_zodiac = zodiadic_sign(individual_day, individual_month)

    ## Individual | Age
    individual_age = relativedelta(datetime.date.today(), individual_birthday).years

    ## Individual | Status
    individual_status = st.radio("What's your current status?", ["single", "seeing someone or married", "unknown"], key="status_individual")

    ## Individual | Languages

    ## Individual | Pets
    individual_pets = st.radio("How do you feel about pets?", ["likes dogs and likes cats","likes dogs","likes dogs and has cats","has dogs","has dogs and likes cats","likes dogs and dislikes cats","has dogs and has cats","has cats","likes cats","has dogs and dislikes cats","dislikes dogs and likes cats","dislikes dogs and dislikes cats","dislikes cats","dislikes dogs and has cats","dislikes dogs"], key="pets_individual")

    ## Individual | Kids
    individual_kids = st.radio("How do you feel about kids?", ["doesn't have kids","doesn't have kids, but might want them","doesn't have kids, but wants them","doesn't want kids","has kids","has a kid","doesn't have kids, and doesn't want any","has kids, but doesn't want more","has a kid, but doesn't want more","has a kid, and might want more","wants kids","might want kids","has kids, and might want more","has a kid, and wants more","has kids, and wants more"
    ], key="kids_individual")

    ## Individual | Diet
    individual_diet = st.radio("What's your diet?", ["anything","vegetarian","other","vegan","kosher","halal"], key="diet_individual")

    ## Individual | Drinks
    individual_drinks = st.radio("How often do you like to drink", ["desperately","very often", "often", "socially", "rarely", "not at all"], key="drinks_individual")

    ## Individual | Smokes
    individual_smokes = st.radio("Do you smoke?", ["yes", "sometimes", "when drinking", "trying to quit", "no"], key="smokes_individual")

    ## Individual | Drugs
    individual_drugs = st.radio("Do you like to use drugs", ["often", "sometimes","never"], key="drugs_individual")

    ## Individual | Education
    individual_education = st.radio("What's your highest level of education?", ["Working on or Finished Bachelor Degree","Working on or Finished Graduate Degree (Masters, Law or Med School)","Working on or Finished High School","Working on or Finished ph.d Program","Working on or Finished Space Camp","Dropped out of High School or Space Camp"
    ], key="education_individual")

    ## Individual | Job
    individual_job = st.radio("What's the area of your work?", ["student", "art/music/writing", "banking/finance", "administration", "technology", "construction", "education", "entertainment/media", "management", "hospitality", "law", "medicine", "military", "politics/government", "sales/marketing", "science/engineering", "transportation", "unemployed", "other", "rather not say", "retire"
    ], key="job_individual")

    ## Individual | Income
    individual_income = st.radio("What's your income? (US$ -1 means rather not say)",[-1, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 100000, 150000, 250000, 500000, 1000000], key="income_individual")

    ## Individual | Religion
    individual_religion = st.radio("What's your religion?", ["atheist or agnostic","buddhism serious","buddhism not serious","christianity serious","christianity not serious","catholicism serious","catholicism not serious","hinduism not serious","hinduism serious","islam serious","islam not serious","judaism serious","judaism not serious","other"], key="religion_individual")
    
    # Submit button
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.write("Thank you for answering 🥰. Now you can move on to the 'Match Info' page")

        individual_profile_dic = {'Gender': individual_gender, 'Binary Gender': individual_gender_binary, 'Birthday': individual_birthday, 'Age': individual_age, 'Zodiac Sign': individual_zodiac, 'Status': individual_status, 'Pets': individual_pets, 'Kids': individual_kids, 'Drinks': individual_drinks, 'Smoke': individual_smokes, 'Drugs': individual_drugs, 'Education': individual_education, 'Job': individual_job, 'Income': individual_income, 'Religion': individual_religion}
        individual_profile_df = pd.read_csv("individual_profile_df.csv")

        df_extended = pd.DataFrame(individual_profile_dic, index=[len(individual_profile_df)])

        combined_df = pd.concat([individual_profile_df, df_extended])

        st.session_state['individual_profile'] = df_extended

        combined_df.to_csv(f"data/individual_profile_df_{id}.csv", index=False)



