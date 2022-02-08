# Cache Crawler
...
# TL;DR

This script runs daily and crawls all sitemaps in .env, I will add more later... hopefully
## Prerequirements

settings.env file with <code>SITEMAP_LIST</code> variable set

requirements.txt with the following content:
<code>
requests==2.27.1
python-dotenv==0.19.2
</code>


## How to run

<code>docker build -t crawler .</code>
<code>docker run crawler</code>
