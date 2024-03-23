from icrawler.builtin import GoogleImageCrawler


google_crawler = GoogleImageCrawler(storage={'root_dir': 'C:/Users/noobi/PycharmProjects/UniversityDegree/neural_network/roten'})

google_crawler.crawl(keyword="rotten tomato", max_num=150)