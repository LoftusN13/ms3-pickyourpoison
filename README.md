<p align="center"><img src="static/images/logo.jpg" width="60%"/></p>

# <p align="center">**MS3: Pick Your Poison**</p>

 ### View the live project [here.]()

This website has been created as my submission for Milestone Project 3 for the Code Institute. *Pick Your Poison* is a collaborative cocktail recipe site designed to allow users to search for and discover new cocktails as well as sharing their own recipes. Users can create an account which allows them to upload and edit their own cocktails. Non-members can also search for and browse the cocktail recipes. The site is designed to be user-friendly and visually appealing while also being responsive across a range of devices.

---

## Contents
- [**User Experience (UX)**](#ux)
    - [Strategy](#strategy)
        - [Target Audience](#target-audience)
        - [User Stories](#user-stories)
        - [Site Owner Goals](#site-owner-goals)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Surface](#surface)
 - [**Features**](#features)
 - [**Technologies Used**](#technologies-used)
    - [Languages](#languages)
    - [Technologies](#technologies)
 - [**Testing**](#testing)
 - [**Deployment**](#deployment)
 - [**Credits**](#credits)
    - [Content](#content)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

---
## <p align="center">**UX**</p>

### **Strategy**
#### Target Audience
The target audience for this site would be adults who have a keen interest in mixology, from beginners looking to learn how to make their first cocktail, to professionals on the search for new and exciting recipes.

#### User Stories
All Users
- As a user, I want to easily navigate through the site.
- As a user, I want the site to be responsive on whichever device and/or browser I'm viewing it on.
- As a user, I want to easily contact the site owners with any questions I might have or problems I may encounter.
- As a user, I want to search for and browse different cocktail recipes.

First-Time User/Non Member
- As a first-time user, I want to immediately understand the purpose of the site.
- As a first-time user, I want to easily create an account if I choose to do so. 

Registered Users
- As a registered user, I want to easily log in with my username and password.
- As a registered user, I want to easily create my own cocktail recipes.
- As a registered user, I want to easily edit or delete my own cocktail recipes.
- As a registered user, I want to easily view and edit my profile
- As a registered user, I want to easily log out from my account.
- As a registered user, I want visual confirmation of any task performed.

Admin User
- As the admin, I want to be the only user who can add or edit cocktail categories.


#### Site Owner Goals
- Create a site that is appealing and useful to encourage users to create an account and upload new cocktail recipes.
- Build up a large database of cocktail recipes via new users.

### **Scope**
For all Users: 
- The site must be fully responsive across different devices and browsers.
- The site must be visually appealing and consistent to ensure the user is comfortable.
- A *fixed navigation bar* must be included to allow users to easily navigate throughout the site.
- A clear way of contacting the site owners must be provided via a *contact form*.
- A clear and simple means of searching for and browsing cocktail recipes must be provided via a *search bar*.
- Cocktail recipes should be divided into categories to allow users to more easily find what they are looking for.

For First-Time Users/Non-Members: 
- Clear information about the purpose of the site must be provided.
- A clear and simple means of creating an account must be provided.

For Registered Users:
- Clear and simple means of:
    - logging into their account,
    - creating a new cocktail recipe, 
    - editing or deleting their recipes, 
    - viewing and editing their profile, 
    - and logging out of their account must be provided.
- Visual confirmation of tasks performed must be provided.

For Admin:
- A clear and simple means of adding and/or editing cocktail recipe categories.

### **Structure**
The structure of the site varies slightly depending on who the user is. All users will see the same fixed navigation bar, with some differing page options, and footer across the site. The colour and design is also consistent across all pages of the site.

#### Navigation Bar
- For All Users:
    - Will contain clear names of each site page for navigation ease; Home, Recipes (which is a dropdown item with links to the different cocktail categories), Register and Log In.
    - Will contain the site logo which acts as a link to the *Home* page.
    - Will remain consistent throughout the site.
    - Will turn into a collapsible menu on smaller devices for a cleaner design.

- For Registered Users (when logged in):
    - Will contain clear names of each site page for navigation ease; Home, Recipes (which is a dropdown item with links to the different cocktail categories), New Recipe, Profile and Log Out.

- For Admin (when logged in):
    - Will contain clear names of each site page for navigation ease; Home, Recipes (which is a dropdown item with links to the different cocktail categories), New Recipe, Categories, Profile and Log Out.

#### Footer
- Will remain consistent throughout the site.
- Will contain links to various social media platforms.
    - As the site owner does not yet have social media accounts, these links will bring the user to the main social media platform rather than to a particular account.
- Will contain a link which brings the user to a contact form if they wish to contact the site owner ("Contact Us Here!").

#### Home Page
- This page will be the same for all users, content-wise, whether they are a member or not.
- A quick introduction to the site will be provided.
- A *search bar* will be available, allowing users to search for a particular cocktail or ingredient, including a *button* to clear their search and another to perform the search.
- A link to all cocktail recipes will be clearly displayed.
- A link inviting first-time users/non-members to create an account will be clearly displayed, which also tells them what extra features they can use by being a member (*"Create an Account to add and edit your own recipes"*).

#### Recipes Page
- A *search bar* will be available, allowing users to search for a particular cocktail or ingredient, including a *button* to clear their search and another to perform the search.
- Will contain card panels of each cocktail category (*Vodka, Gin, Rum, Whiskey, Tequila, Variety* and *Non-Alcoholic*).
- Upon clicking a particular card panel, *Rum* for example, the user will be brought to all cocktails in the *Rum* category.
    - A *search bar* will be available, allowing users to search for a particular cocktail or ingredient, including a *button* to clear their search and another to perform the search.
    - A link will be clearly available allowing the user to return to all categories.
    - Each cocktail recipe will be available as a clickable card panel with its name and image clearly seen. 
    - Any cocktail recipe uploaded by the logged in user will have *buttons* to *Edit* and/or *Delete* the recipe.

#### Register Page
- Will contain a form to be filled out to register with fields for *Username*, *Email*, *Password* and a *Submit* button.
- Will contain a link to the *Log In* page for users who are already registered ("Already Registered? Log In Here").

#### Log In Page
- Will contain a form to be filled out to log in with fields for *Username*, *Password* and a *Submit* button.
- Will contain a link to the *Register* page for users who have not yet made an account ("Don't Have An Account? Register Here").

#### Profile Page
- Will only be available to Registered Users.
- Will display the user's Name and Username.
- Will display their own uploaded cocktail recipes.

#### New Recipe Page
- Will only be available to Registered Users.
- Will contain a form to be filled out to complete the cocktail recipe with fields for *Name*, *Choose Main Alcohol* (dropdown selector), *Ingredients, Steps*, *Image URL* and a *Submit* button.

#### Categories Page
- Will only be available to Admin.
- Will display all current cocktail recipe categories.
- Will contain buttons for *Edit* and *Delete* of each category.
- Will contain a button to *Add New Category*.

#### New Category Page
- Will only be available to Admin.
- Will contain a form to be filled out to add the new category with fields for *Category Name*, *Image URL* and a *Submit* button.

#### Contact Page
- Will be accessible via a link in the footer across all site pages.
- Will contain a contact form for the user to fill out with fields for *Name*, *Email Address*, *Your Message* and a *Submit* button.
- Once the form is submitted, the user will receive an automated reply to the email address that they entered to confirm their message has been received.
- Will contain links to various social media platforms.
    - As the site owner does not yet have social media accounts, these links will bring the user to the main social media platform rather than to a particular account.

### **Skeleton**
All wireframes were created using [Balsamiq](https://balsamiq.com/).

#### Mobile
![Mobile Wireframes](documentation/wireframes/mobile.png)

#### Tablet
![Tablet Wireframes](documentation/wireframes/tablet.png)

#### Desktop
![Desktop Wireframes](documentation/wireframes/desktop.png)

All wireframes can be found below;
- [Mobile Wireframes](documentation/wireframes/mobile)
- [Tablet Wireframes](documentation/wireframes/tablet)
- [Desktop Wireframes](documentation/wireframes/dekstop)

### **Surface**
#### Design

#### Colour

#### Imagery

---
## <p align="center">**Features**</p>

---
## <p align="center">**Technologies Used**</p>
### **Languages**

### **Technologies**

---
## <p align="center">**Testing**</p>

---
## <p align="center">**Deployment**</p>

---
## <p align="center">**Credits**</p>
### **Content**
### **Code**
### **Acknowledgements**