import os
import time
import requests
from grobid_client.grobid_client import GrobidClient

def esperar_grobid(server_url):
    for _ in range(30):
        try:
            response = requests.get(f"{server_url}/api/isalive")
            if response.status_code == 200:
                print(f"El servicio GROBID está disponible en {server_url}")
                return True
        except requests.exceptions.ConnectionError:
            pass
        print(f"Esperando al servicio GROBID en {server_url}")
        time.sleep(5)
    print(f"El servicio GROBID no está disponible en {server_url}")
    return False

def procesar_pdfs(directorio_entrada, server_url):
    client = GrobidClient(config_path='./config.json', grobid_server=server_url)
    #client.process("processFulltextDocument", "/mnt/data/covid/pdfs", n=20)
    client.process(
                    "processFulltextDocument",
                    directorio_entrada,
                    output="/app/output",
                    n=20
                )
    print("Procesamiento completado. Revisa el directorio 'output'.")

if __name__ == '__main__':
    grobid_url = os.getenv('GROBID_URL', 'grobid')
    grobid_port = os.getenv('GROBID_PORT', '8070')
    server_url = f'http://{grobid_url}:{grobid_port}'
    if esperar_grobid(server_url):
        procesar_pdfs('/app/pdfs', server_url)