# Epithet Generator

This is a  basic flask Epithet Generator app.  It has multiple routes to input to get different results.  Based on the route you pass in it will provide a different result to the 4 different routes.

## Instructions

By passing in just the basic local host 5000 route it will return a random epithet to view on the page in jsonified form.  By passing /vocabulary it will return all the different words used by the program that is organized by three columns.  By passing in /epithets/(enter quantity here) it will return a random amount of epithets based of the actual quantity entered.  The final rout of /epithets/random will return a random amount of epithets between 1 and 25 epithets.

------------------------------------------------------

This is the basic introduction to a flask project.  This utilizes the flask, dotenv, and os libraries to run the server.