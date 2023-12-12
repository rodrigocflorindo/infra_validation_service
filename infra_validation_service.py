# requirements.txt

# infra_validation_service.py

import subprocess

def validate_dns(host):
    try:
        subprocess.run(['nslookup', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def validate_network():
    # Aqui você pode adicionar outras validações de rede, se necessário
    # Por exemplo, verificar a conectividade com um serviço específico

    # Exemplo básico de validação de conectividade com um host
    return validate_dns('google.com')

if __name__ == "__main__":
    if validate_network():
        print("Recursos de infraestrutura validados com sucesso!")
    else:
        print("Falha na validação dos recursos de infraestrutura.")
