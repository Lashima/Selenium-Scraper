import requests
from bs4 import BeautifulSoup

YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'

print('hellooo u')

response = requests.get(YOUTUBE_TRENDING_URL)
print('status',response.status_code)
#print('output',response.text[:1000])
with open('trending.html', 'w') as f:
  f.write(response.text)

soup = BeautifulSoup(response.text,'html.parser')
print('page title',soup.title.text)

#find all video divs
video_divs = soup.find_all('div',class_='ytd-video-renderer')

print(f'Found {len(video_divs)} videos')