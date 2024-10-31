# MMORPG Project

Welcome to the MMORPG project! This is a web application where users can create and share character posts. Users can choose from various categories, engage with others, and explore the content. The application is built using Python, Django, CSS, and HTML.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [User Guide](#user-guide)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

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
  - Title
  - Text content
  - Image
  - Author name

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
   ```bash
   git clone https://github.com/yourusername/mmorpg.git
   cd mmorpg
