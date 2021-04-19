# Clickjacking
Explaining clickjacking! Bypass, automation and more.

<h1>What is Clickjacking?</h1>
Clickjacking, also known as a “UI redress attack”, is when an attacker uses multiple transparent or opaque layers to trick a user into clicking on a button or link on another page when they were intending to click on the top level page. Thus, the attacker is “hijacking” clicks meant for their page and routing them to another page, most likely owned by another application, domain, or both.

<h1>Defending against Clickjacking</h1>
There are two main ways to prevent clickjacking:

Sending the proper Content Security Policy (CSP) frame-ancestors directive response headers that instruct the browser to not allow framing from other domains. (This replaces the older X-Frame-Options HTTP headers.)
Employing defensive code in the UI to ensure that the current frame is the most top level window.
<p>Credits: Owasp - https://owasp.org/www-community/attacks/Clickjacking</p>

# Script for Automation
Here in the repository, there is a folder called Script Automation. There is a script made in python that is used to detect whether or not a site has the "X-Frame-Options" header set.
You can upload just one site to scan or upload a list of multiple sites.

Install:
```
git clone https://github.com/diego-tella/Clickjacking.git
cd Clickjacling/Script_Automation
chmod +x install.sh
./install.sh
python3 script.py
```
<span style="color:red;">Attention!</span> it is necessary to use python3.

# Simple Exploit
We have an example of how a Clickjacking attack can be used.
The attacker checks with the ```<iframe>``` tag if the victim site is vulnerable. If so, it leaves the entire content of the ```<iframe>``` tag invisible using CSS. For the exploit to work, the hacker sets exactly in the iframe tag where the victim has to click on the website. It creates a button, making the victim click that button with social engineering, but when clicking, the victim will actually be clicking on a button in website of the ```<iframe>```, potentially doing something malicious.

# Bypass X-Frame-Options
The script developed in JavaScript uses a proxy to scrape the target page and return the content without the header. It will only work for GET requests, won't get cookies, can only scrape pages the third party proxies (one ofcors.io, jsonp.afeld.me, cors-anywhere.herokuapp.com) can access (and may leave a copy of the content on one of those sites).<br>
Official repository: https://github.com/niutech/x-frame-bypass
