rm .gitignore
git remote remove origin

heroku login
echo "Please enter the name of the app (on heroku)"
read NAME
heroku git:remote -a $NAME

echo "Please enter your token"
read TOKEN
echo "$TOKEN" > token.txt

git add .
git commit -m "Adding token and removing gitignore"
git push heroku master --force
