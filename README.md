# LinkedIn Connector

A simple LinkedIn Bot that sends connection requests to people appear on specific search result.

## Made using

- Python
- Selenium
- Edge Browser
- VSCode

## Make it work for you

Follow these steps below to run this

- Download Edge Driver or Chrome Driver for your operating system.

- Put it into the root directory.

- Open ```bot.py``` file in your favorite code editor.

- Go to _line 11_, change it to:
  - ```browser = webdriver.Edge("msedgedriver.exe")``` if you want use Microsoft Edge.
  - ```browser = webdriver.Chrome("chromedriver.exe")``` if you want use Google Chrome.

- Fill these fields with proper credentials and parameters inside ```bot.py``` file.

``` mail = "your_nice_username"
key = "your_secret_pass"
search_param = "search_term"
pages_upto = 5 ```

- Having Python installed on your machine, run ```pip install selenium``` on terminal.

- Now run ```python bot.py``` on terminal.

### [Iben Nahian](https://www.linkedin.com/in/evilprince2009/)
