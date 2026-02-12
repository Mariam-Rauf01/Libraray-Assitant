"""
Library Assistant using Google Gemini API
"""

import os
from typing import Optional
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env file
load_dotenv()

# Configure Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)


# =============================================================================
# Data Models
# =============================================================================

class UserContext(BaseModel):
    """User context with name and member_id"""
    name: str
    member_id: Optional[str] = None


# =============================================================================
# Book Database
# =============================================================================

BOOK_DATABASE = {
    "The Great Gatsby": {"author": "F. Scott Fitzgerald", "available": 3},
    "To Kill a Mockingbird": {"author": "Harper Lee", "available": 2},
    "1984": {"author": "George Orwell", "available": 5},
    "Pride and Prejudice": {"author": "Jane Austen", "available": 4},
    "The Catcher in the Rye": {"author": "J.D. Salinger", "available": 1},
    "One Hundred Years of Solitude": {"author": "Gabriel García Márquez", "available": 2},
    "The Hobbit": {"author": "J.R.R. Tolkien", "available": 3},
    "Fahrenheit 451": {"author": "Ray Bradbury", "available": 4},
}

LIBRARY_TIMINGS = "Monday to Friday: 9 AM to 8 PM, Saturday: 10 AM to 6 PM, Sunday: Closed"


# =============================================================================
# Function Tools
# =============================================================================

def search_book(book_name: str) -> str:
    """
    Search for a book in the library database.
    
    Args:
        book_name: The name of the book to search for
    
    Returns:
        str: Information about the book if found, or message if not found
    """
    # Normalize book name for search
    search_name = book_name.strip().lower()
    
    for book, info in BOOK_DATABASE.items():
        if search_name == book.lower():
            return f"✅ Book found: '{book}' by {info['author']}. Available copies: {info['available']}"
    
    return f"❌ Book '{book_name}' not found in our database."


def check_availability(book_name: str, member_id: str) -> str:
    """
    Check the availability of a book (only for registered members).
    
    Args:
        book_name: The name of the book to check
        member_id: The member ID to verify registration
    
    Returns:
        str: Availability information or error message
    """
    # Check if user is registered
    if not member_id:
        return "🔒 This tool is only available for registered library members. Please provide your member_id."
    
    # Normalize book name for search
    search_name = book_name.strip().lower()
    
    for book, info in BOOK_DATABASE.items():
        if search_name == book.lower():
            return f"📚 '{book}' by {info['author']}: {info['available']} copies available"
    
    return f"❌ Book '{book_name}' not found in our database."


def get_library_timings() -> str:
    """
    Get the library timings.
    
    Returns:
        str: Library timing information
    """
    return f"📅 Library Timings:\n{LIBRARY_TIMINGS}"


# =============================================================================
# Library Assistant
# =============================================================================

def is_library_related(query: str) -> tuple[bool, str]:
    """
    Check if a query is library-related.
    
    Returns:
        tuple: (is_library_related, reason)
    """
    query_lower = query.lower()
    
    # Check for book names in database
    book_names_lower = [book.lower() for book in BOOK_DATABASE.keys()]
    for book_name in book_names_lower:
        if book_name in query_lower:
            return True, f"Query mentions book '{book_name}'"
    
    library_keywords = [
        "book", "library", "borrow", "return", "member", "membership",
        "available", "timings", "hours", "reading", "author", "novel",
        "search", "recommend", "loan", "fine", "policy", "catalog"
    ]
    
    # Check for library-related keywords
    keyword_count = sum(1 for keyword in library_keywords if keyword in query_lower)
    
    non_library_keywords = [
        "weather", "sports", "politics", "cooking", "recipe", "travel",
        "movies", "music", "gaming", "technology", "news", "science"
    ]
    
    # Check for non-library topics (only if no library keywords found)
    if keyword_count == 0:
        for keyword in non_library_keywords:
            if keyword in query_lower:
                return False, f"Query about '{keyword}' is not library-related"
    
    if keyword_count >= 1 or "book" in query_lower or "author" in query_lower:
        return True, f"Query contains library-related content"
    
    return False, "Query does not appear to be library-related"


def generate_response(user_input: str, user_context: UserContext) -> str:
    """
    Generate a response using Gemini API.
    
    Args:
        user_input: The user's question
        user_context: The user's context information
    
    Returns:
        str: The assistant's response
    """
    # Check if the query is library-related
    is_related, reason = is_library_related(user_input)
    
    if not is_related:
        return f"❌ I'm a Library Assistant and can only help with library-related queries.\nReason: {reason}\n\nPlease ask about books, library membership, timings, or borrowing policies."
    
    # Build context information
    context_info = f"""
User: {user_context.name}
Member ID: {user_context.member_id if user_context.member_id else 'Not registered'}
"""
    
    # Build tools description
    tools_info = f"""
Available Tools:
1. search_book - Search for a book by name
2. check_availability - Check availability (members only)
3. get_library_timings - Get library hours

Books in database: {', '.join(BOOK_DATABASE.keys())}

Library Timings: {LIBRARY_TIMINGS}
"""
    
    system_prompt = f"""You are a helpful Library Assistant. Be friendly and professional.

{context_info}

{tools_info}

Rules:
- Always use the available tools when appropriate
- Provide helpful information about books and library services
- If asked about non-library topics, politely redirect to library services
- Keep responses concise but informative
- If asked about book availability, provide full details including author
"""

    # Check if Gemini is configured
    if not GEMINI_API_KEY:
        # Fallback to rule-based response without AI
        return rule_based_response(user_input, user_context)
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content([
            {"role": "user", "parts": [f"{system_prompt}\n\nUser: {user_input}"]}
        ])
        return response.text
    except Exception as e:
        # Fallback to rule-based response
        return rule_based_response(user_input, user_context)


def rule_based_response(user_input: str, user_context: UserContext) -> str:
    """
    Fallback rule-based response without AI.
    """
    query_lower = user_input.lower()
    
    # Check for book searches
    for book, info in BOOK_DATABASE.items():
        if book.lower() in query_lower:
            if "timing" in query_lower or "hours" in query_lower or "when" in query_lower:
                return f"📚 '{book}' by {info['author']} is available ({info['available']} copies).\n\n{LIBRARY_TIMINGS}"
            return f"📚 '{book}' by {info['author']}: {info['available']} copies available.\n\nYou can borrow this book if you're a member!"
    
    # Check for library timings
    if "timing" in query_lower or "hours" in query_lower or "open" in query_lower:
        return f"📅 Library Timings:\n{LIBRARY_TIMINGS}"
    
    # Check for membership
    if "member" in query_lower or "register" in query_lower:
        if user_context.member_id:
            return f"✅ You are a registered member (ID: {user_context.member_id})!"
        return "🔒 To become a member, please visit the library. Members can access full book availability features."
    
    # Default response
    return f"📚 Welcome to the Library Assistant! {user_context.name}.\n\nI can help you:\n- Search for books\n- Check availability\n- Get library timings\n\n{LIBRARY_TIMINGS}"


# =============================================================================
# Test Queries
# =============================================================================

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
