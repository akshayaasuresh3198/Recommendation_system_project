# Recommendation_system_project

This project aims at predicting the products for a given user and recommending them what similar products they would prefer to buy, taking into consideration the sentiment exhibited by the existing users.
* A user interface is built to input the user name present in the dataset and obtain top 5 products that would be recommended to the user.
* Product reviews and titles are combined to build various ML models that predict the sentiment(positive/negative), out of which the best performing model is found.
* User-user and item-item recommendation systems are built and evaluated to choose the one with low rmse score.
* Combining the chosen ML model and recommendation system, a final model is built.
* To deploy the model in heroku , app.py file is used as an interface between frontend web page and the backend model.
* Below is the link to view the final project deployed in heroku:
https://deploy-recommendation.herokuapp.com/
