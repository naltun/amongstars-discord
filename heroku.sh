git clone https://codeberg.org/SnowCode/amongstars-discord
cd amongstars-discord
rm .gitignore
git remote remove origin

heroku login
read NAME
heroku git:remote -a $NAME

read TOKEN
echo "$TOKEN" > token.txt

git add .
git commit -m "Adding token and removing gitignore"
git push heroku master
