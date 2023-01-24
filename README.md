# TeamBitsAndBytes_NewsAggregator
It is a web application which aggregates data (news articles) from multiple websites. Then presents the data in one location.
link to the live website (hosted on heroku)->
https://newsatlasx.herokuapp.com/

So, our news aggregator works in 3 steps: 
A. It scrapes the web for the articles. (In this Django project, we are scraping websites called  Time of India and Outlook India.) 
B. Then it extracts the information we need from the articles. After this it stores our data in  the database. 
C. The stored objects in the database are served to the client. The client gets information in a  nice template.
To build web app with django, we install django on our system using pip install  command. 

After installation of django, We created a new Python Django project named  TeamBitsAndBytes_NewsAggregator. 
∙ django-admin startproject TeamBitsAndBytes_NewsAggregator 
Then, we created the app news in our project, in which web app will go live.  Django, has convention of keeping everything in separate app, inside a project. A  project can have multiple apps. So we need move into the project folder and create  the app. This is the command we used to create app.  
∙ python manage.py startapp news 
Then we add this news app to settings.py file in INSTALLED_APPS. So that, Django  takes this app into consideration. 
After this part we create template for our home page. 
We pass two variables namely toi_news and ot_news from our views.py file to the template with news of Times of India and Outlook India respectively and we  loop through them to print the news.  

We create a views.py file inside which we create news scrapper of both the news sites.  
When we were done with template and views creation, we add this view to our urls.py  file to serve the view. 
Then we need to open urls.py file from our project directory and there we need to import  news view and add this view to url. 
After this we are done with setting our Django server.

We run our web app from command window, using the command given below. ∙ python manage.py runserver 
After that, we open 127.0.0.1:8000 and we can see the homepage of our news aggregator  app. 


