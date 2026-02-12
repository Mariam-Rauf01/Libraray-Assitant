"""Function tools for the Library Assistant."""

from database import BOOK_DATABASE


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
    from database import LIBRARY_TIMINGS
    return f"📅 Library Timings:\n{LIBRARY_TIMINGS}"
