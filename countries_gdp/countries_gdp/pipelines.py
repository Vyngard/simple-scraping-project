from scrapy.exceptions import DropItem
import sqlite3

# if item is still not a float (even after applying all the changes in items.py), we drop the item
class CountriesGdpPipeline:
    def process_item(self, item, spider):
        if not isinstance(item["gdp"], float):
            raise DropItem("Missing GDP Value. Item Excluded")

        return item


# for saving the final data into database
class SavedToDatabasePipeline:
    def __init__(self):
        self.con = sqlite3.connect("countries_gdp.db")
        self.cur = self.con.cursor()

    # it is called everytime the spider is open - we check the table exists, if not we create it
    def open_spider(self, spider):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS countries_gdp 
                            (country_name TEXT PRIMARY KEY, 
                            region TEXT, 
                            gdp REAL, 
                            year INTEGER)
                            """)
        self.con.commit()

    #  add each item to the table
    def process_item(self, item, spider):
        self.con.execute("""INSERT INTO countries_gdp (country_name, region, gdp, year) VALUES (?, ?, ?, ?)""",
                         (item["country_name"], item["region"], item["gdp"], item["year"]))
        self.con.commit()

    def close_spider(self, spider):
        self.con.close()


# for checking if there are duplicate countries, and if so, drop the item
class NoDuplicateCountryPipeline:
    def __init__(self):
        self.country_seen = set()

    def process_item(self, item, spider):
        if item["country_name"] in self.country_seen:
            raise DropItem("Duplicate Country Name Found. Item Excluded")
        else:
            self.country_seen.add(item["country_name"])
            return item
