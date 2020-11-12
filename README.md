Description:
- ExpressJS website that grabs your current location+season and displays what fruits are in season
- UI repository: https://github.com/themansbak/fruit-season-ui
    - Separation of frontend and backend
- API endpoint: https://stormy-reef-43017.herokuapp.com/
- UI: https://sheltered-hollows-41861.herokuapp.com/

Tasks:
- Mark:

- Alex:
    - optimize data storage of db_setup iterations
    Struggles:
    - issue deploying both frontend+backend servers to one heroku dyno
        - heroku dyno uses one specified port for both servers
        - tried adding a proxy key to the frontend package.json to use as endpoing for backend
            - didn't work
        - now going to separate into two repos and run both on separate heroku instances

Server:
- npm run dev

Server:
- npm init
- npm install dotenv --save
- npm install express --save
- npm install mongoose
- dev:  npm run dev
- start: npm start

Deployment:
- https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/Publishing_your_website
- https://www.codecademy.com/learn/deploy-a-website
- Heroku:
    - brew install heroku/brew/heroku
    - touch Procfile
    - echo "web: npm start" > Procfile
    - heroku ps:scale web=[#Dynos]
        - Dynos are basically lightweight containers that run whatever application command process
        - Start: heroku ps:scale web=1 
        - Stop: heroku ps:scale web=0
    - Check # dyno processes: heroku ps

Scraper:
- Utilizes python3 and virtual environment
    - https://docs.python.org/3/library/venv.html
- python3  -m ensurepip --default-pip
- pip install selenium
- pip install beautifulsoup4
- pip install webdriver-manager
- pip install lxml
- Driver:
    - Download chromedriver (my local version is 84)
    - Extract to /usr/local/bin 
        - May need to allow it inside Security and Privacy
- useful links
    - https://stackoverflow.com/questions/49939123/scrape-dynamic-contents-created-by-javascript-using-python
    https://stackoverflow.com/questions/26393231/using-python-requests-with-javascript-pages
    http://theautomatic.net/2019/01/19/scraping-data-from-javascript-webpage-python/
    https://sites.google.com/a/chromium.org/chromedriver/downloads

    - https://stackoverflow.com/questions/51126472/how-to-organise-file-structure-of-backend-and-frontend-in-mern#:~:text=The%20most%20basic%20structure%20would,your%20React%20side%20of%20things