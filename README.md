# **Problem Statement: Online Chatbot based ticketing system**
### Problem Statement ID: 1648
### Problem Statement Title: Online Chatbot Based Ticketing System
### Organization: Ministry of Culture
### Category: Software
### Theme: Travel & Tourism

### Background:
Visitors to museums frequently face challenges with traditional, manual ticket booking methods. These systems often lead to long queues, operational inefficiencies, and increased chances of human error. Such issues negatively impact the visitor experience and the institution's ability to handle high traffic during peak seasons and special exhibitions.

### Description:
This project implements an AI-powered multilingual chatbot-based ticketing system for museums in Tamil Nadu. The chatbot automates the booking process, handles gate entry and show ticket reservations, and provides real-time support to users. The system is accessible 24/7 across devices, reducing manual workload and improving visitor satisfaction.

### Key Features:
Improved Customer Service: The chatbot instantly assists users in booking tickets and answering FAQs, reducing wait time.
Efficient Handling of High Volumes: Capable of managing numerous booking requests during peak hours and special events.
Cost-Effective Solution: Reduces the need for manual ticket counters and staff by automating the process.
Data Collection and Analysis: Booking data is stored and can be used to improve services and drive marketing strategies.
Accessibility: Users can access the chatbot on multiple devices, making booking more convenient.
Reduced Human Error: Automation ensures accurate record-keeping and ticket issuance.
Multilingual Support: The chatbot supports various languages to cater to a diverse audience.
Enhanced Marketing and Promotion: Can promote upcoming museum events and exhibitions.

### Project Structure:
Website: Built using HTML, CSS, and JavaScript. Provides information about various Tamil Nadu museums and integrates the chatbot.
Chatbot: Developed using LangChain and Google Gemini. It manages ticket bookings and responds to museum-related queries.
Backend: Built with Flask and integrates MongoDB for user and booking data storage.

### Technologies Used:
Frontend: HTML, CSS, JavaScript
Chatbot: LangChain + Google Gemini
Backend: Flask (Python)
Database: MongoDB
Authentication: JWT, Bcrypt
NLP & Utilities: dateparser

### Setup Instructions:
Clone the repository:
git clone https://github.com/yourusername/museum-chatbot.git

### Navigate to the project directory:
cd museum-chatbot

### Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

### Install dependencies:
pip install -r requirements.txt

### Create a .env file in the root folder and add the following:
GOOGLE_API_KEY=your_google_gemini_api_key
MONGO_URI=mongodb://localhost:27017
JWT_SECRET_KEY=your_jwt_secret

### Run the development server:
python app.py

### Open in browser:
http://localhost:5000
