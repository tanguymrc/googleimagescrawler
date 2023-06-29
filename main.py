import datetime 
from icrawler.builtin import GoogleImageCrawler

str_search = str(input("What are you looking for?\n")) # ask for search term
int_number = int(input("How many pictures do you want?\n")) # ask for number of pictures
str_type = str(input("What type do you want?\n")) # ask for type of pictures (“photo”, “face”, “clipart”, “linedrawing”, “animated”)
str_color = str(input("What main color do you want?\n")) # ask for main color of pictures (“color”, “blackandwhite”, “transparent”, “red”, “orange”, “yellow”, “green”, “teal”, “blue”, “purple”, “pink”, “white”, “gray”, “black”, “brown”)
str_size = str(input("What size do you want?\n")) # ask for size of pictures (“large”, “medium”, “icon”, or larger than a given size (e.g. “>640x480”), or exactly is a given size (“=1024x768”))

if str_type == "": # if no type is selected
    no_type = True
else: # if type is selected
    no_type = False
if str_color == "": # if no color is selected
    no_color = True
else: # if color is selected
    no_color = False
if str_size == "": # if no size is selected
    no_size = True
else: # if size is selected
    no_size = False

if no_type is True and no_color is True and no_size is True: # if no filter is selected
    filters = dict(date = ((2010, 1, 1), datetime.date.today())) # set filter to date
elif no_type is True and no_color is True and no_size is False: # if only size is selected
    filters = dict(size = str_size, date = ((2010, 1, 1), datetime.date.today())) # set filter to size and date
elif no_type is True and no_color is False and no_size is True: # if only color is selected
    filters = dict(color = str_color, date = ((2010, 1, 1), datetime.date.today())) # set filter to color and date
elif no_type is True and no_color is False and no_size is False: # if color and size are selected
    filters = dict(color = str_color, size = str_size, date = ((2010, 1, 1), datetime.date.today())) # set filter to color, size and date
elif no_type is False and no_color is True and no_size is True: # if only type is selected
    filters = dict(type = str_type, date = ((2010, 1, 1), datetime.date.today())) # set filter to type and date
elif no_type is False and no_color is True and no_size is False: # if type and size are selected
    filters = dict(type = str_type, size = str_size, date = ((2010, 1, 1), datetime.date.today())) # set filter to type, size and date
elif no_type is False and no_color is False and no_size is True: # if type and color are selected
    filters = dict(type = str_type, color = str_color, date = ((2010, 1, 1), datetime.date.today())) # set filter to type, color and date
else: # if all filters are selected
    filters = dict(type = str_type, color = str_color, size = str_size, date = ((2010, 1, 1), datetime.date.today())) # set filter to type, color, size and date

google_crawler = GoogleImageCrawler(feeder_threads = 1, parser_threads = 2, downloader_threads = 4, storage = {'root_dir': 'your_results'}) # set crawler
google_crawler.crawl(keyword = str_search, filters = filters, max_num = int_number, file_idx_offset = 0) # start crawler
print("Find your pictures in the folder 'your_results'!") # print message
