# Cakelicious
## A brand of bake ware

An application which stores recipes for cakes.
The site allows users to search for and browse cake recipes, and  to create a user account so that they can add, edit and delete their own recipes.
The website promotes branded bake ware required for the recipes to its users, and provides accessible links to make online purchases.

Business goals:
* Build brand awareness.
* Create a positive brand image.
* Associate brand with real bakers; brand is credible and trustworthy.
* Encourage users to purchase products from Cakelicious.
* Provide excellent UX to keep users returning to the site for all their baking needs.

Customer goals:
* To easily search for recipes to cook.
* To find inspiration for baking.
* An online cookbook/database which they can add to via a user account.
* Clear and easy to use website.

## UX

#### The Client
##### The ideal client for this website is:
* A baking enthusiast.
* Someone who bakes for a hobby.
* Someone who bakes professionally or regularly, such as a small bakery or cake shop, a stall holder, etc.
* Someone who identifies as a cook and wants to own the best kitchen tools for the purpose.
* Someone who is cooking a one-off special recipe for an occasion.

##### Visitors are searching for:
* Tried & tested recipes to cook.
* Baking inspiration.
* A database of recipes.
* A way to store and share recipes.

##### This app 
* Provides users with a database of reliable recipes tried and tested by other bakers.
* Users have the option to create an account and easily add their own creations to both store and easily access,
and to share with other baking enthusiasts, or to show off their creations.
* The site acts as an online cookbook- somewhere to search for and store recipes for now and for future use.
* Quick easy access to a database of recipes without having to register.
* Easy to navigate.
* Easy to add user’s own recipes.
* Easy access to purchase all and any tools required for baking projects.

##### User Stories:
* I want to search for recipes to cook, usually I know what I want to make and I’m looking for the best recipe.
* I want to browse recipes for inspiration.
* I am looking for a recipe for a special occasion, such as a birthday or other celebration.
* I want to be able to search for and find recipes which cater for particular dietary needs- I’m gluten intolerant/ vegan/
lactose intolerant/ on a diet, etc.
* I want one place I know can go to find a reliable recipe, and a wide selection of recipes.
* I want an app where I can store my recipes and recipes I like.
* I do not bake very often, so when I do I may need to buy equipment to help me cook, such as cake tins or mixers.
I don’t want to have to research this online, so a reliable brand is convenient.
* I bake often and so I like to have all the most up to date and high quality bake ware for my kitchen, including 
items to improve presentation and niche items.

## Features
* Search for recipes by keywords, ingredients and specific recipe titles.
* Browse all recipes.
* Register and Log in to the site.
* Registered users can create own recipes to add to the site, where they can be read by other users.
* Registered users can easily access their recipes to update and delete.
* Links to purchase Cakelicious equipment.
?? * Users can include a photo of the final product

## Desirable features for future implementation
* Easily share recipes to social media using the link to the specific recipe page, displayed as a thumbnail.
* Ability for users to rate recipes they have cooked and easily view a recipes ratings.
* Ability to search for recipes with a high rating.
* Ability for users to comment on recipes and read other’s comments on recipes.
* An internal shop, so that users can add equipment to their ‘basket’ when they are planning what to cook and make a purchase on the site.
* Ability to view a specific user’s recipe collection.
* Ability to store liked recipes in a user account for easy access.
* Email confirmation of Registration.


## Structure

### Database design:
* user: username, email, password
* recipe: name, description, equipment, ingredients, method, user[username], image, (to be added: rating/likes)

* homepage (browse and search)
* register
* login
* my recipes (user homepage)
* edit recipe

# Credits
homepage image Photo by Samuel Ramos on Unsplash https://unsplash.com/photos/QxudOE5_Xwo

### site
* nav bar
* colors
* title image
* font choice


### homepage
* header banner with search bar to search for recipes.
* all cake recipes displayed on the homepage for browsing.
* recipes displayed with card of image, cake name, user and decription. A drop down provides the ingredients, equipment and method.
* For simplicity and intuition, to read the recipe the user does not have to navigate away from the page.


## issues
added maxlength and minlength to recipe description input to ensure that page layout stays looking nice

how to make sure that when the text is displayed from the db it is formatted with paragraphs?

how to display recipes created by the session user from the database:
myrecipes = mongo.db.recipes.find({
    "user": session["user"]})
 
if you click logout when user already logged out, throws an error. fix this by removing logout option once user has logged out
