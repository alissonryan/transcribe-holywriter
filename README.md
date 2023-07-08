# Transcrição Automática de Vídeos do YouTube com Python e Google Colab

Este é um simples script Python que permite baixar um vídeo do YouTube, extrair o áudio e transcrever o áudio usando a biblioteca Whisper da OpenAI.

## Passo a passo para usar este script

### Etapa 1: Bloco de anotações do Google Colab

A primeira coisa que precisamos fazer é criar um novo notebook do Google Colab. Tudo o que você precisa é de uma conta do Google Drive para colocar isso em funcionamento. Você pode criar um novo notebook usando este link: [https://colab.research.google.com/#create=true](https://colab.research.google.com/#create=true)

Antes de começar a escrever qualquer comando, também precisamos ter certeza de que estamos usando a configuração da GPU como nosso tempo de execução (em vez de uma CPU padrão). Isso ocorre porque as GPUs são muito mais adequadas para lidar com tarefas de IA.

Clique em **Runtime** no menu superior do Colab e selecione **Change runtime type**. 
![](https://miro.medium.com/v2/resize:fit:1400/1*v-Bgbe67Q1bLl-l0nt7PXQ.png)

Na opção **Hardware accelerator**, selecione GPU e clique em **Save**.
![](https://miro.medium.com/v2/resize:fit:1400/1*m3PKdpdHSKpcPeQ-DNaDkg.png)

### Etapa 2: Instalar as bibliotecas necessárias

Nós precisamos das bibliotecas `whisper` e `youtube_dl`. Para instalar, use os comandos abaixo:

```python
!pip install git+https://github.com/openai/whisper.git
!sudo pip install git+https://github.com/ytdl-org/youtube-dl.git@master#egg=youtube_dl
```

### Etapa 3: Executar o script Python

Agora você pode copiar o script Python deste repositório e colá-lo em uma nova célula do Colab. Execute a célula.

### Etapa 4: Inserir o link do YouTube

O script irá solicitar que você insira o link do vídeo do YouTube. Após inserir, o script começará a fazer o download do áudio do vídeo e, em seguida, transcrever o áudio.

---

Feito por Alisson Ryan - Holy Writer - [https://holywriter.com.br](https://holywriter.com.br)
