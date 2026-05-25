import streamlit as st

def display(session_state):
    st.markdown("## User Feedback")

    # Display UI elements for user feedback
    st.write("Please rate the recipe:")
    rating = st.slider("Rating", min_value=1, max_value=5, value=3, step=1)

    feedback_text = st.text_area("Feedback", "Share your thoughts...")
    
    submit_feedback = st.button("Submit Feedback")

    # Handling user interaction
    if submit_feedback:
        # Update session_state or store feedback in a database
        # For example, you can store feedback in a list within the session state
        if 'feedback_data' not in session_state:
            session_state.feedback_data = []

        # Capture feedback details
        feedback_details = {
            "rating": rating,
            "feedback_text": feedback_text
        }

        # Store feedback in session state
        session_state.feedback_data.append(feedback_details)
        
        st.success("Thank you for your feedback!")

    # Display previously submitted feedback if available
    if 'feedback_data' in session_state and session_state.feedback_data:
        st.markdown("### Previously Submitted Feedback")
        for idx, feedback in enumerate(session_state.feedback_data):
            st.write(f"**Feedback {idx + 1}:**")
            st.write(f"Rating: {feedback['rating']}")
            st.write(f"Feedback Text: {feedback['feedback_text']}")
