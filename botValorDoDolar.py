from apscheduler.schedulers.blocking import BlockingScheduler
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def valorDoDolar():

    try:
        # Configurações do Chrome
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        driver = webdriver.Chrome(options=chrome_options)
        print("Script Iniciado")

        # Navega até a página que exibe o valor do dolar
        driver.get("https://wise.com/br/currency-converter/usd-to-brl-rate")

        # Espera ate o elemento seja visivel na tela e pega o Xpath do elemento
        elementoDolar = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/main/section/div[3]/section[2]/section/div/div[1]/div[1]/h3[2]/span[3]"))
        )

        # Obtém o valor do dólar da página e remove espaços em brancos extras
        dolarObtidoString = elementoDolar.get_attribute("innerHTML").strip()
        print("Valor do dolar encontrado!")

        # Substitui a vírgula por um ponto e converte para float
        dolarObtidoString = dolarObtidoString.replace(",", ".")  # Substitui vírgula por ponto
        dolarObtido = float(dolarObtidoString) # Converte pra float

        # Formatar número
        dolarFormatado = "{:,.2f}".format(dolarObtido)

        # Emprimir o valor atual do dolar
        print("Esse é o valor atual do dolar: R$: " + dolarFormatado)

        # Fecha o navegador após a conclusão do script.
        driver.quit()
        print("Script Encerrado!")
    except Exception as e:
        print("Erro:", e)

# Cria um objeto scheduler
scheduler = BlockingScheduler()

# Executa o script a cada 10 minutos
scheduler.add_job(valorDoDolar, 'interval', seconds=60)

# Inicia o scheduler
scheduler.start()