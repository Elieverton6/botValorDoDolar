# Bot de Consulta do Valor do Dólar

Este é um bot em Python que consulta automaticamente o valor atual do dólar (USD) em reais (BRL) de um site específico. Ele utiliza a biblioteca Selenium para automatizar a extração dos dados da página da web e imprime o valor do dólar no console.

## Funcionalidades

- **Consulta Automática**: O bot acessa periodicamente uma página da web para obter o valor atual do dólar.
- **Extração de Dados**: Utilizando o Selenium, o bot extrai o valor do dólar da página da web.
- **Formatação de Dados**: O valor do dólar é formatado corretamente antes de ser exibido.
- **Log de Mensagens**: O bot imprime mensagens informativas no console para indicar o início, conclusão e quaisquer erros durante o processo.

## Requerimentos

- **Python 3.x**: É necessário ter Python 3 instalado no ambiente de execução.
- **Selenium**: A biblioteca Selenium é utilizada para automação do navegador.
- **WebDriver para Chrome**: O WebDriver específico para o navegador Chrome é necessário para permitir a interação automatizada com o navegador.

## Instalação e Uso

1. **Instalação de Dependências**: Execute `pip install selenium` para instalar a biblioteca Selenium.

2. **Configuração do WebDriver**: Baixe o WebDriver para o Chrome e atualize o caminho no script onde indicado.

3. **Execução do Script**: Execute o script Python e o bot começará a consultar automaticamente o valor do dólar.

Certifique-se de que o caminho do WebDriver esteja corretamente configurado para garantir o funcionamento adequado do bot.

## Exemplo de Uso

```bash
python valor_do_dolar.py
