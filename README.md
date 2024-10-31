# MMORPG Project

Welcome to the MMORPG project! This is a web application where users can create and share character posts. Users can choose from various categories, engage with others, and explore the content. The application is built using Python, Django, CSS, and HTML.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [User Guide](#user-guide)
- [Technologies Used](#technologies-used)

## Features

- **Character Categories**: Users can create posts under the following categories:
  - Tanks
  - Healers
  - Damage Dealers
  - Merchants
  - Guild Masters
  - Quest Givers
  - Blacksmiths
  - Tanners
  - Potion Makers
  - Spell Masters
  
- **Post Creation**: When creating a post, users can add:
   - Author name
  - Title
  - Text content
  - Image
    
- **Homepage Features**:
  - A "Become an Author" button to create posts under your name.
  - A display of all posts categorized by selected tags.
  - Clicking on a post leads to a detailed view, including:
    - Full post content
    - Replies section showing:
      - Reply author
      - Date of reply
      - Text of reply (comment)

- **Search Functionality**: 
  - A search page allows users to find posts by title, author, or date.

- **User Panel**:
  - Displays all posts created by the user.
  - Options to log out and create a new post.
  - Language switcher to toggle between Russian and English.

- **Guest Access**: 
  - Non-logged-in users can view all posts but cannot create them or access their personal panel.

- **Account Creation**: 
  - Users can create accounts via email or Google.
  - Email verification with an activation code sent to the user's email upon registration.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/AnastasiaGundova/MMORPG.git
   cd mmorpg
   ```
2. Install the required packages:
   ```pip install -r requirements.txt```
3. Set up the database:
   ```python manage.py migrate```
4. Run the development server:
   ```python manage.py runserver```
5. Access the application at http://127.0.0.1:8000/.
   
## Usage
  - Navigate to the homepage to explore all character posts.
  - Click "Become an Author" to create a new post.
  - Use the search feature to find specific posts.
  - Interact with posts by leaving replies and comments.
- **User Guide**:
  1. Creating an Account:
    - Click on the registration option and fill in the required details.
    - Verify your email to activate your account.
  2. Creating a Post:
    - After logging in, click on "Create New Post."
    - Fill in the title, text, upload an image, and select a category.
    - Submit your post to have it published.
  3. Viewing Posts:
    - Browse the homepage to view all posts.
    - Click on a post to read its full content and view comments.
  4. Managing Your Account:
    - Access the User panel to view and manage your posts.
    - Log out when finished.
## Technologies Used
- Python
- Django
- HTML
- CSS

