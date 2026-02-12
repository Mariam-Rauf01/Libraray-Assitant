# Library Assistant

A Python-based Library Assistant application powered by Google Gemini API that helps users manage library-related queries, search for books, check availability, and get library information.

## Features

- **Book Search**: Search for books in the library database by title
- **Availability Check**: Check the availability of books (for registered members only)
- **Library Timings**: Get information about library operating hours
- **Member Support**: Support for both registered members and guest users
- **Smart Guardrails**: Detects and handles non-library related queries
- **AI-Powered Responses**: Uses Google Gemini API for intelligent responses
- **Fallback Mode**: Rule-based fallback when API key is not configured

## Prerequisites

- Python 3.7+
- Google Gemini API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd library
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Project Structure

```
library/
├── main.py                # Entry point with test queries
├── assistant.py           # Main assistant logic (Gemini API integration)
├── tools.py               # Function tools (search_book, check_availability, etc.)
├── database.py            # Book database and library data
├── models.py              # Data models (UserContext)
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API keys)
└── README.md             # This file
```

## Usage

### Run the Library Assistant

```bash
python main.py
```

### Available Commands

The assistant can help with:
- **Search for books**: "Is 'The Great Gatsby' available?"
- **Check availability**: "Tell me about 'To Kill a Mockingbird'"
- **Library timings**: "What are the library hours?"
- **Membership queries**: "How do I become a member?"

## Dependencies

- `google-generativeai` - Google Gemini API client
- `python-dotenv` - Environment variable management
- `pydantic` - Data validation and settings management

## Book Database

The application includes a pre-populated book database with the following titles:

| Book Title | Author | Available Copies |
|------------|--------|------------------|
| The Great Gatsby | F. Scott Fitzgerald | 3 |
| To Kill a Mockingbird | Harper Lee | 2 |
| 1984 | George Orwell | 5 |
| Pride and Prejudice | Jane Austen | 4 |
| The Catcher in the Rye | J.D. Salinger | 1 |
| One Hundred Years of Solitude | Gabriel García Márquez | 2 |
| The Hobbit | J.R.R. Tolkien | 3 |
| Fahrenheit 451 | Ray Bradbury | 4 |

## Library Timings

- **Monday to Friday**: 9 AM to 8 PM
- **Saturday**: 10 AM to 6 PM
- **Sunday**: Closed

## How It Works

1. **User Input**: The user provides a query about library services
2. **Query Analysis**: The system checks if the query is library-related
3. **Tool Selection**: Appropriate tools are selected based on the query
4. **Response Generation**: 
   - With API key: Uses Gemini AI for intelligent responses
   - Without API key: Falls back to rule-based responses
5. **Output**: Returns helpful information to the user

## Membership

- **Guest Users**: Can search for books and get library timings
- **Registered Members**: Can access additional features like availability checks

## License

MIT License

## Contributing

Feel free to submit issues and enhancement requests!
