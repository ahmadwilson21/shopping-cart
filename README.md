# Shopping-Cart

## Setup:

## Installation

Fork it, clone it, nav from command line:
```sh
cd my-repo
```
## SetupPackages to install?
Virtual environment?
## Usage

```sh
python path/to/your/file.py
```

conda create -n shopping-env python=3.7 # (first time only)
conda activate shopping-env

pip install -r requirements.txt

### Google Sheets API Installation

Downloading API Credentials

Visit the Google Developer Console. Create a new project, or select an existing one. Click on your project, then from the project page, search for the "Google Sheets API" and enable it. Also search for the "Google Drive API" and enable it.

From either API page, or from the API Credentials page, follow a process to create and download credentials to use the APIs. Fill in the form to find out what kind of credentials:

    API: "Google Sheets API"
    Calling From: "Web Server"
    Accessing: "Application Data"
    Using Engines: "No"

The suggested credentials will be for a service account. Follow the prompt to create a new service account with a role of: "Project" > "Editor", and create credentials for that service account. Download the resulting .json file and store it in your project repo in a location called "auth/google_api_credentials.json"




Note the document's unique identifier (e.g. 1_hisQ9kNjmc-cafIasMue6IQG-ql_6TcqFGpVNOkUSE) from its URL, and store the identifier in an environment variable called GOOGLE_SHEET_ID.

If you create your own, make sure it contains a sheet called "Products" with column headers id, name, department, price, and availability_date. And modify the document's sharing settings to grant "edit" privileges to the "client email" address located in the credentials file.


Enter the email address that you want to send the email from in environment variable MY_EMAIL_ADDRESS

