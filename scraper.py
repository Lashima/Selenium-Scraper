from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver
def get_videos(driver):
  YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'
  driver.get(YOUTUBE_TRENDING_URL)
  video_div_class='ytd-video-renderer'
  videos = driver.find_elements(By.CLASS_NAME, video_div_class)
  return videos

def parse_video(video):
  title_tag = video.find_elements(By.ID, 'inline-title-icon')
  title = title_tag.text
  url = title_tag.get_attribute('href')
  thumbnail_tag = video.find_elements(By.TAG_NAME, 'img')
  thumbnail_url = thumbnail_tag.get_attribute('src')
  channel_div = video.find_elements(By.CLASS_NAME, 'ytd-channel-name')
  channel_name = channel_div.text
  description = video.find_elements(By.ID, 'description-text').text
  return {
    'title': title,
    'url': url,
    'thumbnail_url': thumbnail_url,
    'channel': channel_name,
    'description': description
  }
if __name__ == "__main__":
  print('Creating driver')
  driver = get_driver()
  print('Fetching trending videos')
  videos = get_videos(driver)
  
  print(f'Found {len(videos)} videos')
  print('Parsing top 10 videos')
  videos_data = [parse_video(video) for video in videos[:10]]
  print('videos_data',)