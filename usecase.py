import os
from google.cloud import dialogflow

# --- IMPORTANT ---
# 1. Set your GOOGLE_APPLICATION_CREDENTIALS environment variable first.
# 2. Replace 'YOUR_PROJECT_ID' with your Google Cloud Project ID.
# -----------------

PROJECT_ID = "YOUR_PROJECT_ID"
SESSION_ID = "some-unique-session-id" # Can be any unique string

def detect_intent(project_id, session_id, text, language_code="en-US"):
    """Returns the structured response from Dialogflow."""
    
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    
    print(f"Sending query: '{text}'")

    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

        print("=" * 20)
        print(f"Intent detected: {response.query_result.intent.display_name}")
        print(f"Confidence: {response.query_result.intent_detection_confidence:.2f}")
        print(f"Fulfillment Text: {response.query_result.fulfillment_text}")
        
        # Print parameters (like the @sys.date-time)
        if response.query_result.parameters:
            print("Parameters:")
            for param, value in response.query_result.parameters.items():
                # Value can be complex (like a struct), so we print it simply
                print(f"  - {param}: {value}")
        
        print("=" * 20)
        return response.query_result

    except Exception as e:
        print(f"Error detecting intent: {e}")
        return None

# --- Main execution ---
if _name_ == "_main_":
    
    # 1. Test a query that matches the steps in your image
    user_query = "I want to reserve a table for tomorrow at 7pm"
    detect_intent(PROJECT_ID, SESSION_ID, user_query)
    
    print("\n" + "-"*30 + "\n")
    
    # 2. Test the Default Welcome Intent
    user_query_2 = "Hello"
    detect_intent(PROJECT_ID, SESSION_ID, user_query_2)
