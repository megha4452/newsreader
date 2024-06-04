import feedparser
import streamlit as st

st.title("WELCOME TO YOUR DAILY DOSE OF NEWS DIGEST")

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://wallpaperaccess.com/full/1567831.jpg")
    }
    </style>
    """,
    unsafe_allow_html=True
)


#st.title("LET'S GO...")
my_range=range(1,21)
user_wants_read_number_of_articles= st.sidebar.select_slider("Select number of articles per source",options=my_range,value=5)
search_choice = st.sidebar.selectbox('Search By Category:', options=['Top Stories',
                                                            'Entertainment',
                                                            'Technology',
                                                            'Sports',
                                                            'Business & Finance',
                                                            'Health','Videos',], index=0)


def rss_feed_url(url):

        """given an RSS feed url, extract it's entities"""

        rss_feed_contents = feedparser.parse(url)
        news = rss_feed_contents.entries
        
    
        for idx, curr_news in enumerate(news):
            id = str(idx+1)
            #val = curr_news['pubDate']
            summ = curr_news.summary
           # st.write(f"{curr_news}")
            title = curr_news['title']
            article_published_at = curr_news.published
            actual_link = curr_news['link']
        #cat = curr_news['pubDate']
            content = curr_news['summary'].split('<')[0] if curr_news['summary'].split('<')[0] != '' else 'No article summary available, click on the link to read'
       # pdate = curr_news['pubDate']
            st.header(f"\n({id}) {title}")
            st.write(f"{article_published_at}")
            st.write(f"{content}")
            #st.write(f"{summ}")
            st.write(f"Read full story here: {actual_link}")
        #st.write(f"\n({id}) {title}\n02. News source: {actual_link}\n03. News Summary: {content}")
            st.write("---------------------------------------------------------")


            if idx>user_wants_read_number_of_articles-2:
                break
if search_choice == 'Top Stories':
    #-------------------------------------------------------------------------------------------------------------
    search_choice_sub = st.sidebar.selectbox('Search By Category:', options=['India',
                                                            'World-wide','Karnataka',], index=0)

    if search_choice_sub == 'India':
            dict_rss_news_feeds = { 'NDTV - India': "https://feeds.feedburner.com/ndtvnews-india-news"}
                 

            for channel, webpage in dict_rss_news_feeds.items():
              st.title(f"Your News from {channel}: \n")
              rss_feed_url(webpage)
              print("###########################################################################")
    if search_choice_sub == 'World-wide':
            dict_rss_news_feeds = { 'Times of India': "https://timesofindia.indiatimes.com/rssfeedstopstories.cms",
                                    'NY Times': "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
                                    'Science Daily':"https://www.sciencedaily.com/rss/all.xml"}
                                    
            for channel, webpage in dict_rss_news_feeds.items():
              st.title(f"Your News from {channel}: \n")
              rss_feed_url(webpage)
              print("###########################################################################")
    if search_choice_sub == 'Karnataka':
            dict_rss_news_feeds = {'OneIndia':"https://kannada.oneindia.com/rss/feeds/oneindia-kannada-fb.xml",
                                   'News18':"https://kannada.news18.com/commonfeeds/v1/kan/rss/breaking-news.xml",
                                   'Hindustan Times':"https://kannada.hindustantimes.com/rss/karnataka"}
                 

            for channel, webpage in dict_rss_news_feeds.items():
              st.title(f"Your News from {channel}: \n")
              rss_feed_url(webpage)
              print("###########################################################################")

    

        

if search_choice == 'Entertainment':
   

    dict_rss_news_feeds = { 'TOI -Entertainment': "https://timesofindia.indiatimes.com/rssfeeds/1081479906.cms",
                            'Hindustan Time':"https://kannada.hindustantimes.com/rss/entertainment",
                           'News nation':"https://english.newsnationtv.com/newsnation-rss/35",
                            'CNN - Entertainment': "http://rss.cnn.com/rss/edition_entertainment.rss",
                            'Hollywood - Life':"https://hollywoodlife.com/feed/",
                            'Zee News Entertainment':"https://zeenews.india.com/rss/entertainment-news.xml"}
                 


    for channel, webpage in dict_rss_news_feeds.items():
        st.title(f"From {channel}: \n")
        rss_feed_url(webpage)
        print("###########################################################################")

if search_choice == 'Sports':
   

    dict_rss_news_feeds = { 'Hindustan Times':"https://kannada.hindustantimes.com/rss/sports",
                             'Zee Sports': "https://zeenews.india.com/rss/sports-news.xml",
                            'Fox Sports':"https://api.foxsports.com/v1/rss?partnerKey=zBaFxRyGKCfxBagJG9b8pqLyndmvo7UU",
                            'Rot Wire':"https://www.rotowire.com/rss/articles.php"}
                 


    for channel, webpage in dict_rss_news_feeds.items():
        st.title(f"From {channel}: \n")
        rss_feed_url(webpage)
        print("###########################################################################")

if search_choice == 'Business & Finance':
   

    dict_rss_news_feeds = { 'Economic Times': "https://economictimes.indiatimes.com/wealth/rssfeeds/837555174.cms",
                            'India Times':"https://economictimes.indiatimes.com/news/economy/rssfeeds/1373380680.cms",
                            'Money Control':"https://www.moneycontrol.com/rss/economy.xml"}
                 


    for channel, webpage in dict_rss_news_feeds.items():
        st.title(f"From {channel}: \n")
        rss_feed_url(webpage)
        print("###########################################################################")

if search_choice == 'Technology':


    dict_rss_news_feeds = { 'NY -Technology': "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
                            'CNBC Tech':"https://www.cnbc.com/id/19854910/device/rss/rss.html",
                            'Wired Tech':"https://www.wired.com/feed/rss"}
    for channel, webpage in dict_rss_news_feeds.items():
        st.title(f"From {channel}: \n")
        rss_feed_url(webpage)
        print("###########################################################################")

if search_choice == 'Health':


    dict_rss_news_feeds = { 'Health News': "http://rssfeeds.webmd.com/rss/rss.aspx?RSSSource=RSS_PUBLIC",
                            'Medical Xpress':"https://medicalxpress.com/rss-feed/",
                            'Science Daily':"https://www.sciencedaily.com/rss/top/health.xml"}
    for channel, webpage in dict_rss_news_feeds.items():
        st.title(f"From {channel}: \n")
        rss_feed_url(webpage)
        print("###########################################################################")

if search_choice == 'Videos':


    dict_rss_news_feeds = {'NDTV':"https://feeds.feedburner.com/ndtv/latest-videos",
                            'Hindustan Times':"https://kannada.hindustantimes.com/rss/videos"}
    for channel, webpage in dict_rss_news_feeds.items():
        st.title(f"From {channel}: \n")
        rss_feed_url(webpage)
        print("###########################################################################")




