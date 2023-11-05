# Join.Connect.Network

# What are we doing here?
Our intention is to make it easier for people to connect with each other, anytime and anywhere. In every room you enter, you are likely to fall into a bucket with at least one person with similar interests to you. But unless you come across them, you might not know who they are. That’s where JCN steps in. Our users will be shown several others to connect with, based on a percentage overlap of their interests. If JCN thinks that you can network with a user, we’ll push them to the top. Our goal is to bring like-minded individuals together when they may never be able to find them. Make new connections anytime anywhere. Join. Connect. Network! Simple as that.


# What did we use?
Our tech stack comprises of technologies foreign and familiar to our team. Our team has specialties in some of our tech stack and some things new to us – challenges are always welcome here.


### Tech Stack:


Backend - Flask, IBM LinuxONE


Frontend - JS, HTML, CSS


Database - SQL


Machine Learning - Data Preprocessing, Feature Engineering and RandomForestClassifier
# How did we use all of this?
Our app greets you with a login and a profile creation page with our signature frontend styling pattern. Our backend uses a microservice laid foundation which handles the information you provide. As you enter your information the data gets sent to our database, connected to our flask server. The database then holds all the user provided information, along with their locational information (longitude and latitude). This is essential to figuring out the proximity of users to each other. The location is found through geofencing for a radius of 15 meters. The database then sends the data to our Machine Learning model which is in our IBM LinuxONE server. That’s where the magic happens! Our model uses your data and the data of other users in the database and finds the best matches possible. These matches, which comprise the match’s relevant information along with the interest overlap percentage, will then be sent to the original Flask server that is connected to the frontend. Our frontend will take the matches with over a 50% overlap and send those to you. And from there – you connect!


# What were the obstacles we faced?
As we said above, challenges are always welcome. As expected, they arose.
A couple of issues were faced while getting the ground running with our implementation of IBM LinuxONE. The first hurdle was hardware incompatibility with MacOS. Getting a Windows machine helped us solve this. Our unfamiliarity with the two services threw up some more hurdles for us. But with grit and wit our team managed to overcome them all.
Our unfamiliarity stemmed further with us facing some issues during integration. (add issues here). Nothing our team couldn’t manage. We couldn’t be stopped from helping you connect.


# What are we proud of?
Initially, it seemed like a daunting task, but our team was able to integrate our fairly complex tech stack and make JCN a reality. Adding on the complexity of all this, the fact that we did it in one day makes us well pleased. We are proud of how our team came together to build this project from the ground up and work together to make a project that would make a difference, helping people get closer.


# Where do we go from here?
This is just the beginning for JCN. Currently, our scope is limited to college students but we all start somewhere. We have a lot more in the pipeline that we plan on adding to JCN.
For now, JCN exists as a webapp. The next step is to make a mobile app. You may not take your computer everywhere, but your phone will probably be with you. A mobile app will help with making it more… mobile.
Now that we have helped you connect, we want to give you an option to communicate. That’s where our plan to implement a chat section. We want to help you network more through JCN.
We would like to fine tune our model further. Currently it gives equal weight to all the parameters. In the future, we would like to add weighted averages per the user’s choice so that certain preferences contribute more to the overlap percentage. Along the same lines, we would like to add more feature vectors so that we can get better matches. This would help us further broaden our user base by adding more options for the users to match based on their preferences.
