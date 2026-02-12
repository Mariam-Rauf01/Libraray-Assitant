📚 Library Assistant

Library Assistant is a Python-based application designed to simplify library management. It helps users quickly search for books, check availability, and get library information through an intelligent and user-friendly assistant.

🚀 Features

Book Search – Quickly find books in the library database by title

Availability Check – Check how many copies are available (for registered members)

Library Timings – Get library opening hours

Member Support – Features for both guests and registered members

Smart Guardrails – Handles non-library-related queries gracefully

AI-Powered Responses – Provides intelligent and helpful answers

Fallback Mode – Rule-based responses if AI integration isn’t available

🛠 Installation

Clone the repository

git clone <repository-url>
cd library


Install dependencies

pip install -r requirements.txt


(Optional) Setup environment variables

Create a .env file in the project root

Use it if you have AI integration settings

📂 Project Structure
library/
├── main.py           # Entry point to run test queries
├── assistant.py      # Core assistant logic
├── tools.py          # Functions like search_book, check_availability
├── database.py       # Pre-populated book database
├── models.py         # Data models (UserContext)
├── requirements.txt  # Python dependencies
├── .env              # Environment variables (optional)
└── README.md         # Project documentation

💡 Usage

Run the Library Assistant:

python main.py


Example Queries:

"Is 'The Great Gatsby' available?"

"Tell me about '1984'"

"What are the library hours?"

"How do I become a member?"

📚 Book Database (Sample)
Book Title	Author	Available Copies
The Great Gatsby	F. Scott Fitzgerald	3
To Kill a Mockingbird	Harper Lee	2
1984	George Orwell	5
Pride and Prejudice	Jane Austen	4
The Catcher in the Rye	J.D. Salinger	1
One Hundred Years of Solitude	Gabriel García Márquez	2
The Hobbit	J.R.R. Tolkien	3
Fahrenheit 451	Ray Bradbury	4
🕒 Library Timings

Monday to Friday – 9 AM to 8 PM

Saturday – 10 AM to 6 PM

Sunday – Closed

⚙ How It Works

User Input – User provides a query about library services

Query Analysis – System identifies if query is library-related

Tool Selection – Appropriate tool is selected (search, check availability, etc.)

Response Generation –

AI Integration: Provides intelligent responses

Fallback Mode: Rule-based answers if AI is unavailable

Output – Returns helpful information to the user

👥 Membership

Guest Users – Can search for books and view library timings

Registered Members – Access advanced features like availability checks

📦 Dependencies

python-dotenv – Environment variable management

pydantic – Data validation and settings management

📜 License

MIT License

🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit pull requests.
