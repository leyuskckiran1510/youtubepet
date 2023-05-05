<a name="readme-top"></a>
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Apache License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<br />
<div align="center">
  <a href="https://github.com/leyuskckiran1510/YoutubePet">
    <!-- <img src="ExtensionFireFox/icon.png" alt="Logo" width="80" height="80"> -->
  </a>

  <h1 align="center">YoutubePet</h1>

  <p align="center">
    Introducing our revolutionary project that empowers users to effortlessly scrape the Instagram feed of their favorite celebrities and upload it to YouTube with ease! Our cutting-edge technology automates the tedious and time-consuming task of compiling small files into a seamless video, complete with proper thumbnails and video descriptions.

With just a simple command, our user-friendly pet project springs into action, handling all the complex backend work while you focus on your productive tasks. Whether you're a content creator or a social media enthusiast, this project is the perfect solution to save you time and energy while elevating your online presence.

We're excited to share this powerful tool with the world, and we're confident that it will make a significant impact in the lives of our users. So why wait? Give our project a try today and experience the ultimate convenience and efficiency in creating engaging and high-quality content.
    <br />
    <a href="https://github.com/leyuskckiran1510/YoutubePet"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://youtu.be/VJFZETC0QiM">View Demo</a>
    ·
    <a href="https://github.com/leyuskckiran1510/YoutubePet/issues">Report Bug</a>
    ·
    <a href="https://github.com/leyuskckiran1510/YoutubePet/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!--[![Product Name Screen Shot][product-screenshot]](https://github.com/leyuskc/YoutubePet)-->

### "It is an easy-to-use for you passive income as youtube content creator. To use it, simply install it and choose what you want to learn. Then let it do its thing."

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

It is built with python
* [![Python][Python]][Pythonorg]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

So If want to use it for yourself then here is how.

### Prerequisites

1. `Google Youtube Api`<br>
[CLICK HERE TO DOWNLOAD YOUR PROJECT JSON FILE](https://console.cloud.google.com/apis/api/youtube.googleapis.com/credentials)

2. `Python 3.X `

3. `FFmpeg`


### Installation

_Now the packages installation and file setup part.Follow the step below and you should be goto go._


1. Clone the repo
   ```sh
   git clone https://github.com/leyuskckiran1510/YoutubePet.git
   cd ./YoutubePet
   ```
   I assume you are in the code folder after this till to very end.

2. Creating Virtual Environments.
    ```python
        python -m venv virtual
    ```
3. Activating virtual Environments<br>
        Windows Users<br>
    ```ps1
        .\source\Scripts\activate.ps1
                or
        .\source\Scripts\activate.bat
    ```
    <br>Linux/Mac users<br>
    ```sh
        source ./virtual/bin/activate
    ```

4. Now installing the requirements.
    ```ps
    python -m pip install -r requirements.txt
    ```




<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Welcome to our game-changing product that streamlines the process of scraping Instagram feeds and uploading them to YouTube! This innovative solution offers a hassle-free approach to compiling small files into an engaging video with proper thumbnails and descriptions.

Using our product is a breeze - simply run the designated file and let our intuitive pet project do the rest. While it works its magic, you can focus on other productive tasks, confident that your content is being handled with the utmost care and efficiency.

Our product is perfect for anyone looking to save time and effort while creating compelling content, whether you're a content creator, social media influencer, or marketing professional. By automating the process of compiling Instagram feeds into YouTube videos, our product enables you to showcase your content in the best possible light with minimal effort.

We're excited to offer this powerful tool to the world and look forward to seeing the many ways it can help individuals and businesses alike. Try our product today and discover the ultimate convenience and effectiveness in creating outstanding online content!

_For more examples, please refer to the [Documentation](https://github.com/leyuskckiran1510/YoutubePet)._

_A Example or simple usecase video may be uploaded to youtube if uploaded then you can click this link [Video](https://youtu.be/VJFZETC0QiM)_

```md
#UseCase and Images will be published after the project is completed.
```
# How to use
  1. Make a google project
  1. Add Youtube Data Api V3 in that project 
  #### [CLICK HERE TO DOWNLOAD YOUR PROJECT JSON FILE](https://console.cloud.google.com/apis/api/youtube.googleapis.com/credentials)
  1. Now click  **_'+ Create credentials'_** button
  1. create a OAuth 2.0 Credentials and press the download icon
  1. save it as client_secret.json
  

## Now you are good to go 
Just a simple task now
Add the Id of instagram account you want to scrape feed of in id.txt file
  



### Now run videogen.py and after the required videos are downloded 
### Now run main.py to upload the fiels to your youtube

```python
#if you want to automate this task everyday late night then
#add this line of code in the end of compiler.py file


import main
main.run()

```


# Some inportant note
```diff
- In some files like main.py ...
- I have left some blank values with following comments So check the entrie code once and add your desire pice of data like Video title ...
- And after making the required change sdelet the unnecessary comment and run your code finally and enjoy

```


<p align="right">(<a href="#readme-top">back to top</a>)</p>


See the [open issues](https://github.com/leyuskckiran1510/YoutubePet/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU license. See [`LICENSE.txt`](https://github.com/leyuskckiran1510/YoutubePet/blob/main/LICENSE) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact


Project Link: [Click ME](https://github.com/leyuskckiran1510/YoutubePet)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Will fill letter when project gets started<br>
Also Thanks to [@othneildrew](https://github.com/othneildrew/Best-README-Template) for providing these readme template.



<p align="right">(<a href="#readme-top">back to top</a>)</p>




[contributors-shield]: https://img.shields.io/github/contributors/leyuskckiran1510/YoutubePet.svg?style=for-the-badge
[contributors-url]: https://github.com/leyuskckiran1510/YoutubePet/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/leyuskckiran1510/YoutubePet.svg?style=for-the-badge
[forks-url]: https://github.com/leyuskckiran1510/YoutubePet/network/members
[stars-shield]: https://img.shields.io/github/stars/leyuskckiran1510/YoutubePet.svg?style=for-the-badge
[stars-url]: https://github.com/leyuskckiran1510/YoutubePet/stargazers
[issues-shield]: https://img.shields.io/github/issues/leyuskckiran1510/YoutubePet.svg?style=for-the-badge
[issues-url]: https://github.com/leyuskckiran1510/YoutubePet/issues
[license-shield]: https://img.shields.io/github/license/leyuskckiran1510/YoutubePet.svg?style=for-the-badge
[license-url]: https://github.com/leyuskckiran1510/YoutubePet/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/leyuskc
[product-screenshot]: images/screenshot.png
[Python]:https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python
[Pythonorg]:https://www.Python.org/

