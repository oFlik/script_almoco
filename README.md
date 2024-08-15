
# Preenche Refeição

Este projeto consiste em um programa para a automação do preenchimento de formulários no google drive.

Sua necessidade surgiu da necessidade diára de efetuar um procedimento repetitivo que consumia tempo e ocasionava o acúmulo de demandas.



## Tecnologias utilizadas
![image](https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

![image](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white)

![image](https://img.shields.io/badge/Google%20Sheets-34A853?style=for-the-badge&logo=google-sheets&logoColor=white)


## Executando localmente

Clone o projeto

```bash
  git clone https://github.com/oFlik/script_almoco.git
```

Vá até a pasta do projeto

```bash
  cd preenche_refeicao
```

Crie um novo ambiente virtual e o ative

```bash
  py -m venv venv
  .venv\Scripts\activate
```

Instale as dependências

```bash
  py -m pip install -r requirements.txt
```

Então escolha uma das opções abaixo:

1ª -  Execute via linha de comando

```bash
  py ./app.py
```

ou 
 
2ª - 
Utilize pyinstaller para criar um novo arquivo executável.

```bash
  pyinstaller --noconfirm .\PreencheRefeicao.spec
```
## Instalação

Alternativamente, é possível baixar apenas o arquivo executável, juntamente com seus binários de apoio na aba de Releases.

O mesmo se encontra compactando em um arquivo .rar.
## Roadmap

- Informações de preenchimento dinâmicas
- Interface de usuário
- Integração com outros formulários


## FAQ

#### O que é o Preenche Refeição

Começou apenas com um script rápido para automação de uma tarefa repetitiva (o preenchimento diário de uma planilha do google), porém com o desenvolvimento contínuo está se tornando uma ferramenta de preenchimento automático para formulários em geral.

#### Para quem este programa serve?

No estágio atual, por se tratar da resolução de uma demanda específica, apenas aos meus companheiros de trabalho, porém é de meu maior interesse disponibilizar o programa para qualquer formulário google.



## Considerações finais

Este é um projeto simples, porém que me trouxe diversos aprendizados, cada linha foi detalhadamente pensada e posicionada pessoalmente por mim para melhor desempenho e legibilidade do código.

Aprendi na prática a utilizar os frameworks: Selenium e Pyinstaller, com os quais nunca havia trabalhado.

Foi (bastante) desafiador, porém os conhecimentos adquiridos estão enraizados em mim para sempre.