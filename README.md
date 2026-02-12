# 📚 Library Assistant

A smart, AI-powered library management assistant that helps users search for books, check availability, and get instant answers to library-related questions. Built with Python and designed for seamless library operations.

![Library Assistant](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 **Smart Book Search** | Instantly find books by title in the library database |
| 📊 **Availability Tracking** | Real-time check of available copies for registered members |
| 🕐 **Library Hours** | Get instant information about operating hours |
| 👤 **Multi-User Support** | Separate experiences for guests and registered members |
| 🛡️ **Smart Guardrails** | Gracefully handles non-library queries |
| 🤖 **Intelligent Responses** | Context-aware answers powered by AI |
| 🔄 **Fallback System** | Reliable rule-based responses when AI is unavailable |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd library

# Install dependencies
pip install -r requirements.txt
```

### Configuration (Optional)

Create a `.env` file in the project root for AI integration:

```env
AI_API_KEY=your_api_key_here
```

---

## 📁 Project Structure

```
library/
├── main.py              # 🎯 Entry point - run test queries here
├── assistant.py         # 🧠 Core assistant logic and AI integration
├── tools.py             # 🔧 Utility functions (search, availability)
├── database.py          # 💾 Pre-populated book database
├── models.py            # 📋 Data models (UserContext, Book, etc.)
├── requirements.txt     # 📦 Python dependencies
├── .env                 # 🔐 Environment variables (optional)
└── README.md            # 📖 This file
```

---

## 💡 Usage

### Run the Assistant

```bash
python main.py
```

### Example Queries

| Query | Expected Response |
|-------|-------------------|
| "Is 'The Great Gatsby' available?" | Book availability status |
| "Tell me about '1984'" | Book details and availability |
| "What are the library hours?" | Operating hours |
| "How do I become a member?" | Membership information |

---

## 📚 Sample Book Database

| Title | Author | Available |
|-------|--------|-----------|
| The Great Gatsby | F. Scott Fitzgerald | 3 |
| To Kill a Mockingbird | Harper Lee | 2 |
| 1984 | George Orwell | 5 |
| Pride and Prejudice | Jane Austen | 4 |
| The Catcher in the Rye | J.D. Salinger | 1 |
| One Hundred Years of Solitude | Gabriel García Márquez | 2 |
| The Hobbit | J.R.R. Tolkien | 3 |
| Fahrenheit 451 | Ray Bradbury | 4 |

---

## 🕒 Library Timings

| Day | Hours |
|-----|-------|
| Monday - Friday | 9:00 AM - 8:00 PM |
| Saturday | 10:00 AM - 6:00 PM |
| Sunday | Closed |

---

## ⚙️ How It Works

```
┌─────────────┐
│ User Query  │
└──────┬──────┘
       ▼
┌─────────────┐
│ Query       │
│ Analysis    │
└──────┬──────┘
       ▼
┌─────────────┐
│ Tool        │
│ Selection   │
└──────┬──────┘
       ▼
┌─────────────┐    ┌─────────────┐
│ AI Response │    │ Fallback    │
│ (Primary)   │    │ (Backup)    │
└──────┬──────┘    └──────┬──────┘
       │                  │
       └────────┬─────────┘
                ▼
        ┌─────────────┐
        │ User Output │
        └─────────────┘
```

### Step-by-Step Flow

1. **User Input** - Query about library services
2. **Query Analysis** - System determines intent
3. **Tool Selection** - Routes to appropriate handler
4. **Response Generation** - AI or rule-based response
5. **Output** - Delivers helpful information

---

## 👥 Membership Tiers

### Guest Users
- ✅ Search for books
- ✅ View library timings
- ❌ Check availability

### Registered Members
- ✅ All guest features
- ✅ Real-time availability checks
- ✅ Reserve books (coming soon)

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `python-dotenv` | Environment variable management |
| `pydantic` | Data validation and models |

---

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| AI responses not working | Check `.env` file and API key |
| Import errors | Run `pip install -r requirements.txt` |
| Database empty | Restart application to load sample data |

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📧 Contact

For questions or support, please open an issue in the repository.

---

<div align="center">

**Made with ❤️ for library enthusiasts**

</div>
