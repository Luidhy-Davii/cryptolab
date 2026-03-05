# 🔐 CryptoLab

CryptoLab é um projeto em **Python** desenvolvido com foco educacional para explorar diferentes técnicas de **criptografia clássica e moderna**.  
O sistema funciona via **terminal interativo**, permitindo ao usuário criptografar e descriptografar mensagens utilizando diversos algoritmos.

O projeto foi desenvolvido com **boas práticas de programação**, **modularização** e uma interface de terminal estilizada usando a biblioteca **Rich**.

---

# 📚 Criptografias Implementadas

O CryptoLab possui um menu interativo com os seguintes métodos:

### 1️⃣ Cifra de César
Uma das criptografias mais antigas da história.

- Funciona deslocando as letras do alfabeto.
- Exemplo com deslocamento 3:

```
A → D
B → E
C → F
```

#### Complexidade
- Tempo: **O(n)**
- Espaço: **O(n)**

---

### 2️⃣ Cifra de Vigenère
Uma evolução da Cifra de César que utiliza **uma palavra-chave** para realizar múltiplos deslocamentos.

Exemplo:

Mensagem:
```
ATAQUE
```

Chave:
```
LIMAO
```

Cada letra da chave define um deslocamento diferente.

#### Complexidade

- Tempo: **O(n)**
- Espaço: **O(n)**

---

### 3️⃣ RSA
Algoritmo de **criptografia assimétrica** utilizado amplamente na internet.

Ele utiliza:

- chave pública
- chave privada
- fatoração de números primos grandes

Fluxo simplificado:

```
Mensagem → Criptografada com chave pública → Descriptografada com chave privada
```

#### Complexidade

Depende da implementação, mas geralmente envolve:

- exponenciação modular
- complexidade aproximada: **O(log n)** para operações principais

---

### 4️⃣ Base64

Base64 **não é uma criptografia**, mas um método de **codificação de dados**.

Ele transforma dados binários em caracteres ASCII.

Exemplo:

```
Texto: Hello
Base64: SGVsbG8=
```

#### Complexidade

- Tempo: **O(n)**
- Espaço: **O(n)**

---

### 5️⃣ SHA-256

Algoritmo de **hash criptográfico**.

Características:

- hash de **256 bits**
- **irreversível**
- muito usado em:
  - segurança
  - senhas
  - blockchain

Exemplo:

```
senha123 → ef92b778...
```

#### Complexidade

- Tempo: **O(n)**

---

# 🖥 Interface do Sistema

O projeto possui um **menu estilizado no terminal** utilizando a biblioteca **Rich**.

Exemplo:

```
🔐 CryptoLab

1 - Cifra de César
2 - Vigenère
3 - RSA
4 - Base64
5 - SHA-256
6 - Laboratório
0 - Sair
```

---

# 📦 Bibliotecas Utilizadas

### Rich

Biblioteca usada para estilizar a interface do terminal.

Recursos utilizados:

- menus coloridos
- caixas (Panel)
- prompts estilizados

Documentação oficial:

https://github.com/Textualize/rich

---

# 🚀 Como Clonar o Projeto

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/crypto_lab.git
```

Entre na pasta:

```bash
cd crypto_lab
```

---

# 🧪 Criar Ambiente Virtual

Crie a **venv**:

```bash
python3 -m venv venv
```

Ative a venv:

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

# 📥 Instalar Dependências

Instale a biblioteca necessária:

```bash
pip install rich
```

---

# ▶️ Executar o Projeto

Execute o arquivo principal:

```bash
python main.py
```

---

# 🎯 Objetivo do Projeto

O CryptoLab foi desenvolvido para:

- estudar **criptografia**
- entender **algoritmos clássicos**
- praticar **Python modular**
- aplicar **boas práticas de desenvolvimento**

É um projeto ideal para estudantes de:

- Ciência da Computação
- Segurança da Informação
- Programação em Python

---

# 👨‍💻 Autor

**Luidhy Davi**

Estudante de **Ciência da Computação** na **UNIP**  
Focado em **Desenvolvimento Front-End e Software Engineering**
