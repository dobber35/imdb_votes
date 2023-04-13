import scrapy
from scrapy.crawler import CrawlerProcess
import csv

class VideoGameVotesSpider(scrapy.Spider):
    name = 'videogamevotes'
    
    start_urls = ['https://www.imdb.com/search/title/?title_type=video_game&release_date=2022-01-01,2022-12-31']
    
    def parse(self, response):
        for row in response.xpath('//*[@id="main"]/div/div[3]/div/div'):
            game_title = row.xpath('//*[@id="main"]/div/div[3]/div/div[1]/div[3]/h3/a/text()').extract_first()
            release_year = row.xpath('//*[@id="main"]/div/div[3]/div/div[1]/div[3]/h3/span[2]/text()').extract_first()
            votes = row.xpath('//*[@id="main"]/div/div[3]/div/div[1]/div[3]/p[4]/span[2]/text()').extract_first()
            yield {'game_title': game_title, 'release_year': release_year, 'votes': votes}
            
process = CrawlerProcess()
process.crawl(VideoGameVotesSpider)
process.start()

with open('video_game_votes_2022.csv', 'w', newline='') as csvfile:
    fieldnames = ['game_title', 'release_year', 'votes']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    with open('video_game_votes_2022.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            writer.writerow(row)



