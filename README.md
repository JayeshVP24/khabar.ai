<br />
<div align="center">
  <a href="https://github.com/JayeshVP24/MumbaiHacks">
    <img src="public/logo.gif" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Khabar.AI</h3>

  <p align="center">
    Khabar.AI - Exploring and understanding the world via check
    <br />
    <a href="https://github.com/JayeshVP24/MumbaiHacks"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/JayeshVP24/MumbaiHacks">View Demo</a>
    ·
    <a href="https://github.com/JayeshVP24/MumbaiHacks/issues">Report Bug</a>
    ·
    <a href="https://github.com/JayeshVP24/MumbaiHacks/issues">Request Feature</a>
  </p>
</div>



<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#About">About</a></li>
    <li><a href="#Features">Features</a></li>
    <li><a href="#Tech-Stack">Tech Stack</a></li>
    <li><a href="#Languages-and-Tools">Languages and Tools</a></li>
    <li><a href="#Workflow">Workflow</a></li>
    <li><a href="#Instructions-on-running-project-locally">Instructions on running project locally</a></li>
    <li><a href="#Feedback">Feedback</a></li>
  </ol>
</details>

------

## About

In today's digital world, the spread of misinformation and deceptive news has reached unprecedented levels. It's becoming increasingly difficult to distinguish between accurate information and manipulative narratives. That's why we created Khabar.AI. As the need for reliable news evaluation grows, Khabar.AI emerges as a beacon of truth. Developed to combat misinformation, propaganda, and coordinated campaigns, this powerful tool equips you with the ability to uncover the hidden truths behind the articles you encounter.

With Khabar.AI, you'll gain access to advanced features like sentiment analysis, text analytics, propaganda identification, hate speech detection, and bot activity analysis. Our easy to use interface ensures that evaluating news articles and identifying unreliable sources is just a few clicks away.


## Features

🔍 **Real-Time Twitter Integration**: Stay updated with the latest news through real-time Twitter integration and the Lambda index.


📰 **Sentiment Analysis**: Measures the sentiment of entities mentioned in articles, providing a balanced view of the information being presented.

🐦 **Langchain-based LLM Model with Google Search Integration**: Get real-time information and related links with Google Search integration.

💬 WhatsApp Bot Integration: Seamlessly integrate Khabar.AI with WhatsApp for enhanced accessibility and interaction. 

📝 **Text Analytics**: To understand about the content on the article and understanding in an analytical way like summarization, most word used like word cloud, etc.

🕵️ **Propaganda Identification**: Useful to identify whether the content/information present in the news article/blog or any string url contains any propoganda and also provides the score with yes and no labels.

🧐 **Hate Speech Detection**: The hate speech is identified with the help of hate_speech_eng and classify into the classes like **Acceptable, Inapproproiate, offensive, voilet.** 

⚠️ **Unrevealing Misinformation**:  Helping users identify unreliable sources by detecting and flagging misleading or inaccurate information.

🤖 **Bot Activity Detection**: Identifies coordinated clusters of bots and automatons, providing insight into potential manipulation and disinformation campaigns. 

📱 **Social Media Presence**: Explores the presence of the same information present on the social media like twitter and other metadata associated with it like like, share, top user retweeting it the most, etc. 

🌐 **Real-Time Twitter Analytics**: Url or the string provided for the news article/blog is identified on the social media and the activity performed by different user and the sentiment of the people tweeting with the same link is provided by social crypt. 

#️⃣ **Associated Presence**: To understand the associated hashtags or other information with the blog and also the top users sharing the content.

⚙️**Easy-to-Use Interface**: User-friendly interface, making it accessible and intuitive for users of all levels. Only putting the URL of the blog and the application will generate the whole analytical report.



## Tech Stack

**Frontend** - Whatsapp Bot

**Backend** - Flask

**Other Tools** - Twitter, HuggingFace, LlamaIndex, Langchain, Plotly, Seaborn, Serp



## Languages and Tools

<p align="left"> <a href="https://www.gnu.org/software/bash/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/gnu_bash/gnu_bash-icon.svg" alt="bash" width="40" height="40"/> </a>  <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> <a href="https://flask.palletsprojects.com/en/2.2.x/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="nodejs" width="40" height="40"/> </a><a href="https://huggingface.co/" target="_blank" rel="noreferrer"> <img src="https://www.svgrepo.com/show/401953/hugging-face.svg" alt="nodejs" width="40" height="40"/> </a><a href="https://llamahub.ai/" target="_blank" rel="noreferrer"> <img src="https://aeiljuispo.cloudimg.io/v7/https://s3.amazonaws.com/moonup/production/uploads/6424f01ea4f3051f54dbbd85/oqVQ04b5KiGt5WOWJmYt8.png?w=200&h=200&f=face" alt="nodejs" width="40" height="40"/> </a><a href="https://llamahub.ai/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/WhatsApp_Logo.svg/2048px-WhatsApp_Logo.svg.png" alt="nodejs" width="40" height="40"/> </a>
 
 
 
 

 
 ## Instructions on running project locally:

Clone the project

```bash
  git clone https://github.com/JayeshVP24/MumbaiHacks
```

Install dependencies:

```bash
  cd www.khabar-ai.com/
  
  pip install -r requirements.txt
```

Run Project on terminal

```bash
  cd apps/api.khabar-ai.com
  py app.py
```

Start the server

```bash
  http://localhost:127.0.0.5000
```

## Usecases

🗳️ **In Political campaigns,** Monitor and analyse social media activity and sentiment surrounding issues and candidates from parties, in order to gain a better understanding of public opinion from social media.

📰 **In News Media,** Identify and prevent misinformation by analysing the sentiment and credibility of news articles and sources. As News Media is the platform where the information is spread so having the correct fact check is important. 

📦 **In Product Market Fit Analysis,** To understand about the product with the help of sentiment of the user reviews on social media and also monitoring the needs to improve it in a better way. It is useful tor analysing whether the product is market fit or not.

🕵️ **Identifying Suspected Users ,** Keeping track of the activity and sentiment of users who interact with a specific piece of content on social media. It’s helpful to understand doing spam tweets on the same content or spreading misleading content.

🤖 **Detecting Unusual Behaviour,** Track and Identify coordinated bot and automaton campaigns to prevent manipulation and disinformation.

✔️ **In Informative/Factual Content Curation,** Curating and Checking the whether the content is correct or containing any manipulative sentence.

📄 **In Research Analysis,** Useful for research about the product/news/hashtags nature and sentiment on the social media to understand it in a better way and also helpful to understand the trend.


## Authors

🔆 [@Jayesh Potlabattini](https://github.com/Mr-Jayesh)

🔆 [@Hrishikesh Yadav](https://www.github.com/hrishikesh332)

🔆 [@Prathik Shetty](https://www.github.com/prathikshetty2002)



## Feedback

If you have any feedback, please reach out to us at **jayeshpotlabattini24@gmail.com**


## Support

For support join our Slack channel - [AMA](https://ml-geeksworkspace.slack.com/archives/C03K2M9SBAA)

## License

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

