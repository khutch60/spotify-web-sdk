# spotify-web-sdk
Spotify web SDK application using a Flask framework

The main goal of this project was to create a standalone spotify playback device to use alongside my turntable setup.  I used a raspberry pi 5 connected to a Pimoroni Inky Impression 5.7" e ink display to show the artist name and album artwork.  

Spotify's authorization code flow requires a user to physically sign in to retrieve an api access token.

![auth-code-flow](https://github.com/user-attachments/assets/3f5c13f8-8a06-4aaf-8b40-2e53ff640da2)

To get around this, I configured a selenium bot to log in automatically.  Once the access token is aquired, flask will run and the web player will initialize.  The access token expires every hour and needs to be refreshed with a special refresh token given alongside the initial access token.  This is handled via a Javascript fetch request which calls back to flask to retrieve a new access token.

Finally, I configured the program to autorun at startup.  All I need to do is power on the pi and the script handles everything by itself.  I can then connect with my phone and control playback and volume from it seemlessly.


