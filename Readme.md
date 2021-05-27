# Google Drive V3 API: Upload/Update multiple files into a created folder within Drive using Python.

This is a script that uses the google drive api v3. Further Documentation and References can be found on the official website: https://developers.google.com/drive/api/v3/about-sdk . Google APIs use Oauth 2.0.


## Pre-requisite steps:

* 1. Install python 2.6 or greater.
* 2. Have pip installed.
* 3. A Google cloud platform desktop project with the drive v3 api enabled: https://developers.google.com/workspace/guides/create-project
* 4. Authorization credentials for a desktop application: https://developers.google.com/workspace/guides/create-credentials#desktop, remember to download and change the client secret .json file name to credentials.json.
* 5. And of course, a Google Drive account.
* Note: you may want to configure the scope of the API if you want to only allow specific access. Current implementation gives the App full access. For more information on this and how to change the scope: https://developers.google.com/workspace/guides/create-credentials#configure_the_oauth_consent_screen

## STEP 1: Install required libraries 
* Run   `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

## STEP 2: Authenticate flow on the initial run
* Run the script with `python quickstart.py`  . This will open new window prompting you to allow the Application to access your google drive data. (Note this is only for the initial run).

# Additional Information:

* The current script will create a new folder every time it is run containing any new/updated files to be uploaded on google drive. It handles updates by removing the old folder if it exists.
* Please modify the names of the folder & list of files within `quickstart.py` in order to suit individual needs.
* If you want to read about/implement additional functionality please refer to the official google guides using the link at the top of this page.
*  The current scope allows the application to only handle the files it creates. More information on scopes: https://developers.google.com/identity/protocols/oauth2/scopes#drive

*  if your application loses the refresh token, the user will need to repeat the OAuth 2.0 consent flow so that your application can obtain a new refresh token.

## How long do refresh tokens last?

* The current documentation contains conflicting information about the lifetime of refresh tokens. Google's Oauth 2.0 documentation suggests that refresh tokens last for 7 days and there is a limit of 50 refresh tokens per normal Google account (no limit for a service account). https://developers.google.com/identity/protocols/oauth2#expiration

*  Information on refresh token for Mobile/desktop applications suggest that refresh tokens are valid until they are revoked. https://developers.google.com/identity/protocols/oauth2/native-app#exchange-authorization-code

## Setting up a service account to handle the authentication process.

* If you have admin access to a google workspace account, You can create a service account that belongs to the Google application rather than an individual end user. The application will call Google APIs on behalf of the service account - user consent is not required. 

* https://developers.google.com/identity/protocols/oauth2/service-account#delegatingauthority for more information on implementation.


