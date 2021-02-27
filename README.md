# URL-Shortener #
* transform longer URLs into manageable, meaning full, easy to remember short links

## Configure url mappings
* Update _url_mapping.regex_ and _nicknames.json_ file inside config folder.

### To avoid Server IP address in the URL, Add the below entry in the host file. ####

##### For Windows machine: #####
1) Open **C:\Windows\System32\Drivers\etc\hosts** file in the editor as an admin.
2) Append the below content in the file.
```
# URL Shortener
<Server_IP> go
```
3) Save the file.

## Start Dev Server
1. First install python packages.
```bash
RUN pip install -r requirements.txt
```
2. Start dev server 
```bash
python app/app.py
```

## Usage ###
* To open the PROJ1-110 Jira ticket type [http://go/j/PROJ1-110](http://go/j/PROJ1-110) URL in the browser.


**Note**: Users have to write http:// prefix only if the direct go/j/PROJ1-110 URL is not working, otherwise there is no need to write http:// prefix every time.

