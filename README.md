

Live link [here](https://fashionews.herokuapp.com/)

# About

Fashionews is a blog-like news page where anyone can share their local news from the fashion industry. May it be about a new fashion school with focus on sustainability and social justice in your city or the cool concept store in your home-town now expanding to another city, share it! 
We can read about the big brands revenue and change of directors on a daily basis in the big newspapers - this is not about them -this is about supporting and sharing our local fashion-heros.


# UX

## User Goals

Users should be able to read about fashion news that are not in the big tabloids.

Signed in users should additionally be able to share news that happen locally to them and comment on others posts.

## Site Owner Goals

Site owner should be able to control users, posts and comments in case of violation of a safe community space.


## User Stories
- As a Site user I want to make posts so that I can share fashion news around me with the community.
- As a Site user I want to see all available news on the frontpage so that I can click decide on what I want to read more about.
- As a Site user I want to click on a news-post so that I can read the full news article.
- As a Site user I want to see a link to the original post so that I can see that the news is legit.
- As a Site user I want to to see when the news-post was posted so that I know when the news was from.
- As a Site user I want to search for a news-post so that I easily can navigate to a specific post.
- As a Site user I want to register an account so that I can create a news-post, comment and interact with other posts.
- As a Site user I want to receive flash messages after my actions so that I know if I successfully have processed my action.
- As a Site user I want to add photos as well as text to my posts in a userfriendly way so that I can make the posts more appealing with the images.
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

Full CRUD functionality is implemented for posting on the site.

## Wireframes

I made the wireframes in Figma:

**Home Page:**

![Home page](/static/readme_images/wireframe_home.png)

**Detailed Post Page:**

![Detailed Post page](/static/readme_images/wireframe_detailed_post.png)

**Mobile:**

![Mobile](/static/readme_images/wireframe_mobile.png)



## Design

I wanted to use a clear layout and color scheme for a serious news look and used Bootstrap as a toolkit with maincolors of black and white. 
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


# Planning / Agile Development

I used the Github kanban board to create issues and user stories in the early development stages of this project and moved them across the board as I progressed. 


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

## Functionality testing

## Code Validation

[W3C CSS](https://jigsaw.w3.org/css-validator/) Validator to validate CSS
[Html Checker](https://validator.w3.org/nu) to test HTML

## Performance testing

I run Lighthouse tool to check performance of the website. 

<!-- IMAGE -->




### Compatibility testing

### User stories testing


| Test | Expected Output | Passed
| ----------- | ----------- | ---- |
|  User loads the home page | All content loads without error both as logged in or logged out, navigation bar and content is fully responsive| [x]
| User loads the home page as signed in | Only Logout and Create Post links show in nav bar and all content loads and work as expected |  [x]
| User loads the home page as logged out | Only Register and Login links show in nav bar and all content loads and work as expected |  [x]
| User clicks on a news-post | Full news-post shown on its own page |  [x]
| User enters a post they are *not* owner of | Full news-post page shown without Edit and Delete button |  [x]
| User enters a post they are owner of | Full news-post page shown *with* Edit and Delete button |  [x]
| User clicks on Edit button | Site redirects user to "Edit" page |  [x]
| User loads the Edit page | Original content is prepopulated in the edit form, user can make edits and save changes and is then being taken back to the full news-post page |  [x]
| User tries to leave fields in the Edit form empty | Form can not be submitted and user is being prompted to enter data |  [x]
| User clicks on Delete button | Site redirects user to "Delete" page |  [x]
| User loads the Delete page | User is being asked if they are sure they want to delete post, and if they proceed site redirects them to home-page and post is deleted. |  [x]
| User clicks on 'Original News Link' at bottom of post | New window opens and takes user to the original news article |  [x]
| User clicks on FASHIONEWS logo | User is redirected to HOME page  |  [x]
| Signed in user clicks on Create Post in nav-bar | User is being redirected to Create Post where user must fill out all fields or is being prompt to fill out all fields. When user save post they are being redirected to the newly created post |  [x]
| Signed in user wants to create a comment to post | Leave a Comment field is shown on full news-post page and signed in can leave a comment that is being published on the same page |  [x]

<!-- | Signed in user wants to create a DELETE A COMMENT to post | Leave a Comment field is shown on full news-post page and signed in can leave a comment that is being published on the same page |  [x] -->

| User wants to Register | User is being prompt to fill in all fields if failing to do so as well as a long and uncommon password. Success message is shown below navbar |  [x]


ADMIN STORIES TO ADD 



### Issues found during site development


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

The site was deployment in Heroku and followed instructions by Code Institutes - [Deployment Cheat Sheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf)

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


## Credits

* [Stack Overflow - Show Edit button on owners post](https://stackoverflow.com/questions/69059272/only-show-edit-button-on-owners-posts-django) - Show edit-button only on owners post to allow editing (`{% if post.author == request.user %}`)

* [Bootstrap flash-messages](https://getbootstrap.com/docs/4.0/components/alerts/)

* [GeeksforGeeks - CreateView class-based-views](https://www.geeksforgeeks.org/createview-class-based-views-django/)

* [GeeksforGeeks - DeleteView class-based-views](https://www.geeksforgeeks.org/deleteview-class-based-views-django/)

* [Djangoproject - EditView class-based-views](https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-editing/)

* Summernote - to show on frontend [Codedevlib](https://www.codedevlib.com/article/steps-to-implement-djangos-integrated-rich-text-editor-summernote-32382)

 




Welcome Vikmah,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
