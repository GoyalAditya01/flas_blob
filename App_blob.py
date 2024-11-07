from flask import Flask, render_template, jsonify, send_file
from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os
import io

app = Flask(__name__)
load_dotenv()

# Azure Blob Storage configuration
client_id = os.environ['AZURE_CLIENT_ID']
tenant_id = os.environ['AZURE_TENANT_ID']
client_secret = os.environ['AZURE_CLIENT_SECRET']
account_url = os.environ["AZURE_STORAGE_URL"]

# Create a credential 
credentials = ClientSecretCredential(
    client_id=client_id, 
    client_secret=client_secret,
    tenant_id=tenant_id
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download_blob", methods=["GET"])
def download_blob():
    container_name = 'mystoragedemo'
    blob_name = '26092024 Touchbase_ Bexsero_Enhancement_KPIs_V1.0 (1) - Copy.pptx'

    try:
        blob_service_client = BlobServiceClient(account_url=account_url, credential=credentials)
        container_client = blob_service_client.get_container_client(container=container_name)
        blob_client = container_client.get_blob_client(blob=blob_name)

        blob_data = blob_client.download_blob().readall()

        return send_file(
            io.BytesIO(blob_data),
            download_name=blob_name,
            as_attachment=True
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)

