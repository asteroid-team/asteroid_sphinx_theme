# Install yarn
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt update
sudo apt install yarn

# Install npm
sudo apt install npm

# Install grunt
sudo apt install node-grunt-cli

# Fix some error I got..
npm install --save node-sass grunt-sass
npm install grunt-contrib-sass --save-dev
sudo npm install -g sass