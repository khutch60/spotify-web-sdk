# spotify-web-sdk
Spotify web SDK application using a Flask framework

![20250509_003036](https://github.com/user-attachments/assets/c0edcec9-6aad-4bc4-aa18-3178a41bbc50)

The main goal of this project was to create a standalone spotify playback device to use alongside my turntable setup.  I used a raspberry pi 5 connected to a Pimoroni Inky Impression 5.7" e ink display to show the artist name and album artwork.  

Spotify's authorization code flow requires a user to physically sign in to retrieve an api access token.

![441986052-3f5c13f8-8a06-4aaf-8b40-2e53ff640da2](https://github.com/user-attachments/assets/3e683e8c-4540-4793-88d6-a9ce4881e405)


To get around this, I configured a selenium bot to log in automatically.  Once the access token is aquired, flask will run and the web player will initialize.  The access token expires every hour and needs to be refreshed with a special refresh token given alongside the initial access token.  This is handled via a Javascript fetch request which calls back to flask to retrieve a new access token.

Finally, I configured the program to autorun at startup.  All I need to do is power on the pi and the script handles everything by itself.  I can then connect with my phone and control playback and volume from it seemlessly.  

![Screenshot_20250509_002718_Spotify](https://github.com/user-attachments/assets/97ce1309-3ebd-4941-986b-6ab1d45b9298)


Whenever a new album plays, the screen will update showing the album art, album name, and artist name.

![20250509_003021](https://github.com/user-attachments/assets/f376e276-fbce-4bff-aa59-c7f1c529ff52)
