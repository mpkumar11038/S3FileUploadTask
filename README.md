# S3FileUpload
## Follow below steps to setup the project 

Open your favorite Terminal and run these commands.

First open the directry where you want to clone the project
```sh
cd "path/to/your/dierectry"
```
1. Clone the Repository and go to the Repository

```sh
git clone <repository_url>
cd <repository_name>
```
2. Create and Activate a Virtual Environment

```sh
# Create a virtual environment
python -m venv env

# Activate the virtual environment
# On Windows
env\Scripts\activate

# On macOS and Linux
source env/bin/activate
```

3. Install Project Dependencies
```sh
pip install -r requirements.txt
```

4. Create Migrations
```sh
python manage.py makemigrations
```

5. Apply Migrations
```sh
python manage.py migrate
```

6. Create a superuser
```sh
python manage.py createsuperuser
```

7. Setting Up AWS credentials in the `.env` file:

```dotenv
AWS_ACCESS_KEY_ID='your_access_key_id'
AWS_SECRET_ACCESS_KEY='your_secret_access_key'
AWS_STORAGE_BUCKET_NAME='your_bucket_name'
AWS_REGION='your_aws_region'
```
8. Start the Development Server
```sh
python manage.py runserver
```
> Note: keep the server on to test in local.

9. Check the endpoint at.

```sh
127.0.0.1:8000/upload_to_s3_app/upload_file/
```
10. How to Test 
```sh
- Upload a File.
- Verify Upload Completion.
- Check S3 Bucket.
```
