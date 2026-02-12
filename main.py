"""Main entry point for the Library Assistant."""

from models import UserContext
from assistant import generate_response


def main():
    """Main function to run tests with the library assistant."""
    
    print("=" * 60)
    print("LIBRARY ASSISTANT")
    print("=" * 60)
    
    # Test 1: Registered member searching for a book
    print("\n--- Test 1: Registered Member Searching for a Book ---")
    user_context_registered = UserContext(name="Alice", member_id="M001")
    test_input_1 = "Is 'The Great Gatsby' available?"
    print(f"User: {test_input_1}")
    result_1 = generate_response(test_input_1, user_context_registered)
    print(f"Assistant: {result_1}")
    
    # Test 2: Registered member checking availability
    print("\n--- Test 2: Registered Member Checking Availability ---")
    test_input_2 = "Tell me about 'To Kill a Mockingbird'"
    print(f"User: {test_input_2}")
    result_2 = generate_response(test_input_2, user_context_registered)
    print(f"Assistant: {result_2}")
    
    # Test 3: Guest user (not registered)
    print("\n--- Test 3: Guest User (Not Registered) ---")
    user_context_guest = UserContext(name="Bob")
    test_input_3 = "What are the library timings?"
    print(f"User: {test_input_3}")
    result_3 = generate_response(test_input_3, user_context_guest)
    print(f"Assistant: {result_3}")
    
    # Test 4: Non-library question (should be blocked)
    print("\n--- Test 4: Non-Library Question (Guardrail Test) ---")
    test_input_4 = "What's the weather like today?"
    print(f"User: {test_input_4}")
    result_4 = generate_response(test_input_4, user_context_registered)
    print(f"Assistant: {result_4}")
    
    # Test 5: Library timings query
    print("\n--- Test 5: Library Timings Query ---")
    test_input_5 = "What are the library hours?"
    print(f"User: {test_input_5}")
    result_5 = generate_response(test_input_5, user_context_guest)
    print(f"Assistant: {result_5}")
    
    # Test 6: Membership query
    print("\n--- Test 6: Membership Query ---")
    test_input_6 = "How do I become a member?"
    print(f"User: {test_input_6}")
    result_6 = generate_response(test_input_6, user_context_guest)
    print(f"Assistant: {result_6}")


if __name__ == "__main__":
    main()
