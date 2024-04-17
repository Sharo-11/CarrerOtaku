
# CarrerOtaku

Welcome to the Campus-Focused Placement Platform, a dynamic solution designed to revolutionize the way students and companies connect on campus.

## Project Overview

Our Campus-Focused Placement Platform is a comprehensive solution tailored to the unique needs of educational institutions. It acts as a bridge between students seeking valuable internships and job opportunities and companies eager to discover top talent within the campus community. This platform facilitates the entire placement process, providing students with a user-friendly interface to explore opportunities and enabling companies to streamline their campus hiring efforts.

## Getting Started

To run this project locally, follow the steps below:

### Prerequisites

Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository to your local machine:

   ```bash
   https://github.com/Sharo-11/CarrerOtaku.git
   ```

2. Navigate to the project directory:

   ```bash
   cd CarrerOtaku
   ```

3. Install Flask and other required libraries:

   ```bash
   pip install flask
   pip install flask-sqlalchemy
   pip install flask-login
   pip install WTForms
   ```

### Running the Application

1. Initialize the database:

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

2. Run the application:

   ```bash
   python app.py
   ```

   The application will be accessible at [http://localhost:5000](http://localhost:5000) in your web browser.

## Feedback

We value your feedback and are eager to enhance our platform continually. Please share your suggestions, feature requests, or report issues by reaching out to us at sharodubey1312@gmail.com.
