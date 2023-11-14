import re

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

# remove commas from gdp values
def remove_commas(value):
    return value.replace(",", "")

# try to convert value to float for gdp, otherwise return the value itself
def try_float(value):
    try:
        return float(value)
    except ValueError:
        return value

# try to convert value to int for year, otherwise return the value itself
def try_int(value):
    try:
        return int(value)
    except ValueError:
        return value

# using regex to extract year
def extract_year(value):
    year = re.findall(r"\d{4}", value)

    # if we don't have a year, return the value itself
    if not year:
        return value

    return year

class CountryGdpItem(scrapy.Item):
    country_name = scrapy.Field(
        input_processor=MapCompose(remove_tags,str.strip),  # remove html tags and possible spaces from input
        output_processor=TakeFirst()  # only the first value is returned
    )
    region = scrapy.Field(
        input_processor=MapCompose(remove_tags,str.strip),
        output_processor=TakeFirst()
    )
    gdp = scrapy.Field(
        input_processor=MapCompose(remove_tags,str.strip, remove_commas, try_float),
        output_processor=TakeFirst()
    )
    year = scrapy.Field(
        input_processor=MapCompose(remove_tags,str.strip, extract_year, try_int),
        output_processor=TakeFirst()
    )
