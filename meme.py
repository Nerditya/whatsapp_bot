import praw
from urllib.request import urlopen
from bs4 import BeautifulSoup

def image_extractor(url):
    htmldata = urlopen(url)
    soup = BeautifulSoup(htmldata, 'html.parser')
    images = soup.find_all('img')
    a=[]
    for item in images:
        a.append(item['src'])
    return a

    

# htmldata = urlopen('https://www.geeksforgeeks.org/')
# soup = BeautifulSoup(htmldata, 'html.parser')
# images = soup.find_all('img')
  
# for item in images:
#     print(item['src'])
reddit =praw.Reddit(client_id="lQ26Qy6_PfFP1heyITHLxw",
                    client_secret="3kySPFFxJauQoPd-dK0_1x-ld3RE5g",                  
                    user_agent="my user"
                    )
def memer():
    memes=[]
    # for submission in reddit.subreddit("meme").hot(limit=20):
    #     memes.append(submission.url)
    # for submission in reddit.subreddit("memes").hot(limit=20):
    #     memes.append(submission.url)
    for submission in reddit.subreddit("dankmemes").hot(limit=30):
        memes.append(submission.url)
    return memes 



def imgs(re):
    ims=[]
    for submission in reddit.subreddit(re).hot(limit=30):
        ims.append(submission.url)
    return ims

