# Web-Crawler
A bot created in python using selenium to crawl pages and sub pages of a website and store the outputs in json format.It can crawl any website page and its sub pages recursively and therefore , generates json file for output of each page individually. Initial url of main website is provided at runtime.

Steps to execute-
1. Ensure python3 and selenium in your system.
2. Clone this repository and extract files from it.
3. Move to the directory containing main.py file using cmd(for windows).
4. Write following code in cmd:
        python main.py "url of website"
   NOTE: "url of website" above refers to the url of site that is to be crawled.
   Also this cmd code may vary for different Operating Systems.

OUTPUT:
  Output will appear in json file format and can be seen in the same directory once the program is executed successfully.

Logs of code execution can be seen in log.txt file.
  
  main1.py includes code which can crawl a website in background itself without showing further steps to the program.
        To execute main1.py,write following code in cmd after reaching to the path of main1.py:
                        python main1.py "url of website"
