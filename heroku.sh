git clone https://codeberg.org/SnowCode/amongstars-discord
cd amongstars-discord
rm .gitignore
git remote remove origin

heroku login
read NAME
heroku git:remote -a $NAME
