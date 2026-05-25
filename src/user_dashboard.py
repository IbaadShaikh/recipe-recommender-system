import streamlit as st

def display(session_state):
    st.markdown("## User Dashboard")

    # Example: Display recent searches
    st.subheader("Recent Searches:")
    recent_searches = session_state.get("recent_searches", [])
    if not recent_searches:
        st.write("No recent searches.")
    else:
        st.write(recent_searches)

    # Example: Display favorite recipes
    st.subheader("Favorite Recipes:")
    favorite_recipes = session_state.get("favorite_recipes", [])
    if not favorite_recipes:
        st.write("No favorite recipes yet.")
    else:
        st.write(favorite_recipes)

    # Example: Add a button to clear recent searches
    if st.button("Clear Recent Searches"):
        session_state.recent_searches = []
        st.success("Recent searches cleared!")

    # Example: Add a button to clear favorite recipes
    if st.button("Clear Favorite Recipes"):
        session_state.favorite_recipes = []
        st.success("Favorite recipes cleared!")

# Sample logic to simulate data updates
# Replace this with actual logic based on your data structure and storage
def update_user_dashboard(session_state):
    # Assume recent searches and favorite recipes are stored in the session state
    # Replace this with actual data retrieval logic from your application's data source
    recent_searches = ["Pasta", "Salad", "Soup"]
    favorite_recipes = ["Spaghetti Carbonara", "Caesar Salad", "Tomato Basil Soup"]

    # Update the session state with fetched data
    session_state.recent_searches = recent_searches
    session_state.favorite_recipes = favorite_recipes
