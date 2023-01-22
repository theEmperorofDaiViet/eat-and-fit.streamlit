import streamlit as st
from algorithm.fuzzy_logic import FuzzyLogic
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
            .css-wjbhl0, .css-hied5v {{
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

# A flag to show whether the page is loaded the first time or not
is_first_load = True

# Input fields in the sidebar
with st.sidebar:
    st.title("Body Parameters")

    # A workaround using st.session_state and callback to keep input value during navigating through other pages
    if "page1" not in st.session_state:
        st.session_state.page1 = {'is_first_load': True, 'sex': 0, 'height': 175.0, 'weight': 80.0, 'stage': 0}

    for k, v in st.session_state.items():
        st.session_state[k] = v

    def submit_sex():
        if st.session_state.sex_input_value == 'Male':
            i = 0
        elif st.session_state.sex_input_value == 'Female':
            i = 1
        st.session_state.page1['sex'] = i

    def submit_height():
        st.session_state.page1['height'] = st.session_state.height_input_value

    def submit_weight():
        st.session_state.page1['weight'] = st.session_state.weight_input_value

    def submit_stage():
        if st.session_state.stage_input_value == "Yes, I'm a beginner":
            st.session_state.page1['stage'] = 0
        elif st.session_state.stage_input_value == "No, I'm an intermediate":
            st.session_state.page1['stage'] = 1

    sex_input = st.radio("**What's your sex?**", ('Male', 'Female'), key='sex_input_value', index=st.session_state.page1['sex'], on_change=submit_sex)

    height_input = st.number_input("**What's your height (in centimeters)?**", key='height_input_value', min_value=130.0, max_value=220.0, step=0.1, value=st.session_state.page1['height'], on_change=submit_height)

    weight_input = st.number_input("**What's your weight (in kilograms)?**", key='weight_input_value', min_value=30.0, max_value=150.0, step=0.1, value=st.session_state.page1['weight'], on_change=submit_weight)

    stage_input = st.selectbox("**Are you new to weight loss?**", ("Yes, I'm a beginner", "No, I'm an intermediate"), key='stage_input_value', index=st.session_state.page1['stage'], on_change=submit_stage)

    # Align the buttons in the sidebar
    col1, col2, col3 = st.columns([1, 0.5, 0.85])
    with col1:
        if st.button("Submit"):
            st.session_state.page1['is_first_load'] = False
    with col3:
        if st.button("Reset"):
            st.session_state.page1['is_first_load'] = True    

if not st.session_state.page1['is_first_load']:
    # Perform Fuzzy Logic to determine the body state
    fuzzy_logic = FuzzyLogic()
    fuzzy_logic.do_fuzzification_of_height(round(st.session_state.page1['height'], 2), st.session_state.page1['sex'])
    fuzzy_logic.do_fuzzification_of_weight(round(st.session_state.page1['weight'], 2), st.session_state.page1['sex'])
    fuzzy_logic.do_fuzzy_inference()
    body = fuzzy_logic.do_defuzzification_of_body()

    # Conclusion
    body_result = ''
    match body:
        case 2:
            body_result = 'overweight'
        case 3:
            body_result = 'pre-obese'
        case 4:
            body_result = 'obese'

    if body == 0:
        st.subheader("You are thin! You should gain weight instead of losing weight!")
    elif body == 1:
        st.subheader("You are in shape! Keep going! :sunglasses:")
    else:
        st.subheader(f"You are {body_result}! To lose weight, you can follow this guide:")

        # Diet plan overview
        st.subheader("A. Diet")
        st.write('**Carbohydrates** or ***carbs*** (including *sugars*, *starch*, and *cellulose*) are the main energy source of the human diet. To lose weight, you need to eat fewer carbs.')
        st.markdown(
            """
            In this diet plan, each week will consist of 3 different types of eating days:
            <ul style="padding-left: 2rem">
            <li><b>Low Carb Days</b> (below <b>26%</b> of total energy intake) - <b>3</b> days per week</li>
            <li><b>Moderate Carb Days</b> (between <b>26%</b> and <b>45%</b> of total energy intake) - <b>3</b> days per week</li>
            <li><b>High Carb Days</b> (above <b>45%</b> of total energy intake) - <b>1</b> day per week</li>
            </ul>
            """, unsafe_allow_html=True
        )
        # Get and display diet plan from the database
        low_carb_1, moderate_carb_1, high_carb_1 = st.columns(3)
        low_carb_2, moderate_carb_2, high_carb_2 = st.columns(3)
        matplotlib.rcParams.update({'font.size': 5})
        label = ['Carbs', 'Fat', 'Protein']
        colors = ['#F7D300', '#38BC56' ,'#D35454']
        engine = sqlalchemy.create_engine("sqlite:///database/eatandfit.db")
        with engine.connect() as conn:
            # Get standard calories each day for the user
            sc_result = conn.execute("SELECT * FROM StandardCalories WHERE Stage = :stage AND Body = :body AND Sex = :sex", 
                                                                                    {'stage': st.session_state.page1['stage'], 'body': body, 'sex': st.session_state.page1['sex']}, ).fetchone()
            standard_calories = StandardCalories(*sc_result)

            # Get low carb diet  
            lc_result = conn.execute("SELECT * FROM LowCarb WHERE Calories = :calories", 
                                                                    {'calories': standard_calories.low_carb}, ).fetchone()
            low_carb_diet = Diet(*lc_result)           

            low_carb_nutrition_detail = low_carb_diet.get_nutrition_detail()

            low_carb_data = [low_carb_nutrition_detail.get_carbs_percentage(), low_carb_nutrition_detail.get_fat_percentage(), low_carb_nutrition_detail.get_protein_percentage()]
            low_carb_fig, low_carb_ax = plt.subplots(figsize=(1, 1))
            low_carb_ax.pie(low_carb_data, labels=label, colors=colors, explode=(0.15, 0.075, 0.075), autopct='%1.1f%%', startangle=90,
                            wedgeprops= {"edgecolor":"black",
                            'linewidth': 1,
                            'antialiased': True})
            low_carb_ax.axis('equal')

            low_carb_breakfast_detail = low_carb_diet.get_breakfast_detail()
            low_carb_lunch_detail = low_carb_diet.get_lunch_detail()
            low_carb_dinner_detail = low_carb_diet.get_dinner_detail()

            lcb1_result = conn.execute("SELECT * FROM Dish WHERE Id = :id",
                                                            {'id': low_carb_breakfast_detail.id1}, ).fetchone()
            lcb2_result = conn.execute("SELECT * FROM Dish WHERE Id = :id",
                                                            {'id': low_carb_breakfast_detail.id2}, ).fetchone()
            lcl1_result = conn.execute("SELECT * FROM Dish WHERE Id = :id",
                                                            {'id': low_carb_lunch_detail.id1}, ).fetchone()
            lcl2_result = conn.execute("SELECT * FROM Dish WHERE Id = :id",
                                                            {'id': low_carb_lunch_detail.id2}, ).fetchone()
            lcd1_result = conn.execute("SELECT * FROM Dish WHERE Id = :id",
                                                            {'id': low_carb_dinner_detail.id1}, ).fetchone()
            lcd2_result = conn.execute("SELECT * FROM Dish WHERE Id = :id",
                                                            {'id': low_carb_dinner_detail.id2}, ).fetchone()
            
            low_carb_breakfast_1 = Dish(*lcb1_result)
            low_carb_breakfast_2 = Dish(*lcb2_result)
            low_carb_lunch_1 = Dish(*lcl1_result)
            low_carb_lunch_2 = Dish(*lcl2_result)
            low_carb_dinner_1 = Dish(*lcd1_result)
            low_carb_dinner_2 = Dish(*lcd2_result)

            with low_carb_1:
                st.markdown(
                    f"""
                        <h3 style="text-align: center">Low Carb Diet</h3>
                        <table style="width:100%">
                            <tr>
                                <th style="font-size:18px;">Nutrition</th>
                            </tr>
                            <tr>
                                <td>
                                    <b>Calories:</b>
                                    <text style="float:right">{round(low_carb_nutrition_detail.calories)} cal</text><br/>
                                    <b>Carbs:</b>
                                    <text style="float:right">{low_carb_nutrition_detail.carbs} g</text><br/>
                                    <b>Fat:</b>
                                    <text style="float:right">{low_carb_nutrition_detail.fat} g</text><br/>
                                    <b>Protein:</b>
                                    <text style="float:right">{low_carb_nutrition_detail.protein} g</text><br/>
                                </td>
                            </tr>
                        </table>
                        <br/>
                        <div class="figure_title" style="text-align:center; font-size:20px"><b>Percent Calories From:</b></div>
                    """, unsafe_allow_html=True
                )
                st.pyplot(low_carb_fig)
            with low_carb_2:
                st.markdown(
                    f"""
                        <table style="white-space:nowrap; width:100%;">
                            <tr>
                                <td colspan="2"><b style="font-size:18px;">Breakfast</b><text style="float:right">{low_carb_breakfast_detail.calories} calories</text></td>
                            </tr>                            
                            <tr>
                                <td style="width: auto;"><img src="data:image/jpeg;base64,{base64.b64encode(low_carb_breakfast_1.image).decode('utf-8')}" width="70"></td>
                                <td><b>{low_carb_breakfast_1.name}</b><br/>
                                {low_carb_breakfast_detail.amount1} &nbsp; serving</td>
                            </tr>
                            <tr>
                                <td style="width: auto;"><img src="data:image/jpeg;base64,{base64.b64encode(low_carb_breakfast_2.image).decode('utf-8')}" width="70"></td>
                                <td><b>{low_carb_breakfast_2.name}</b><br/>
                                {low_carb_breakfast_detail.amount2} &nbsp; serving</td>
                            </tr>
                            <tr>
                                <td colspan="2"><b style="font-size:18px;">Lunch</b><text style="float:right">{low_carb_lunch_detail.calories} calories</text></td>
                            </tr>
                            <tr>
                                <td style="width: auto;"><img src="data:image/jpeg;base64,{base64.b64encode(low_carb_lunch_1.image).decode('utf-8')}" width="70"></td>
                                <td><b>{low_carb_lunch_1.name}</b><br/>
                                {low_carb_lunch_detail.amount1} &nbsp; serving</td>
                            </tr>
                            <tr>
                                <td style="width: auto;"><img src="data:image/jpeg;base64,{base64.b64encode(low_carb_lunch_2.image).decode('utf-8')}" width="70"></td>
                                <td><b>{low_carb_lunch_2.name}</b><br/>
                                {low_carb_lunch_detail.amount2} &nbsp; serving</td>
                            </tr>
                            <tr>
                                <td colspan="2"><b style="font-size:18px;">Dinner</b><text style="float:right">{low_carb_dinner_detail.calories} calories</text></td>
                            </tr>
                            <tr>
                                <td style="width: auto;"><img src="data:image/jpeg;base64,{base64.b64encode(low_carb_dinner_1.image).decode('utf-8')}" width="70"></td>
                                <td><b>{low_carb_dinner_1.name}</b><br/>
                                {low_carb_dinner_detail.amount1} &nbsp; serving</td>
                            </tr>
                            <tr>
                                <td style="width: auto;"><img src="data:image/jpeg;base64,{base64.b64encode(low_carb_dinner_2.image).decode('utf-8')}" width="70"></td>
                                <td><b>{low_carb_dinner_2.name}</b><br/>
                                {low_carb_dinner_detail.amount2} &nbsp; serving</td>
                            </tr>
                        </table><br/> 
                    """, unsafe_allow_html=True
                )

            # Get moderate carb diet
            lc_result = conn.execute("SELECT * FROM ModerateCarb WHERE Calories = :calories", 
                                                                    {'calories': standard_calories.moderate_carb}, ).fetchone()
            moderate_carb_diet = Diet(*lc_result)           

            moderate_carb_nutrition_detail = moderate_carb_diet.get_nutrition_detail()

            moderate_carb_data = [moderate_carb_nutrition_detail.get_carbs_percentage(), moderate_carb_nutrition_detail.get_fat_percentage(), moderate_carb_nutrition_detail.get_protein_percentage()]
            moderate_carb_fig, moderate_carb_ax = plt.subplots(figsize=(1, 1))
            moderate_carb_ax.pie(moderate_carb_data, labels=label, colors=colors, explode=(0.15, 0.075, 0.075), autopct='%1.1f%%', startangle=90,
                            wedgeprops= {"edgecolor":"black",
                            'linewidth': 1,
                            'antialiased': True})
            moderate_carb_ax.axis('equal')

            moderate_carb_breakfast_detail = moderate_carb_diet.get_breakfast_detail()
            moderate_carb_lunch_detail = moderate_carb_diet.get_lunch_detail()
            moderate_carb_dinner_detail = moderate_carb_diet.get_dinner_detail()

            lcb1_result = conn.execute("SELECT * FROM Dish WHERE Id = :id",
                                                            {'id': moderate_carb_breakfast_detail.id1}, ).fetchone()
            lcb2_result = conn.execute("SELECT * FROM Dish WHERE Id = :id",
                                                            {'id': moderate_carb_breakfast_detail.id2}, ).fetchone()
            lcl1_result = conn.execute("SELECT * FROM Dish WHERE Id = :id",
                                                            {'id': moderate_carb_lunch_detail.id1}, ).fetchone()
            lcl2_result = conn.execute("SELECT * FROM Dish WHERE Id = :id",
                                                            {'id': moderate_carb_lunch_detail.id2}, ).fetchone()
            lcd1_result = conn.execute("SELECT * FROM Dish WHERE Id = :id",
                                                            {'id': moderate_carb_dinner_detail.id1}, ).fetchone()
            lcd2_result = conn.execute("SELECT * FROM Dish WHERE Id = :id",
                                                            {'id': moderate_carb_dinner_detail.id2}, ).fetchone()
            
            moderate_carb_breakfast_1 = Dish(*lcb1_result)
            moderate_carb_breakfast_2 = Dish(*lcb2_result)
            moderate_carb_lunch_1 = Dish(*lcl1_result)
            moderate_carb_lunch_2 = Dish(*lcl2_result)
            moderate_carb_dinner_1 = Dish(*lcd1_result)
            moderate_carb_dinner_2 = Dish(*lcd2_result)

            with moderate_carb_1:
                st.markdown(
                    f"""
                        <h3 style="text-align: center">Moderate Carb Diet</h3>
                        <table style="width:100%">
                            <tr>
                                <th style="font-size:18px;">Nutrition</th>
                            </tr>
                            <tr>
                                <td>
                                    <b>Calories:</b>
                                    <text style="float:right">{round(moderate_carb_nutrition_detail.calories)} cal</text><br/>
                                    <b>Carbs:</b>
                                    <text style="float:right">{moderate_carb_nutrition_detail.carbs} g</text><br/>
                                    <b>Fat:</b>
                                    <text style="float:right">{moderate_carb_nutrition_detail.fat} g</text><br/>
                                    <b>Protein:</b>
                                    <text style="float:right">{moderate_carb_nutrition_detail.protein} g</text><br/>
                                </td>
                            </tr>
                        </table>
                        <br/>
                        <div class="figure_title" style="text-align:center; font-size:20px"><b>Percent Calories From:</b></div>
                    """, unsafe_allow_html=True
                )
                st.pyplot(moderate_carb_fig)
            with moderate_carb_2:
                st.markdown(
                    f"""
                        <table style="white-space:nowrap; width:100%;">
                            <tr>
                                <td colspan="2"><b style="font-size:18px;">Breakfast</b><text style="float:right">{moderate_carb_breakfast_detail.calories} calories</text></td>
                            </tr>                            
                            <tr>
                                <td style="width: auto;"><img src="data:image/jpeg;base64,{base64.b64encode(moderate_carb_breakfast_1.image).decode('utf-8')}" width="70"></td>
                                <td><b>{moderate_carb_breakfast_1.name}</b><br/>
                                {moderate_carb_breakfast_detail.amount1} &nbsp; serving</td>
                            </tr>
                            <tr>
                                <td style="width: auto;"><img src="data:image/jpeg;base64,{base64.b64encode(moderate_carb_breakfast_2.image).decode('utf-8')}" width="70"></td>
                                <td><b>{moderate_carb_breakfast_2.name}</b><br/>
                                {moderate_carb_breakfast_detail.amount2} &nbsp; serving</td>
                            </tr>
                            <tr>
                                <td colspan="2"><b style="font-size:18px;">Lunch</b><text style="float:right">{moderate_carb_lunch_detail.calories} calories</text></td>
                            </tr>
                            <tr>
                                <td style="width: auto;"><img src="data:image/jpeg;base64,{base64.b64encode(moderate_carb_lunch_1.image).decode('utf-8')}" width="70"></td>
                                <td><b>{moderate_carb_lunch_1.name}</b><br/>
                                {moderate_carb_lunch_detail.amount1} &nbsp; serving</td>
                            </tr>
                            <tr>
                                <td style="width: auto;"><img src="data:image/jpeg;base64,{base64.b64encode(moderate_carb_lunch_2.image).decode('utf-8')}" width="70"></td>
                                <td><b>{moderate_carb_lunch_2.name}</b><br/>
                                {moderate_carb_lunch_detail.amount2} &nbsp; serving</td>
                            </tr>
                            <tr>
                                <td colspan="2"><b style="font-size:18px;">Dinner</b><text style="float:right">{moderate_carb_dinner_detail.calories} calories</text></td>
                            </tr>
                            <tr>
                                <td style="width: auto;"><img src="data:image/jpeg;base64,{base64.b64encode(moderate_carb_dinner_1.image).decode('utf-8')}" width="70"></td>
                                <td><b>{moderate_carb_dinner_1.name}</b><br/>
                                {moderate_carb_dinner_detail.amount1} &nbsp; serving</td>
                            </tr>
                            <tr>
                                <td style="width: auto;"><img src="data:image/jpeg;base64,{base64.b64encode(moderate_carb_dinner_2.image).decode('utf-8')}" width="70"></td>
                                <td><b>{moderate_carb_dinner_2.name}</b><br/>
                                {moderate_carb_dinner_detail.amount2} &nbsp; serving</td>
                            </tr>
                        </table><br/> 
                    """, unsafe_allow_html=True
                )

            # Get high carb diet
            hc_result = conn.execute("SELECT * FROM HighCarb WHERE Calories = :calories", 
                                                                    {'calories': standard_calories.high_carb}, ).fetchone()
            high_carb_diet = Diet(*hc_result)

            high_carb_nutrition_detail = high_carb_diet.get_nutrition_detail()

            high_carb_data = [high_carb_nutrition_detail.get_carbs_percentage(), high_carb_nutrition_detail.get_fat_percentage(), high_carb_nutrition_detail.get_protein_percentage()]
            high_carb_fig, high_carb_ax = plt.subplots(figsize=(1, 1))
            high_carb_ax.pie(high_carb_data, labels=label, colors=colors, explode=(0.15, 0.075, 0.075), autopct='%1.1f%%', startangle=90,
                            wedgeprops= {"edgecolor":"black",
                            'linewidth': 1,
                            'antialiased': True})
            high_carb_ax.axis('equal')

            high_carb_breakfast_detail = high_carb_diet.get_breakfast_detail()
            high_carb_lunch_detail = high_carb_diet.get_lunch_detail()
            high_carb_dinner_detail = high_carb_diet.get_dinner_detail()

            lcb1_result = conn.execute("SELECT * FROM Dish WHERE Id = :id",
                                                            {'id': high_carb_breakfast_detail.id1}, ).fetchone()
            lcb2_result = conn.execute("SELECT * FROM Dish WHERE Id = :id",
                                                            {'id': high_carb_breakfast_detail.id2}, ).fetchone()
            lcl1_result = conn.execute("SELECT * FROM Dish WHERE Id = :id",
                                                            {'id': high_carb_lunch_detail.id1}, ).fetchone()
            lcl2_result = conn.execute("SELECT * FROM Dish WHERE Id = :id",
                                                            {'id': high_carb_lunch_detail.id2}, ).fetchone()
            lcd1_result = conn.execute("SELECT * FROM Dish WHERE Id = :id",
                                                            {'id': high_carb_dinner_detail.id1}, ).fetchone()
            lcd2_result = conn.execute("SELECT * FROM Dish WHERE Id = :id",
                                                            {'id': high_carb_dinner_detail.id2}, ).fetchone()
            
            high_carb_breakfast_1 = Dish(*lcb1_result)
            high_carb_breakfast_2 = Dish(*lcb2_result)
            high_carb_lunch_1 = Dish(*lcl1_result)
            high_carb_lunch_2 = Dish(*lcl2_result)
            high_carb_dinner_1 = Dish(*lcd1_result)
            high_carb_dinner_2 = Dish(*lcd2_result)

            with high_carb_1:
                st.markdown(
                    f"""
                        <h3 style="text-align: center">High Carb Diet</h3>
                        <table style="width:100%">
                            <tr>
                                <th style="font-size:18px;">Nutrition</th>
                            </tr>
                            <tr>
                                <td>
                                    <b>Calories:</b>
                                    <text style="float:right">{round(high_carb_nutrition_detail.calories)} cal</text><br/>
                                    <b>Carbs:</b>
                                    <text style="float:right">{high_carb_nutrition_detail.carbs} g</text><br/>
                                    <b>Fat:</b>
                                    <text style="float:right">{high_carb_nutrition_detail.fat} g</text><br/>
                                    <b>Protein:</b>
                                    <text style="float:right">{high_carb_nutrition_detail.protein} g</text><br/>
                                </td>
                            </tr>
                        </table>
                        <br/>
                        <div class="figure_title" style="text-align:center; font-size:20px"><b>Percent Calories From:</b></div>
                    """, unsafe_allow_html=True
                )
                st.pyplot(high_carb_fig)
            with high_carb_2:
                st.markdown(
                    f"""
                        <table style="white-space:nowrap; width:100%;">
                            <tr>
                                <td colspan="2"><b style="font-size:18px;">Breakfast</b><text style="float:right">{high_carb_breakfast_detail.calories} calories</text></td>
                            </tr>                            
                            <tr>
                                <td style="width: auto;"><img src="data:image/jpeg;base64,{base64.b64encode(high_carb_breakfast_1.image).decode('utf-8')}" width="70"></td>
                                <td><b>{high_carb_breakfast_1.name}</b><br/>
                                {high_carb_breakfast_detail.amount1} &nbsp; serving</td>
                            </tr>
                            <tr>
                                <td style="width: auto;"><img src="data:image/jpeg;base64,{base64.b64encode(high_carb_breakfast_2.image).decode('utf-8')}" width="70"></td>
                                <td><b>{high_carb_breakfast_2.name}</b><br/>
                                {high_carb_breakfast_detail.amount2} &nbsp; serving</td>
                            </tr>
                            <tr>
                                <td colspan="2"><b style="font-size:18px;">Lunch</b><text style="float:right">{high_carb_lunch_detail.calories} calories</text></td>
                            </tr>
                            <tr>
                                <td style="width: auto;"><img src="data:image/jpeg;base64,{base64.b64encode(high_carb_lunch_1.image).decode('utf-8')}" width="70"></td>
                                <td><b>{high_carb_lunch_1.name}</b><br/>
                                {high_carb_lunch_detail.amount1} &nbsp; serving</td>
                            </tr>
                            <tr>
                                <td style="width: auto;"><img src="data:image/jpeg;base64,{base64.b64encode(high_carb_lunch_2.image).decode('utf-8')}" width="70"></td>
                                <td><b>{high_carb_lunch_2.name}</b><br/>
                                {high_carb_lunch_detail.amount2} &nbsp; serving</td>
                            </tr>
                            <tr>
                                <td colspan="2"><b style="font-size:18px;">Dinner</b><text style="float:right">{high_carb_dinner_detail.calories} calories</text></td>
                            </tr>
                            <tr>
                                <td style="width: auto;"><img src="data:image/jpeg;base64,{base64.b64encode(high_carb_dinner_1.image).decode('utf-8')}" width="70"></td>
                                <td><b>{high_carb_dinner_1.name}</b><br/>
                                {high_carb_dinner_detail.amount1} &nbsp; serving</td>
                            </tr>
                            <tr>
                                <td style="width: auto;"><img src="data:image/jpeg;base64,{base64.b64encode(high_carb_dinner_2.image).decode('utf-8')}" width="70"></td>
                                <td><b>{high_carb_dinner_2.name}</b><br/>
                                {high_carb_dinner_detail.amount2} &nbsp; serving</td>
                            </tr>
                        </table><br/> 
                    """, unsafe_allow_html=True
                )

        st.write('You may structure these days in any preferred manner. I suggest keeping the high carb day for special occasions. That way you can attend family functions, or eat out with friends, and indulge a little more than normal.')