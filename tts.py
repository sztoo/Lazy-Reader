import requests
from bs4 import BeautifulSoup 
from gtts import gTTS

base_url = "https://www.nytimes.com/2015/08/16/technology/inside-amazon-wrestling-big-ideas-in-a-bruising-workplace.html?_r=1"

def scrape(base_url): 
  r = requests.get(base_url)
  soup = BeautifulSoup(r.text, "html.parser")
  with open("tts.text", "w") as file: 
    for body in soup.find_all(class_="story-body-text"): 
      file.write(body.text)
        
def tts():
  f = open('tts.text', 'r')
  tts = gTTS(text=f.read(), lang='en-us')
  tts.save("output.mp3")
  f.close()

if __name__ == "__main__":
  scrape(base_url)
  tts()