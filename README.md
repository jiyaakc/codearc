# ReparoHub - Electronics Repair Management Portal

## Overview
ReparoHub is a web-based platform designed to streamline the process of electronic product registration and repair request management. It provides an intuitive interface for customers to register their products, submit repair requests. Service providers (agents) can log in to manage incoming repair requests and update service statuses.

## Current Progress
### Implemented Features:
- **User Registration & Login**
  - Customers and service providers (agents) can sign up and log in using their email and password.
  - OTP verification is implemented for added security.
  
- **Product Registration**
  - Logged-in users can manually register their electronic products.
  - Registered products can be viewed from the user dashboard.
  
- **Service Provider Login**
-   signup is done with email,otp and pan number (for added security),pan number is validated.
  - Agents can log in and access a home dashboard.
  - 

### Work In Progress:
- **Repair Request Form** (Currently implemented but not storing data properly)
- **Agent Dashboard & Request Management** (Not yet implemented)
- **Service Center Assignment & Repair Status Tracking** (Planned for future implementation)

## Planned Features
- **Repair Request Submission**: Customers will be able to submit detailed repair requests, including issue descriptions and optional file uploads.
- **Service Center Assignment**: The system will suggest service centers based on the product brand and user location.
- **Repair Status Updates**: Agents will update the status of ongoing repairs, allowing customers to track progress.
- **Notifications**: Email/SMS/via app notifications for repair status updates.
- **Customer Support & Feedback**: Live chat, ticketing system, and service center reviews.
- **Admin Panel**: For managing users, repair requests, and service centers.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django (Python)
- **Database**:MySQL
- **Hosting**: Planned for AWS, Heroku, or similar Django-compatible platforms

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/reparohub.git
   cd reparohub
   ```
2. Create a virtual environment:
   ```bash
   python -m venv arcenv
   source arcenv/bin/activate   # On macOS/Linux
   arcenv\Scripts\activate      # On Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```
6. Open `http://127.0.0.1:8000/` in your browser.

## Known Issues
- The repair request form is implemented but not saving data correctly.
- No functionality yet for agents to process repair requests.

## Future Enhancements
- Implementing the repair request system fully
- Developing the agent dashboard for request management
- Service center suggestions and auto-assigning requests



