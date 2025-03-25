# Right Place to Blog

## Overview
Right Place to Blog is a feature-rich blogging platform built with Django that allows users to create, publish, and interact with blog posts. The application provides a clean, responsive user interface with both light and dark mode support, comprehensive user authentication, and social features like likes, loves, and comments.

The live project can be viewed [here](https://edite-blog-a9c16877beb1.herokuapp.com)


![all-devices-black (2)](https://github.com/user-attachments/assets/f219c3bb-f423-4086-94c4-d0703c087e6b)

## Features
- **User Authentication**: Complete user registration and login system powered by django-allauth
- **Blog Management**: Create, edit, delete, and publish/unpublish blog posts
- **Rich Text Editing**: TinyMCE integration for formatting blog content
- **Interactions**: Like, love, and comment on blog posts
- **Search & Filter**: Find posts by title, content, or author
- **Dashboard**: Personal statistics showing post counts, interactions, and most popular content
- **Accessibility**: WCAG-compliant design with keyboard navigation, screen reader support, and color contrast
- **Responsive Design**: Mobile-friendly interface that works across devices
- **Light/Dark Mode**: Theme toggle that respects system preferences and saves user choice

## Technology Stack
- **Backend**: Django 4.2
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **CSS Framework**: Bootstrap 5
- **Icons**: Bootstrap Icons
- **Rich Text Editor**: TinyMCE
- **Authentication**: django-allauth
- **Deployment**: Whitenoise for static files

## Project Structure
```
django_blog/
├── blog/
│   ├── models.py          # Database models (Post, Comment, etc.)
│   ├── views.py           # View functions and classes
│   ├── forms.py           # Form definitions
│   ├── urls.py            # URL routing
│   └── admin.py           # Admin interface configuration
├── editeblog/             # Project settings
│   ├── settings.py        # Django settings
│   ├── urls.py            # Project URL configuration
│   └── wsgi.py            # WSGI configuration
├── static/                # Static assets
│   ├── css/               # CSS files
│   │   └── style.css      # Custom styles
│   └── js/                # JavaScript files
│       └── theme.js       # Theme toggle functionality
├── templates/             # HTML templates
│   ├── base.html          # Base template with common elements
│   ├── index.html         # Homepage template
│   ├── account/           # Authentication templates
│   └── blog/              # Blog-specific templates
└── requirements.txt       # Project dependencies

```
## Wireframes
<details open>
<summary>Wireframe - Blog Post </summary>  
   
![Blog post](https://github.com/user-attachments/assets/9509a9d1-17d4-4668-b32e-85cdf9f755cf)

</details> 

<details>
<summary>Wireframe - Register </summary>  

![register](https://github.com/user-attachments/assets/9d2e6bdd-25de-46ce-b37c-5e9744316970)

</details> 

<details>
<summary>Wireframe - Login </summary>  

![Login](https://github.com/user-attachments/assets/e3e4420a-008c-4e54-950a-f14756506db5)

</details> 

<details>
<summary>Wireframe - My Blog Post </summary>  

![my blog post](https://github.com/user-attachments/assets/c573313c-ebf7-4973-80ee-5ec8d60e8c99)

</details> 

<details>
<summary>Wireframe - Create New Post </summary>  

![create new post](https://github.com/user-attachments/assets/9020b84b-1408-4f3e-a182-d7b5a098810a)

</details> 

<details>
<summary>Wireframe - Dashboard </summary>  

![dashboard](https://github.com/user-attachments/assets/67da6def-a89a-4a8b-994f-69d7a933c5d1)

</details> 

<details>
<summary>Wireframe - Logout </summary>  

![sign out](https://github.com/user-attachments/assets/3b825c56-3e30-43ef-a99d-dc89e9d342cd)

</details> 





## Installation and Setup
1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/django_blog.git
   cd django_blog
2. Create a virtual environment and activate it
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables (create env.py file with the following):
   ```python
   import os
   os.environ["SECRET_KEY"] = "your-secret-key"
   os.environ["DATABASE_URL"] = "your-database-url"
   ```

5. Apply migrations
   ```bash
   python manage.py migrate
   ```

6. Create a superuser
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server
   ```bash
   python manage.py runserver
   ```

## User Experience (UX)
  #### User stories 

1. **Creating a Post**: Log in and click "New Post" in the navigation bar to create a blog post
2. **Editing/Deleting Posts**: From "My Posts" or from the dashboard, you can edit or delete your own posts
3. **Interacting with Posts**: Like, love, or comment on posts to engage with other users' content
4. **Dashboard**: View your statistics and activity from the dashboard page
5. **Searching**: Use the search bar to find posts by title, content, or author

The User Stories in this project are documented in GitHub Projects. 
The project board link, can find [here](https://github.com/users/Edite10/projects/7/views/1) 

## Deployment
This project can be deployed to various hosting platforms:

### Heroku Deployment

#### Setting up a cloudinary account for static storage.
1. Navigate to www.cloudinary.com, and click the Sign Up for Free button. Create a new account.
2. Click on Create Account, and click the link in the verification email that you'll be sent.
3. On the Dashboard, copy the API Environment variable somewhere safe - this must be added to the Heroku
configuration variables in the next section.

#### Deploying the app on Heroku
1. Log into Heroku and navigate to the Dashboard.
2. Click on the 'New' button.
3. Choose a unique app name, and select the region closest to you.
4. Create a database on Heroku
    - Click on the Resources tab.
    - Click the Find more add-ons button.
    - Select Heroku Postgres, and click on Install Heroku Postgres.
    - Select a plan and select your app.
    - Return to Resources tab and click on the Heroku Postgres icon, then select the settings tab and click on Database Credentials. Copy the URI to your clipboard. Paste it to your env.py file using the key "DATABASE_URL". This will allow you to use the same database for development and production.
5. Click the settings tab on the Dashboard, and click the button to Reveal Config Vars. Your database url should be populated here already. Add your Django secret key.
Set the PORT to 8000. I also have a GOOGLE-API-KEY config variable to enable Social-Sign-In with Google.
6. In your local repository, add a Procfile to the root directory of the project, containing the following line :<br /> `web: gunicorn editeblog.wsgi`.
7. Add the url of your Heroku project to the `ALLOWED_HOSTS` list in `settings.py`.
8. Set DEBUG to False, and commit your changes and push to GitHub.
9. In Heroku, navigate to the Settings Tab, and within this the Buildpacks section, and click on Add Buildpack. Select the python buildpack, and save changes.
10. On the Dashboard, select the Deploy tab, and under the Deployment Method heading, select the
GitHub icon to connect your Heroku project to your GitHub repo. Enter your repository name in the text input, and click Search, and then when your repo appears, click Connect.
11. Under the Manual deploy section, click Deploy Branch. You should receive this message - 'Your app was successfully deployed". Click view to see the app running in the browser.

### Other Deployment Options
- AWS Elastic Beanstalk
- DigitalOcean
- PythonAnywhere
- Self-hosted with Gunicorn and Nginx

## Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgments

The main additions are:
1. Completing the Installation and Setup section with all necessary steps
2. Adding a Usage section explaining how to use the application
3. Including a Deployment section with instructions for various platforms
4. Adding a Contributing section to encourage collaboration
5. Making the formatting consistent throughout the document

## AI Assistance & Development Process

This project was developed with significant assistance from AI tools, primarily GitHub Copilot and OpenAI's ChatGPT. The AI tools helped with:

1. **Code Generation**: Initial model structures, view logic, and template layouts
2. **Debugging**: Identifying and fixing errors in code
3. **Recommendations**: Suggesting modern features and best practices
4. **Accessibility**: Enhancing accessibility features and compliance
5. **Documentation**: Assisting with code documentation and README creation

Approximately 60-70% of the codebase was initially generated or suggested by AI tools, with human oversight, customization, and refinement. The AI particularly excelled at:
- Setting up repetitive code patterns
- Implementing common Django patterns consistently
- Generating boilerplate HTML and CSS
- Suggesting optimizations and improvements
- Creating consistent styling across templates

The human developer was essential for:
- Project architecture decisions
- Quality control and testing
- Custom feature specifications
- Business logic implementation
- UI/UX design decisions
- Integration of various components

## Future Improvements
1. **User Profiles**: Enhanced user profiles with avatars, bios, and social links
2. **Categories and Tags**: Better organization of content with hierarchical categories
3. **Image Uploads**: Direct image uploads in blog posts with gallery management
4. **Newsletter Integration**: Allow readers to subscribe to new posts
5. **Social Authentication**: Login with Google, Facebook, etc.
6. **Advanced Analytics**: Track post views, reader demographics
7. **Scheduled Publishing**: Set future publish dates for posts
8. **SEO Optimization**: Meta tags, structured data, and sitemap generation
9. **Multi-language Support**: Internationalization and localization
10. **Progressive Web App**: Offline support and mobile app features

## Challenges
#### Lack of commits

   Due to technical reasons, I had to delay the development of my project. As a result, it was not possible to work on my computer, so the solution was that I could work on another computer. However, to be able to do a Git push, the files had to be transferred back to my computer. When transferring the files, the commits were lost.


## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Frameworks, Libraries, Technologies & Programs Used
- Balsamiq - used to create wireframes.
- GitHub - used to save and store all files. 
- Git - used for version control.
- GitPod - used as a workspace.
- Visual Studio Code - Used to SSH into my GitPod workspace.
- Bootstrap v5.3
- Google Fonts - fonts were chose imported from here  
- Dev Tools - to debug and for testing responsiveness 
- Google Lighthouse - for auditing the website
- W3C Validator - for validating the HTML and CSS code
- Heroku - for deployment

## Acknowledgments
- Django and its community for the excellent framework
- Bootstrap for the responsive design components
- TinyMCE for the rich text editing capabilities
- All open-source contributors whose libraries made this project possible


## Testing
  ### Testing browsers
  - Opera GX
  - Mozzila Firefox
  - Microsoft Edge

#### **HTML Validation using W3C Validation**

![Screenshot 2025-03-25 111424](https://github.com/user-attachments/assets/4df32a5d-25b3-42ec-ab4f-ec839041c689)

#### **CSS Validation using W3C Validation**

![Screenshot 2025-03-25 111320](https://github.com/user-attachments/assets/0f90ff86-5c75-4e6d-bfbf-aa7348322942)


#### **Lighthouse scores via Chrome Developer Tools**

![lighthouse](https://github.com/user-attachments/assets/42384436-2b53-4fe5-9c6d-6fa066a343f8)

