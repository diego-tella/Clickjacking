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
