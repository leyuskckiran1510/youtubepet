## Youtubepet
Code to scrape the celeb Instagram Feed and upload it to YouTube with proper thumbnails and video description.

## How to use
 clone this dir to your local device or Virtual servers
  

  -> Make a google project
  -> Add Youtube Data Api V3 in that project 
  #[CLICK HERE TO DOWNLOAD YOUR PROJECT JSON FILE](https://console.cloud.google.com/apis/api/youtube.googleapis.com/credentials)
  -> Now click  **_'+ Create credentials'_** button
  -> create a OAuth 2.0 Credentials and press the download icon
  -> save it as client_secret.json
  

# Now you are good to go 
Just a simple task now
Add the Id of instagram account you want to scrape feed of in id.txt file
  



# Now run videogen.py and after the required videos are downloded 
# Now run main.py to upload the fiels to your youtube

```python
#if you want to automate this task everyday late night then
#add this line of code in the end of compiler.py file


import main
main.run()

```
