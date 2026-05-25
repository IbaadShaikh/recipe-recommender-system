import streamlit as st

def display(session_state):
    st.markdown("## Nutritional Information")

    selected_recipe = session_state.selected_recipe  # Retrieve the selected recipe from session state

    if selected_recipe:
        # Placeholder data for nutritional information (replace this with actual data retrieval)
        nutritional_info = {
            'Calories': 350,
            'Protein': 25,
            'Carbs': 40,
            'Fat': 15,
        }

        st.write(f"### Nutritional Information for {selected_recipe}")
        st.write("Here is the nutritional information for the selected recipe:")
        
        # Display nutritional information to the user
        for metric, value in nutritional_info.items():
            st.write(f"- {metric}: {value}g")  # Display each nutritional metric

    else:
        st.write("No recipe selected. Please select a recipe to view nutritional information.")
