# AnonymousMessageBoard

This global anonymous message board allows you to post a comment and see comments that other people have posted as well. 

Users can type in a comment and press submit to submit the comment and see other comments users on different computers have made. All comments no matter the user or computer is submitted to one message board. The messages are saved until the site is refreshed from the platform. Messages are displayed from most recently posted to least recently posted.

Users cannot submit an empty comment or a comment that has a profanity word in it in the list of words found in the home.html section of the code – if they try to, an error or alert will pop up and prevent them from submititng their comment. If a user types in a comment that exceeds more than 128 characters, the program will not allow more characters in the text box.

This app was made with a Flask blueprint to write the routes and post requests. All routes are written in the flask_app.py file. The formatting and restrictions on user input was done in HTML and JavaScript, and light styling was applied with CSS. All formatting and restrictions can be found in the home.html function in the templates folder, and this template is rendered with render_template in the flask_app.py file.

The message board can be accessed here: http://eunicekoo.pythonanywhere.com/. No other installations or building instructions are necessary, and this platform was chosen for that reason.
