# favorite-things
This  application allows the user to track their favorite things.

[![Netlify Status](https://api.netlify.com/api/v1/badges/08a9fa6d-e6a8-41c1-b4ee-bdf23874b11d/deploy-status)](https://app.netlify.com/sites/favoriteapp/deploys)


### Installation
Follow these steps to set up the app.
Clone the repo:
> git clone https://github.com/el-Joft/favorite-things.git

Navigate to the project directory:

##### For the backend

> cd server/

Create a virtual environment depending on your preferred environment
read more about virtualenv [here](https://virtualenv.pypa.io/en/latest/)
> virtualenv favorite-things-env

This will generate the virtual environment but will not activate it To activate the virtual environment, run:
> source favorite-things-env/bin/activate

#### Running test
run the below command to run tests
> tox

### Running and Development
Install the dependencies in the requirements.txt
To start the application
> python manage.py runserver

Run migrations using
> python manage.py migrate
### Deployment
The backend of this application was built using Python/Django/GraphQL(Graphene) which was deployed to aws using zappa while the frontend of the application was built using VueJS and deployed to Netlify.

##### To deploy using Zappa

Make sure the application is working locally
##### Setup Zappa

> zappa init

This command will bring series of prompts:
- Name of environment - just accept the default 'dev'
- S3 bucket for deployments. If the bucket does not exist, zappa will create it for you. You can use an existing bucket name if you'd like. Note that this bucket just holds the zappa package temporarily while it is being transferred to AWS lambda. The zappa package is then removed after deployment. For the purposes of the walkthrough we are using zappatest-code
- Zappa should automatically find the correct Django settings file so accept the default
- Say 'no' to deploying globally
- If everything looks ok, then accept the info

###### Create the `~/.aws/credentials` file
at the root of your machine create this file and add this into it
```
[default]
aws_access_key_id = your_access_key_id
aws_secret_access_key = your_secret_access_key
```

 ###### Deploy the setup
 This will create a `zappa_settings.json` file
 add your aws region to it
 ```
   "aws_region": "us-east-2",
 ```
 **Or** Add default region in your `~/.aws/credentials` file
 ```
 [default]
aws_access_key_id = your_access_key_id
aws_secret_access_key = your_secret_access_key
region=us-east-1
 ```
 **Or** add it using environment variables
 `export AWS_DEFAULT_REGION=us-east-1`
 
 You also have the privilege to exclude some files to prevent you from getting max file size error
 ```
 "exclude": ["*.gz", "*.rar", "htmlcov/", "*.coverage", "*.tox"]
 ```
 then run
 > zappa deploy dev
 Everything being equal the application will deploy succesfully which will generate a url
 
##### Update the settings
> server/favorite_things/settings

At the generated url to the ALLOWED_HOSTS. for example:
> ALLOWED_HOSTS = [ '127.0.0.1', 'dhfhdfdfd.execute-api.us-east-2.amazonaws.com', ]

Then run
> zappa update dev

After this completes, you can open the application in `insonmia or postman` or any of your favorite api testing tool

If, at any time, you would like to get information on the deployment, the command to run is

> zappa status dev


##### For the Frontend
> cd client/favorite-app

Install all dependencies using 
> npm install or yarn install

Start the application 
> npm run dev or npm run start


License
----

MIT

Author
----
 
### Timothy Fehintolu
[github](https://github.com/el-Joft)
 