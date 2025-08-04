# ZapChat

Um aplicativo de chat em tempo real desenvolvido com Flask e Socket.IO, inspirado no WhatsApp.

## 🚀 Funcionalidades

- Chat em tempo real
- Interface similar ao WhatsApp
- Suporte a múltiplos usuários
- Envio de mensagens por Enter ou botão
- Design responsivo

## 📋 Pré-requisitos

- Python 3.9 ou superior
- pip (gerenciador de pacotes Python)

## 🛠️ Instalação

1. **Clone o repositório:**
```bash
git clone <URL_DO_REPOSITORIO>
cd ZapChat
```

2. **Crie um ambiente virtual:**
```bash
python3 -m venv myenv
```

3. **Ative o ambiente virtual:**
```bash
# macOS/Linux
source myenv/bin/activate

# Windows
myenv\Scripts\activate
```

4. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

## 🚀 Como Executar

1. **Ative o ambiente virtual:**
```bash
source myenv/bin/activate
```

2. **Execute o aplicativo:**
```bash
python3 main.py
```

3. **Acesse no navegador:**
```
http://127.0.0.1:5001
```

## 📁 Estrutura do Projeto

```
ZapChat/
├── main.py              # Aplicação Flask principal
├── requirements.txt     # Dependências Python
├── templates/
│   └── index.html      # Interface do chat
├── myenv/              # Ambiente virtual
└── README.md           # Este arquivo
```

## 🔧 Configuração do VS Code

Se você estiver usando VS Code, consulte o arquivo `VSCODE_SETUP.md` para configurações específicas.

## 🐛 Solução de Problemas

### Porta 5000 em uso (macOS)
Se você receber erro "Address already in use", o AirPlay Receiver pode estar usando a porta 5000. O projeto foi configurado para usar a porta 5001.

### Problemas com dependências
```bash
# Reinstale as dependências
pip install --upgrade -r requirements.txt
```

## 📝 Como Usar

1. Abra o aplicativo no navegador
2. Digite seu nome de usuário
3. Digite sua mensagem
4. Pressione Enter ou clique em "Enviar"
5. Sua mensagem aparecerá para todos os usuários conectados

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
