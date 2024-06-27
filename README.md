## Remover Plano de Fundo: Aplicação GUI para Remover Fundo de Imagens

Esta aplicação GUI, desenvolvida em Python com a biblioteca `tkinter`, permite remover o fundo de imagens de forma simples e rápida utilizando a biblioteca `rembg`.

<p align="center">
  <img src="./assets/icon.png" alt="ícone do app" width="200"/>
</p>

### Funcionalidades:

- **Selecionar Imagem:** Permite carregar uma imagem do seu computador.
- **Remover Plano de Fundo:** Remove o fundo da imagem selecionada usando a biblioteca `rembg`.
- **Salvar Resultado:** Salva a imagem com o fundo removido em um novo arquivo.
- **Interface Gráfica:** Possui uma interface gráfica intuitiva e amigável.

### Como Usar:

1. **Instale as dependências:**

   ```bash
   pip install Pillow rembg
   ```

2. **Execute o script:**

   ```bash
   python remove_background.py
   ```

3. **Selecione uma imagem:**

   - Clique no botão "Selecionar Imagem".
   - Navegue até a imagem que você deseja remover o fundo e abra-a.

4. **Remova o plano de fundo:**

   - Clique no botão "Remover Plano de Fundo".
   - A aplicação irá processar a imagem e remover o fundo.

5. **Salve o resultado:**
   - Clique no botão "Salvar Resultado".
   - Escolha um nome e local para salvar a imagem com o fundo removido.

### Gerando um Executável para Linux:

1. **Instale o PyInstaller:**

   ```bash
   pip install pyinstaller
   ```

2. **Gere o executável:**

   ```bash
   pyinstaller --onefile --icon="./assets/icon.png" --noconsole --hidden-import=scipy._lib.array_api_compat.numpy.fft --hidden-import=scipy.special --hidden-import=scipy.special._special_ufuncs --hidden-import=PIL._tkinter_finder remove_background.py
   ```

3. **Execute o executável:**
   - O PyInstaller criará uma pasta chamada `dist` no seu diretório de projeto.
   - Dentro dessa pasta, você encontrará o arquivo executável do seu aplicativo.
   - Você pode executá-lo diretamente clicando duas vezes no arquivo ou usando o comando:
     ```bash
     ./dist/remove_background
     ```

### Observações:

- **Ícone:** O ícone do executável é definido na opção `--icon` do comando do PyInstaller. Certifique-se de que o arquivo `icon.png` esteja na pasta `assets` na raiz do seu projeto. Ainda não foi possível adicionar o ícone corretamente no build para linux.
- **Dependências:** Certifique-se de que todas as dependências do seu projeto estejam instaladas corretamente no ambiente virtual.
- **Modelos de IA:** O `rembg` precisa baixar os modelos de IA pela primeira vez. Isso pode levar algum tempo. Quando abrir o executável pela primeira vez, os modelos serão baixados, a partir da segunda vez, o carregamento será mais rápido.
