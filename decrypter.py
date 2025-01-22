import os
import pyaes

# Abrir o arquivo criptografado
file_name = 'teste.txt.ransomwaretroll'
try:
    with open(file_name, 'rb') as file:
        file_data = file.read()
except FileNotFoundError:
    print(f"Erro: {file_name} não encontrado.")
    exit()

# Definir chave de descriptografia
key = b'testeransomware'
aes = pyaes.AESModeOfOperationCTR(key)

# Descriptografar o arquivo
decrypt_data = aes.decrypt(file_data)

# Remover o arquivo criptografado
os.remove(file_name)

# Criar um novo arquivo descriptografado
new_file = 'teste.txt'
with open(new_file, 'wb') as new_file:
    new_file.write(decrypt_data)

print(f"Arquivo descriptografado salvo como {new_file}")
