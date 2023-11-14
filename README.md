# Simple Scraping Project
***
This is a simple scraping spider, using Scrapy and Python.
In this project, we scrape the following page and extract the first table, which
contains the GPD of the all the counties in 2022   
`https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)`


# Configuration
***
- Create a venv using `python3 -m venv venv`
- activate venv using `source venv/bin/activate` on Mac or `venv\Scripts\activate.bat` on Windows
- install Scrapy using `pip install scrapy`
- create a new project using `scrapy startproject <project_name>` which in our case is `scrapy startproject countries_gdp`
- go to the project directory using `cd countries_gdp`
- create a spider using `scrapy genspider <spider_name> <url>` which in our case is `scrapy genspider gdp https://en.wikipedia.org/`

and that's it, you are ready to go. whenever you want to run the project use `scrapy crawl <spider_name>` which in our case is `scrapy crawl gdp`.  
If you want to store the result in a separate file you can use `scrapy crawl gdp -O <file_name>.<file_extension>` which in our case is `scrapy crawl gdp -o gdp.csv`   
In this project, we store the final result in SQLite database, so if you don't export the data, that's fine.   

# Project Structure
***
The project structure is as follows:
- `gdp.py` is the main file which contains the spider
- `items.py` is the file which contains the model of the data we want to scrape
- `pipelines.py` is the file which contains the pipeline of the project

You can find sufficient comments inside the project files to understand the code.