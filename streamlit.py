import sys
sys.path.append("src")

import streamlit as st
import pandas as pd
import SessionState
import rec_sys


def make_clickable(name, link):
    return f'<a target="_blank" href="{link}">{name}</a>'


def main():
    st.title("Recipe Recommendation System")

    st.markdown(
        """
        Enter ingredients you have, and this app will recommend recipes using a
        machine learning-based recommendation system.
        """
    )

    session_state = SessionState.get(
        recipes=[],
        model_computed=False,
        recipe_df_clean=pd.DataFrame(),
        recipe_display="",
    )

    ingredients = st.text_input(
        "List your ingredients",
        placeholder="Example: chicken, rice, onion, tomato"
    )

    if st.button("Get recommendations"):
        if not ingredients.strip():
            st.warning("Please enter at least one ingredient.")
        else:
            try:
                with st.spinner("Finding recipe recommendations..."):
                    recipe = rec_sys.RecSys(ingredients)

                session_state.recipe_df_clean = recipe.copy()
                recipe["url"] = recipe.apply(
                    lambda row: make_clickable(row["recipe"], row["url"]),
                    axis=1
                )

                recipe_display = recipe[["recipe", "url", "ingredients", "score"]]
                session_state.recipe_display = recipe_display.to_html(
                    escape=False,
                    index=False
                )
                session_state.recipes = recipe.recipe.values.tolist()
                session_state.model_computed = True

            except Exception as e:
                st.error("Something went wrong while generating recommendations.")
                st.write(e)

    if session_state.model_computed:
        st.markdown("## Recommended Recipes")

        option = st.selectbox(
            "View all recommendations or select one recipe",
            ["Show all recommendations", "Select a single recipe"],
        )

        if option == "Show all recommendations":
            st.write(session_state.recipe_display, unsafe_allow_html=True)

        else:
            selection = st.selectbox(
                "Select a recipe",
                options=session_state.recipes
            )

            selection_details = session_state.recipe_df_clean.loc[
                session_state.recipe_df_clean.recipe == selection
            ]

            if not selection_details.empty:
                st.markdown("### Recipe Details")
                st.write(f"**Recipe:** {selection_details.recipe.values[0]}")
                st.write(f"**Ingredients:** {selection_details.ingredients.values[0]}")
                st.write(f"**URL:** {selection_details.url.values[0]}")
                st.write(f"**Score:** {selection_details.score.values[0]}")


if __name__ == "__main__":
    main()