# Along Among The Stars: Discord bot
> Find the original game [here](https://noroadhome.itch.io/alone-among-the-stars)

This is a Python Discord bot. 

## Building
1. Make sure you have Python3 and Python3-pip installed
2. Install the depedencies

```bash
pip3 install discord.py
```

3. Download this repository 

```bash
git clone https://codeberg.org/SnowCode/amongstars-discord
cd amongstars-discord
```

4. Create a file called `token.txt` in the main directory and paste your Discord token inside.
5. Run the script

```bash
python3 bot.py
```

### How to get the Discord token 
1. Create an application on Discord dev portal [here](https://discord.com/developers/applications)
2. Select `Bot` on the left menu and create one. 
3. Select `OAuth` on the left menu, check `Bot`, then check `Administrator`, then copy and open the link in your browser to add the bot to a server.
4. Go back on the `Bot` tab and copy the token on the top of the page. 

## Usage
| Command | Meaning |
| --- | --- |
| `>land` | Find a new planet and land on it | 
| `>discover` | Discover a new element of the planet |
| `>log <your entry>` | Add the description of the element and your feelings into the log |
| `>burn` | Burn your log |
| `>read` | Read your log |
