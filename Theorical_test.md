Theorical test answers:

1: The main challenges i see are rate-limit, IP block and protected content. i have never collected data from those big companys before, so i don't know which particular challenge i might encounter, but i believe that no block is impossible to bypass
2: Data Mining in my understanding is when you have a huge amount of data to collect from. With this data in hand, you can see what's the target for the marketing, who have better results in certain marketing actions, and most importantly, help the ones with bad results.
3: For web-scraping twitter i used snscraper lib to get the user and post data and use that data to make my own report.  I also web-scraped iFood, and the main challenge is because ifood html is highly responsive and changes with every minimal action you make on the screen and change the way it delivery the data, so i created a bot that capture everything on the screen before scroll-down and put everything on a database to use it later.
4: HTTP is a protocol to get resources like HTML documents, it's the foundation of any data exchange on the Web where clients and servers communicate by exchanging message via requests and responses.
5: Proxies servers are used to change your IP and/or location. That way you can bypass some blockages you can encounter while web-scraping huge amounts of data in protected sites.
6: While all of then work with data, Data science focuses on managing, processing and interpreting data to make better decisions. Machine learning is an algorithm that analyze data and learn from it. AI requires a continuous feed of data to learn and improve decision-making
7: Feature engineering is a machine learning technique that leverages data to create new variables that aren't in the initial training set. It's important because it can produce new features for supervised and unsupervised learning, simplifying and speeding up data transformations while also enhancing accuracy
8: A data scientist cleans and analyzes data, answers questions, and provides metrics to solve business problems. A data engineer, on the other hand, develops, tests, and maintains data pipelines and architectures, which the data scientist uses for analysis.
9:
    - step 1: create a web-scrap to collect data from the influencers and save it on the database
    - step 2: create a schedule to update and compare new and old data from time to time
    - step 3: create a auto-clean bot that delete data from influencers that i'm not aiming at
    - step 4: create a dashboard to better vizualize all that data and use it for AI or Machine Learning

answer of Pratical test:
    Mean of tweets per day, because it reflect how often the user use and post on the social media, which indirectly tells us how much time he spends in the social media.