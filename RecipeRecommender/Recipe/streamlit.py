import streamlit as st
import pandas as pd
import numpy as np
import SessionState
import os
from PIL import Image

import rec_sys
import user_feedback
import user_dashboard
import meal_planner

import config, rec_sys
from ingredient_parser import ingredient_parser
import nltk

try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet")


def make_clickable(name, link):
    # target _blank to open new window
    text = name
    return f'<a target="_blank" href="{link}">{text}</a>'

# Function to display user dashboard
def display_user_dashboard(session_state):
    st.markdown("## User Dashboard")
    # Use user_dashboard module to display recent searches, favorite recipes, etc.
    user_dashboard.display(session_state)
    


# Function to display nutritional information
def display_nutritional_info(session_state):
    st.markdown("## Nutritional Information")

    if session_state.selected_recipe:
        recipe_name = session_state.selected_recipe  # Get the name of the selected recipe
        # Placeholder logic to retrieve nutritional information for the selected recipe
        nutritional_info = fetch_nutritional_info(recipe_name)  # Replace this with your logic

        if nutritional_info:
            st.write(f"Nutritional Information for {recipe_name}:")
            # Display nutritional information using Streamlit components
            for nutrient, value in nutritional_info.items():
                st.write(f"{nutrient.capitalize()}: {value}")
        else:
            st.write("Nutritional information is not available for this recipe.")
    else:
        st.write("Please select a recipe to view nutritional information.")


# Function to display meal planning and shopping list
def display_meal_planning(session_state):
    st.markdown("## Meal Planning and Shopping List")
    # Use meal_planner module to allow users to plan meals and generate a shopping list
    meal_planner.display(session_state)
   

def main():
    image = Image.open("input/wordcloud.png").resize((680, 150))
    st.image(image)
    st.markdown("# *Aren't you tired of wasting ingridients? :cooking:*")

    st.markdown(
        "## What different recipes can I can make? :tomato: "
    )
    st.markdown(
        "For example, what recipes can you make with the food in your apartment? :house: My ML based model will look through over 4500 recipes to find matches for you... :mag: Try it out for yourself below! :arrow_down:"
    )

    st.text("")

    session_state = SessionState.get(
        recipe_df="",
        recipes="",
        model_computed=False,
        execute_recsys=False,
        recipe_df_clean="",
    )

    ingredients = st.text_input("List your ingredients")
    session_state.execute_recsys = st.button("Get recommendations!")

    if session_state.execute_recsys:

        col1, col2, col3 = st.beta_columns([1, 6, 1])
        with col2:
            gif_runner = st.image("input/cooking_gif.gif")
        recipe = rec_sys.RecSys(ingredients)
        gif_runner.empty()
        session_state.recipe_df_clean = recipe.copy()
        recipe["url"] = recipe.apply(
            lambda row: make_clickable(row["recipe"], row["url"]), axis=1
        )
        recipe_display = recipe[["recipe", "url", "ingredients"]]
        session_state.recipe_display = recipe_display.to_html(escape=False)
        session_state.recipes = recipe.recipe.values.tolist()
        session_state.model_computed = True
        session_state.execute_recsys = False

    if session_state.model_computed:
        # st.write("Pick a particular recipe or see the top 5 recommendations.")
        recipe_all_box = st.selectbox(
            "See the top 5 recommendations or pick a particular recipe ya fancy",
            ["Show me them all!", "Select a single recipe"],
        )
        if recipe_all_box == "Show all!":
            st.write(session_state.recipe_display, unsafe_allow_html=True)
        else:
            selection = st.selectbox(
                "Select a delicious recipe", options=session_state.recipes
            )
            selection_details = session_state.recipe_df_clean.loc[
                session_state.recipe_df_clean.recipe == selection
            ]
            st.write(f"Recipe: {selection_details.recipe.values[0]}")
            st.write(f"Ingredients: {selection_details.ingredients.values[0]}")
            st.write(f"URL: {selection_details.url.values[0]}")
            st.write(f"Score: {selection_details.score.values[0]}")
           
            # Display user feedback form
            user_feedback.display(session_state)

            # Display user dashboard
            display_user_dashboard(session_state)

            # Display nutritional information
            display_nutritional_info(session_state)

            # Display meal planning and shopping list
            display_meal_planning(session_state)

if __name__ == "__main__":
    main()
