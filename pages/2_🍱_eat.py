import streamlit as st
import sqlalchemy
from models.eat import *
import base64
import matplotlib
import matplotlib.pyplot as plt

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
    all_dish_results = conn.execute("SELECT * FROM Dish").fetchall()
dish_keywords = ['',]
for d in all_dish_results:
    dish = Dish(*d)
    dish_keywords.append(dish.name)

col1, col2, col3 = st.columns([0.4, 1.2, 0.4])
with col2:
    st.markdown(
        f"""
            <h1 style="text-align: center">Food & Recipe Browser</h1>
        """, unsafe_allow_html=True
    )
    dish_keyword = st.selectbox("**Search**", tuple(dish_keywords))

if dish_keyword != '':
    with engine.connect() as conn:
        dish_result = conn.execute("SELECT * FROM Dish WHERE Name = :name", {'name': dish_keyword}).fetchone()
        dish = Dish(*dish_result)
        st.markdown(
            f"""
                <h2 style="text-align: center">{dish.name}</h2>
            """, unsafe_allow_html=True
        )
        col1, col2, col3 = st.columns([1.3, 0.55, 0.15])
        with col1:
            st.markdown(
                f"""
                <p style="text-align: right">
                    <img src="data:image/jpeg;base64,{base64.b64encode(dish.image).decode('utf-8')}" width="90%">
                </p>
                """, unsafe_allow_html=True
            )
        with col2:
            st.markdown(
                f"""
                    <table style="width:100%">
                        <tr>
                            <th style="font-size: 22px;">Nutrition</th>
                        </tr>
                        <tr>
                            <td>
                                <b>Calories:</b>
                                <text style="float:right">{round(dish.get_nutrition_detail().calories)} cal</text><br/>
                                <b>Carbs:</b>
                                <text style="float:right">{dish.get_nutrition_detail().carbs} g</text><br/>
                                <b>Fat:</b>
                                <text style="float:right">{dish.get_nutrition_detail().fat} g</text><br/>
                                <b>Protein:</b>
                                <text style="float:right">{dish.get_nutrition_detail().protein} g</text><br/>
                            </td>
                        </tr>
                    </table>
                    <br/>
                    <div class="figure_title" style="text-align:center; font-size:20px"><b>Percent Calories From:</b></div>
                """, unsafe_allow_html=True
            )  
            matplotlib.rcParams.update({'font.size': 5})
            label = ['Carbs', 'Fat', 'Protein']
            colors = ['#F7D300', '#38BC56' ,'#D35454']            
            nutrition_detail = dish.get_nutrition_detail()
            data = [nutrition_detail.get_carbs_percentage(), nutrition_detail.get_fat_percentage(), nutrition_detail.get_protein_percentage()]
            fig, ax = plt.subplots(figsize=(1, 1))
            ax.pie(data, labels=label, colors=colors, explode=(0.15, 0.075, 0.075), autopct='%1.1f%%', startangle=90,
                            wedgeprops= {"edgecolor":"black",
                            'linewidth': 1,
                            'antialiased': True})
            ax.axis('equal')
            st.pyplot(fig)

        col1, col2, col3, col4 = st.columns([0.122, 0.45, 1.278, 0.15])
        with col2:
            recipe_table_builder =  '''<table style="width: 100%;">
                                    <tr>
                                        <th style="font-size: 22px;">Recipe</th>
                                    </tr>
                                    <tr><td>'''
            for ingredient, amount in dish.get_recipe_detail().ingredients.items():
                recipe_table_builder += f'<b>{ingredient}:</b><text style="float:right">{amount}</text><br/>'
            recipe_table_builder += '</td></tr></table>'

            st.markdown(recipe_table_builder, unsafe_allow_html=True)

        with col3:
            steps_table_builder =  '''<table style="width: 100%;">
                                    <tr>
                                        <th colspan="2" style="font-size: 22px;">Steps to cook</th>
                                    </tr>'''
            for step, detail in dish.get_steps_detail().steps.items():
                steps_table_builder += f'<tr><td style="width: 80px; vertical-align: top"><b>{step}</b></td><td>{detail}</td></tr>'
            steps_table_builder += '</table>'

            st.markdown(steps_table_builder, unsafe_allow_html=True)            