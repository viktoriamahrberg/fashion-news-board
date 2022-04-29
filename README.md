

Live link [here](https://fashionews.herokuapp.com/)

# About

Fashionews is a blog-like news page where anyone can share their local news from the fashion industry. May it be about a new fashion school with focus on sustainability and social justice in your city or the cool concept store in your home-town now expanding to another city, share it! 
We can read about the big brands revenue and change of directors on a daily basis in the big newspapers - this is not about them - this is about supporting and sharing our local fashion-heroes.


# UX

## User Goals

Users should be able to read about fashion news that are not in the big tabloids.

Signed in users should additionally be able to share news that happen locally to them and comment on others posts.

## Site Owner Goals

Site owner should be able to control users, posts and comments in case of violation of a safe community space.


## User Stories
- As a Site user I want to see all available news on the frontpage so that I can click decide on what I want to read more about.
- As a Site user I want to click on a news-post so that I can read the full news article.
- As a Site user I want to register an account so that I can create a news-post, comment and interact with other posts.
- As a Site user I want to receive flash messages after my actions so that I know if I successfully have processed my action.
- As a Site user I want to make posts so that I can share fashion news around me with the community.
- As a Site user I want to add photos as well as text to my posts in a userfriendly way so that I can make the posts more appealing with the images.
- As a Site user I want to to see when the news-post was posted so that I know when the news was from.
- As a Site user I want to see a link to the original post so that I can see that the news is legit.
- As a Site user I want to search for a news-post so that I easily can navigate to a specific post.
- As a Site admin I want to delete inappropriate users or users who spread fake news so that I keep the site legit and trustworthy.

- As a Site user I want to choose what to read from a category list so that I can read that of what is in my interest.
- As a Site user I want to share a post on social media so that I can interact with and spread the articles I find interesting.
- As a Site user I want to login or register account with my Facebook or Google account so that I can speed up the login/register process.


## Structure of the website

The site is simply structured after a blog concept where the news are added in chronological order with the latest ones on top. The home page is paginated witn only 4 posts per page - for users not to be overwhelmed with content. 

I believe in peoples right and judgement to share fashion related news in an appropirate manners and therefor news-post are not being approved by the admin - but can be removed by the admin if needed.

Any user on the page can read the excerpt of the news and click on each post for further reading, but only signed in users can make a comment to the news-post. 

Any *signed in* user can additionally:

- Comment on posts

- Create posts

- Edit posts

- Delete posts

Full CRUD (Create, Read, Update, Delete) functionality is implemented for posting on the site.

## Wireframes

The layout for this project is set after the blogpost layout which is what users know best how to interact with. A navbar and four blogposts following. On mobile devices the site is only showing one post followed by the rest vertically.
I made the wireframes in Figma:

**Home Page:**

![Home page](/static/readme_images/wireframe_home.png)

**Detailed Post Page:**

![Detailed Post page](/static/readme_images/wireframe_detailed_post.png)

**Mobile:**

![Mobile](/static/readme_images/wireframe_mobile.png)



## Design

I wanted to use a clear layout and color scheme for a serious but fashionable news look and used Bootstrap as a toolkit with maincolors of black and white. 
For the black text not to be so hard on the white background I used a greyish tone to black (fontcolor: #191919)
To bring some life to the site a peachy-pink was used as accent color.
Color palette was created in: [https://color.adobe.com](https://color.adobe.com/create/color-wheel)

**Color Palette:**

![Color palette](/static/readme_images/color_palette.png)


**Typography:**

Font used for the logo are based of two different ones: ['Syncopate'](https://fonts.google.com/specimen/Syncopate), (sans-serif)

And for the body: ['Alatsi'](https://fonts.google.com/specimen/Alatsi), (sans-serif)

![Logo](/static/readme_images/logo.png)


## Database

* SQLite was used in delevopment to store data
* PostgreSQL was used in production to store data

## Data Models

The app is built on two models; Post and Comment which allow users to comment to a post and links the comments to the user and the post. 
Djangos built in *Allauth* is used to manage users to login, logout and create account.

In the back-end Django admin panel, the admin can view displayed posts, search by *title* and *content* and filter posts by date_published.

Diagram was made in [DB diagram](https://dbdiagram.io/home) of the correlation between the models:

![Diagram](/static/readme_images/fashionews_database.png)


# Planning / Agile Management

I used the Github kanban board to create issues and user stories in the early development stages of this project and moved them across the board as I progressed. 
Link to [Github Project](https://github.com/viktoriamahrberg/fashion-news-board/projects/1)


![Github kanban board](/static/readme_images/todo_board.png)



## Features to be implemented in future:

As part of the agile planning and kanban board two user stories could definitely have been implemented but due to lack of time was not: **Search bar** and **Category dropdown menu**. 
I would consider these two as quite strong candidates for a good user experience.


# Technologies used

**Django** - The framwork the app is built on

**Django Allauth** - User authentication

**Bootstrap** - CSS library

**Claudinary** - To store static files and images

**Crispyforms** - To display forms

**Python** - To write functions and models

**Javascript** - To add some functionality to the html-page

**Github** - To store repo and plan the project

**Gitpod** - Development hosting platform

**Google Developer Tools** - For debugging and check responsiveness

**SQLite** - Database for development

**PostgreSQL** - Database

**Heroku** - As a development hosting platform

**Google Fonts** - As a font resource.

**TinyPNG** - Compress image file


# Testing


## Code Validation

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to validate CSS: Shows no errors

[Html Checker](https://validator.w3.org/nu) to test HTML: Shows no errors

[JSHint](https://jshint.com/) to test Javascript: Shows no errors

[PEP8 Validator](http://pep8online.com/) to test all Python files: Shows no erros

![PEP8 results](/static/readme_images/pep8_result.png)


## Performance testing

I run Lighthouse tool to check performance of the website. 

![Lighthouse](/static/readme_images/lighthouse.png)


## Automated Testing

- 'Title required' test in test_forms.py
- 'Post-list-view as home page' test in test_views.py

## Manual Testing

| Test | Expected Output | Passed
| ----------- | ----------- | ---- |
|  User loads the home page | All content loads without error both as logged in or logged out, navigation bar and content is fully responsive| [x]
| User loads the home page as signed in | Only Logout and Create Post links show in nav bar and all content loads and work as expected |  [x]
| User wants to Register | User is being prompt to fill in all fields if failing to do so as well as a long and uncommon password. Success message is shown below navbar |  [x]
| User loads the home page as logged out | Only Register and Login links show in nav bar and all content loads and work as expected |  [x]
| User clicks on a news-post | Full news-post shown on its own page |  [x]
| User enters a post they are *not* owner of | Full news-post page shown without Edit and Delete button |  [x]
| User enters a post they are owner of | Full news-post page shown *with* Edit and Delete button |  [x]
| User clicks on Edit button | Site redirects user to "Edit" page |  [x]
| User loads the Edit page | Original content is prepopulated in the edit form, user can make edits and save changes and is then being taken back to the full news-post page |  [x]
| User tries to leave fields in the Edit form empty | Form can not be submitted and user is being prompted to enter data |  [x]
| User clicks on Delete button | Site redirects user to 'Delete' page |  [x]
| User loads the Delete page | User is being asked if they are sure they want to delete post, and if they proceed site redirects them to home-page and post is deleted. |  [x]
| User clicks on 'Original News Link' at bottom of post | New window opens and takes user to the original news article |  [x]
| User clicks on FASHIONEWS logo | User is redirected to HOME page  |  [x]
| Signed in user clicks on Create Post in nav-bar | User is being redirected to Create Post where user must fill out all fields or is being prompt to fill out all fields. When user save post they are being redirected to the newly created post |  [x]
| Signed in user wants to comment to post | 'Leave a Comment' field is shown on full news-post page and signed in can leave a comment that is being published on the same page. After a flash message is shown and automatically dismissed that the comment was posted. |  [x]
| Logged user wants to comment to post | 'Leave a Comment' field is not showing |  [x]
| Signed in user wants to comment to post | 'Leave a Comment' field is shown on full news-post page and signed in can leave a comment that is being published on the same page |  [x]


## User stories testing

### User

- As a **user** I want to **register an account**
    - When landing on the home-page user can click on "Register" in order to create an account. User needs to enter username, email (optional), password and reconfirm password. User is after this thrown a success-message of a successfull registration.
- As a **user** I want to **see all available news on the frontpage** 
    - All users can view all news-posts on home page and click for further reading.
- As a **user** I want to **make posts**
    - As a logged in user, user can create posts.
- As a **user** I want to **add photos as well as text to my posts**
    - As a logged in user "Create Post" is shown in navbar with a form to to create a post. The user has to provide a title, excerpt and content and original news-source link. Author is being automatically added as the logged in user. Images are optional and if not adding an image a default image will be provided.
- As a **user** I want to **receive flash messages after my actions**
    - Flash messages are shown to user when logging in, creating account, signing out of account and sucessfully commenting on a post. 
    - Messages are shown above input fields if user fails to provide the right information when creating an account or logging in.
- As a **user** I want to **see when the news post was posted**
    - Date and time of posting is shown on post summary on homepage as well as detailed post view.
- As a **user** I want to **click on a post**
    - Posts on home page is clickable and will take user to a detailed news-post for further reading.
- As a **user** I want to **see a link to the original post** 
    - At the bottom of the detailed news-post a link to the original article is provided.
- As a **user** I want to **comment on a news post** 
    - As a logged-in user the Leave-a-Comment field is shown under each post and user can comment.

### Admin

- As a **site admin** I want to **delete inappropriate users or users who spread fake news** 
    - In the back-end admin panel, admin can delete users, posts and comments.


## Further testing

Throughout development of this site the Google Inspect function has been used and cross-tested on different screens for responsivness. 


## Issues found during site development


1. **ISSUE:** Add custom color to toggle navbar

**FIX:** Change the 'rgba' in the background image URL:

`.navbar-toggler-icon {
    background-image: url("data:image/svg+xml;charset=utf8,%3Csvg viewBox='0 0 32 32' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath stroke='rgba(184, 120, 105, 1)' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 8h24M4 16h24M4 24h24'/%3E%3C/svg%3E");
}
`

![Navbar-toggler](/static/readme_images/navbar-toggler.png)


2. **ISSUE:** URL path from `<button>` on index.html to delete_post.html or edit_post.html not working 

**FIX:** Change from `<button>` to `<a href="">` made the url path work correctly


3. **ISSUE:** Wrong path by having `<slug>` in the beginning: `path('<slug>/delete_post/..` created an error.

**FIX:** Change the path with the slug in the end of the url `path('/delete_post/<slug>..` 

4. **ISSUE:** Several templating issues due to commented out comments

**FIX / LESSON LEARNED:** Templating language can't be commented out - it will still be read if there is an error in the out-commented code. 

5. **ISSUE:** When adding a post and uploading an image *front-end* the default image appeared instead of the chosen uploaded image. 

**FIX:** Add `enctype="multipart/form-data` to `<form>`


## Deployment

The site was deployment in Heroku and followed instructions by Code Institutes - [Deployment Cheat Sheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf) and [Heroku CLI Devtips](https://drive.google.com/file/d/12vhufODDWL4TaaaObqxxOMSwp4Tt2PCY/view) from Code Institute due to no sync between Heroku and Github.

Heroku steps (after created account or logged in):
1. "Create new App"
2. Give the App a unique name and enter region
3. Click on "Create App"
4. Click on "Settings" on your new App Dashboard
5. Scroll down to Config Vars and add values and keys
6. Go to Deploy section tab and scroll down to Deployment Method. I connected to my Github pages and could thereafter linked to the Github repo.
7. Scroll down to Automatic and Manual Deploys sections. I clicked on Automatic Deployment so that my changes that I push to Github automatically updates in Heroku.
8. Then in the Manual Deploy section, press Deploy Branch
9. After project has been deployed successfully I clicked the View-button to see the program run in the terminal.

After working on the site: DEBUG = False was changed in settings.py and COLLECTSTATIC value was removed from Config Vars in Heroku. 
Manual deployment from Gitpod to Heroku is made with command: `git push heroku main` in CLI.


## Credits

* General help and improved learning from Stack Overflow and [Django Documentation](https://docs.djangoproject.com/en/4.0/) and Code Institute Slack community.

* [Stack Overflow - Show Edit button on owners post](https://stackoverflow.com/questions/69059272/only-show-edit-button-on-owners-posts-django) - Show edit-button only on owners post to allow editing (`{% if post.author == request.user %}`)

* [Bootstrap flash-messages](https://getbootstrap.com/docs/4.0/components/alerts/)

* [GeeksforGeeks - CreateView class-based-views](https://www.geeksforgeeks.org/createview-class-based-views-django/)

* [GeeksforGeeks - DeleteView class-based-views](https://www.geeksforgeeks.org/deleteview-class-based-views-django/)

* [Djangoproject - EditView class-based-views](https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-editing/)

* Summernote - to show on frontend [Codedevlib](https://www.codedevlib.com/article/steps-to-implement-djangos-integrated-rich-text-editor-summernote-32382)
