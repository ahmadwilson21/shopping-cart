# Shopping-Cart

## Installation

Fork this remote repository, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):


```sh
cd shopping-cart
```
Use Anaconda to create a new env called perhaps shopping-env
```sh
create -n shopping-env python=3.7 # (first time only)
conda activate shopping-env
```

From inside the virtual environment, install package dependencies:
```sh
pip install -r requirements.txt
```

### Google Sheets API Installation

Downloading API Credentials

Visit the Google Developer Console(https://console.developers.google.com/cloud-resource-manager). Create a new project, or select an existing one. Click on your project, then from the project page, search for the "Google Sheets API" and enable it. Also search for the "Google Drive API" and enable it.

From either API page, or from the API Credentials page(https://console.developers.google.com/apis/credentials), follow a process to create and download credentials to use the APIs. Fill in the form to find out what kind of credentials:

    API: "Google Sheets API"
    Calling From: "Web Server"
    Accessing: "Application Data"
    Using Engines: "No"

The suggested credentials will be for a service account. Follow the prompt to create a new service account with a role of: "Project" > "Editor", and create credentials for that service account. Download the resulting .json file and store it in your project repo in a location called "auth/google_api_credentials.json"
The path should be as follows:
```sh
cd shopping-cart/auth/google_api_credentials.json
```



Use this example google sheet (https://docs.google.com/spreadsheets/d/1_hisQ9kNjmc-cafIasMue6IQG-ql_6TcqFGpVNOkUSE/edit#gid=0) or create your own. Note the document's unique identifier (e.g. 1_hisQ9kNjmc-cafIasMue6IQG-ql_6TcqFGpVNOkUSE) from its URL, and store the identifier in an environment variable called GOOGLE_SHEET_ID.

If you create your own, make sure it contains a sheet called "Products" with column headers id, name, department, price, and availability_date. And modify the document's sharing settings to grant "edit" privileges to the "client email" address located in the credentials file.

### Sendgrid API Installation
First, sign up for a free account here (https://signup.sendgrid.com/), then click the link in a confirmation email to verify your account. Then create an API Key here (https://app.sendgrid.com/settings/api_keys) with "full access" permissions.

To setup the usage examples below, store the API Key value in an environment variable called SENDGRID_API_KEY. Also set an environment variable called MY_EMAIL_ADDRESS to be the email address you just associated with your SendGrid account (e.g. "abc123@gmail.com"). You will send emails from this account





### Add a Custom Tax
Add a custom tax value to be used by creating a variable in your .env file called CUSTOM_TAX
(eg. CUSTOM_TAX = "0.85")

## Usage



Run the program by calling
```sh
python shopping-cart/shopping_cart.py
```



