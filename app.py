import feedparser
from flask import Flask, render_template, flash, request,Markup
import pymysql
db = pymysql.connect("localhost", "root", "", "rssfeed")

app= Flask(__name__)
#api = Api(app)
app.secret_key = 'my unobvious secret key'
BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"
CNN_FEED = "http://rss.cnn.com/rss/edition.rss"
FOX_FEED = "http://feeds.foxnews.com/foxnews/latest"
IOL_FEED = "http://www.iol.co.za/cmlink/1.640"

@app.route("/",methods=['GET','POST'])
def get_news():
    select=1
    feed=''
    articles=''
    cursor = db.cursor()
    sql = "SELECT * From Channel"
    cursor.execute(sql)
    
    channelTup = cursor.fetchall()
    data = [list(t) for t in channelTup]
    print(data)
    if request.method == 'POST':
        select = request.form.get('comp_select')

        #if(select=="BBC"):
        print(select)
        print(type(select))
        
        feed = feedparser.parse(data[int(select)-1][2])
        #print(len(feed))
        size = 0
        articles = feed['entries']

        if(int(select)!=3):
            print(len(feed))
            while (size < len(feed)):
                #print(feed['entries'])
                first_article = feed['entries'][size]
                title = first_article.get("title")
                published = first_article.get("published")
                summary = first_article.get("summary")
                flash(title,'title')
                size+=1
        if(int(select)==3):
            print(len(feed))
            while (size < len(feed)-2):
                #print(feed['entries'])
                first_article = feed['entries'][size]
                title = first_article.get("title")
                published = first_article.get("published")
                summary = first_article.get("summary")
                flash(title,'title')
                size+=1
        
        
        
        
        '''
        if(select=="CNN"):
            feed = feedparser.parse(CNN_FEED)
            #print(len(feed))
            size = 0
            articles = feed['entries']
            
            while (size < len(feed)):
                first_article = feed['entries'][size]
                title = first_article.get("title")
                published = first_article.get("published")
                summary = first_article.get("summary")
                flash(title,'title')
                size+=1
        
        if(select=="FOX"):
            feed = feedparser.parse(FOX_FEED)
            print(len(feed))
            size = 0
            articles = feed['entries']
            

            while (size < len(feed)-2):
                print(size)
                first_article = feed['entries'][size]
                title = first_article.get("title")
                published = first_article.get("published")
                summary = first_article.get("summary")
                flash(title,'title')
                size+=1
        '''    
        if(select==4):
            feed = feedparser.parse(IOL_FEED)
            print(len(feed))
            size = 0
            articles = feed['entries']
            
            while (size < len(feed)-2):
                print(size)
                first_article = feed['entries'][size]
                title = first_article.get("title")
                published = first_article.get("published")
                summary = first_article.get("summary")
                flash(title,'title')
                size+=1

        
    #return render_template("hello.html",page_title="News headlines",data=[{'name':'BBC'}, {'name':'CNN'}, {'name':'FOX'},{'name':'Independent Online'}],articles=articles,select=select)
    select = data[int(select)-1][1]
    return render_template("hello.html",page_title="News headlines",data=data,articles=articles,select=select)
if __name__ == "__main__":
    app.run(port=5000, debug=True)