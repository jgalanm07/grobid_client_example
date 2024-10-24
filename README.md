# GROBID Client Example

This is a basic example of a Python client that communicates with a GROBID server to extract metadata from scientific PDF documents. The setup uses Docker Compose to manage both the GROBID server and the client application.

# Setup and Deployment
## 1. Place PDF Files
- Place the PDF files you want to process into the client/pdfs/ directory.
## 2. Build and Run the Services
```bash
docker compose build
docker compose run
```
## 3. Wait for Processing
- The client will wait for the GROBID server to be available.
- It will then process any PDFs found in the client/pdfs/ directory.
- The extracted metadata will be saved in the client/output/ directory.

## 4. Check the Output
The output files will be in the client/output/ directory on your host machine.