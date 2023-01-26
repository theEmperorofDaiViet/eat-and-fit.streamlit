import streamlit as st
import sqlalchemy
from models.fit import *

st.set_page_config(page_title='Eat & Fit', page_icon='images\logo.png')

# A workaround using st.markdown() to apply some style sheets to the page
st.markdown(
    f"""
        <style>
            /* Add a background to the page, but I don't use it here */
            # .stApp {{
            #     background: url("https://thumbs.dreamstime.com/b/healthy-clean-eating-layout-vegetarian-food-diet-nutrition-concept-various-fresh-vegetables-ingredients-salad-white-105567339.jpg");
            #     background-repeat: no-repeat;
            #     background-size: cover;
            # }}

            /* Make the default header of streamlit invisible */
            .css-18ni7ap.e8zbici2 {{
                opacity: 0
            }}

            /* Make the default footer of streamlit invisible */
            .css-h5rgaw.egzxvld1 {{
            opacity: 0
            }}

            /* Change width and padding of the page */
            .block-container.css-91z34k.egzxvld4 {{
            width: 100%;
            padding: 0.5rem 1rem 10rem;
            max-width: none;
            }}

            /* Change padding of the pages list in the sidebar */
            .css-uc76bn.e1fqkh3o9 {{
            padding-top: 2rem;
            padding-bottom: 0.25rem;
            }}
        </style>
        """, unsafe_allow_html=True
    )

# A workaround using st.columns() to move logo and title to the center of the page
col1, col2, col3, col4, col5, col6, col7, col8 = st.columns([0.5, 0.5, 1, 0.75, 1, 0.75, 0.5, 0.5])
with col4:
    st.image(image='images\logo.png', width=140)
with col5:
    st.markdown("""<br/><h1 style="display: inline;">Eat & Fit</h1>
                    <i style="font-size: 22px;">Weight-Loss Guide</i>
                """, unsafe_allow_html=True)

engine = sqlalchemy.create_engine("sqlite:///database/eatandfit.db")
with engine.connect() as conn:
    all_exercise_results = conn.execute("SELECT * FROM Exercise").fetchall()
exercise_keywords = ['',]
for e in all_exercise_results:
    exercise = Exercise(*e)
    exercise_keywords.append(exercise.name)

col1, col2, col3 = st.columns([0.4, 1.2, 0.4])
with col2:
    st.markdown(
        f"""
            <h1 style="text-align: center">Exercise Browser</h1>
        """, unsafe_allow_html=True
    )
    exercise_keyword = st.selectbox("**Search**", tuple(exercise_keywords))

if exercise_keyword != '':
    with engine.connect() as conn:
        exercise_result = conn.execute("SELECT * FROM Exercise WHERE Name = :name", {'name': exercise_keyword}).fetchone()
        exercise = Exercise(*exercise_result)
        st.markdown(
            f"""
                <h2 style="text-align: center">{exercise.name}</h2>
            """, unsafe_allow_html=True
        )

    col1, col2, col3 = st.columns([0.15, 1.7, 0.15])
    with col2:
        st.markdown(
            f"""
                <iframe width="100%" height="500px" allow="fullscreen;" src="{exercise.link}"></iframe>
            """, unsafe_allow_html=True
        )
        st.subheader("I. Overview")

        overview_builder = ''

        for p in exercise.get_overview_paragraph():
            overview_builder += f"<p style='padding-left: 22px'>{p}</p>"

        st.markdown(overview_builder, unsafe_allow_html=True)

        st.subheader("II. Instructions")

        instructions_builder = "<ul style='list-style-type: decimal; padding-left: 22px'>"

        for li in exercise.get_introductions_detail():
            instructions_builder += f"<li>{li}</li>"

        instructions_builder += "</ul>"

        st.markdown(instructions_builder, unsafe_allow_html=True)