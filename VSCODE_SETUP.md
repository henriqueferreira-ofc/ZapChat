# Configuração do VS Code para o Projeto ZapChat

## Problema: "Sorry, something went wrong activating IntelliCode support for Python"

### Soluções:

#### 1. Reiniciar o VS Code
- Feche completamente o VS Code
- Abra novamente o projeto
- Aguarde as extensões carregarem

#### 2. Verificar Extensões Python
Certifique-se de que as seguintes extensões estão instaladas:
- Python (ms-python.python)
- VS IntelliCode (VisualStudioExptTeam.vscodeintellicode)
- Pylance (ms-python.vscode-pylance)

#### 3. Selecionar Interpretador Python Correto
1. Pressione `Cmd+Shift+P` (macOS)
2. Digite "Python: Select Interpreter"
3. Selecione: `/Users/henriquecesararaujoferreira/Documents/PROJETOS /ZapChat/myenv/bin/python3`

#### 4. Recarregar Janela
1. Pressione `Cmd+Shift+P`
2. Digite "Developer: Reload Window"
3. Pressione Enter

#### 5. Limpar Cache do VS Code
1. Pressione `Cmd+Shift+P`
2. Digite "Python: Clear Cache and Reload"
3. Pressione Enter

### Configurações Aplicadas:

O arquivo `.vscode/settings.json` foi configurado com:
- Interpretador Python correto
- Ativação automática do ambiente virtual
- Configurações de formatação

### Como Executar o Projeto:

```bash
# 1. Ativar ambiente virtual
source myenv/bin/activate

# 2. Executar aplicativo
python3 main.py
```

### Debug no VS Code:

Use as configurações de debug criadas em `.vscode/launch.json`:
- "Python: Current File" - para executar arquivo atual
- "Python: Flask" - para executar aplicativo Flask

### Se o problema persistir:

1. Desinstale e reinstale as extensões Python
2. Verifique se há conflitos com outras extensões
3. Consulte os logs do VS Code (Help > Toggle Developer Tools) 