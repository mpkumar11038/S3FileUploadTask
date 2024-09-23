import uuid
from cryptography.fernet import Fernet
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

class FileUploadView(APIView):
    """
    API view for uploading and encrypting files.
    """
    def post(self, request):
        """
        Handles POST requests to upload and encrypt a file.
        """
        try:
            # Check if the 'file' key exists in the request
            if 'file' not in request.FILES:
                return JsonResponse(
                    {"message": 'No file provided'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

            file = request.FILES['file']
            key = Fernet.generate_key().decode('utf-8')  # Generate an encryption key
            encrypted_file = self.encrypt_file(file, key)  # Encrypt the file
            file_content = ContentFile(encrypted_file)  # Prepare the encrypted file content for saving

            # Generate a unique filename
            name, ext = file.name.rsplit('.', 1)
            filename = f"{name}-{uuid.uuid4()}.{ext}"

            # Save the encrypted file to storage
            default_storage.save(filename, file_content)

            return JsonResponse(
                {"message": 'File uploaded and encrypted successfully!',
                 "file": file.name}, 
                status=status.HTTP_200_OK
            )

        except Exception as e:
            # Handle any unexpected errors
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def encrypt_file(self, file, key):
        """
        Encrypts the provided file using the specified encryption key,
        Returns the encrypted file content in bytes.
        """
        cipher_suite = Fernet(key.encode('utf-8'))  # Initialize the cipher suite with the key
        encrypted_file = cipher_suite.encrypt(file.read())  # Encrypt the file content
        return encrypted_file
