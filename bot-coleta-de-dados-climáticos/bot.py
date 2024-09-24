"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/web/
"""


# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

bot = WebBot()

# ------------------------------------------------------------------------------- Manaus ---------------------------------------------------------------------------------------
def dados_clima_manaus(bot, lidar_com_cookies=True):
    bot.browse("https://weather.com/pt-BR/clima/10dias/l/cfa996baf3b36644dd756369dc7afcc16bfab91c7561b06a43bd832bb0d67dfc")

    bot.sleep(1000)
    
    if not bot.find("cookies", matching=0.97, waiting_time=10000):
       not_found("cookies")
    bot.click()

    bot.sleep(2000)

    dados = []

    for i in range(1, 11):
    
        bot.find_element(f'//*[@id="detailIndex{i}"]/summary/div/div/h2', By.XPATH).click()

    
        dia = bot.find_element(f'//*[@id="detailIndex{i}"]/div/div[1]/h2/span', By.XPATH).text
        max_temp = bot.find_element(f'//*[@id="detailIndex{i}"]/div/div[1]/div/div[1]/span', By.XPATH).text
        min_temp = bot.find_element(f'//*[@id="detailIndex{i}"]/div/div[3]/div/div[1]/span', By.XPATH).text
        umidadeDia = bot.find_element(f'//*[@id="detailIndex{i}"]/div/div[2]/ul/li[1]/div/span[2]', By.XPATH).text
        umidadeNoite = bot.find_element(f'//*[@id="detailIndex{i}"]/div/div[4]/ul/li[1]/div/span[2]', By.XPATH).text
        uvD = bot.find_element(f'//*[@id="detailIndex{i}"]/div/div[2]/ul/li[2]/div/span[2]', By.XPATH).text
        uvN = bot.find_element(f'//*[@id="detailIndex{i}"]/div/div[4]/ul/li[2]/div/span[2]', By.XPATH).text

        print(f'\nDia: {dia}, max: {max_temp}, min: {min_temp}, umidade: dia: {umidadeDia}, noite: {umidadeNoite}, índice UV: dia: {uvD}, noite: {uvN}\n')

        dados.append({
                'Dia': dia,
                'Temp. maxima': max_temp,
                'Tem. minima ': min_temp,
                'Umidade do dia': umidadeDia,
                'Umidade da noite': umidadeNoite,
                'Índice UV do dia': uvD,
                'Índice UV da noite': uvN
            })

   
    salvar_em_excel_manaus(dados)

def salvar_em_excel_manaus(dados):
   
    df = pd.DataFrame(dados)

    df.to_excel('dados_clima_manaus.xlsx', index=False, engine='openpyxl')

    print("Dados salvos em 'dados_clima_manaus.xlsx' com sucesso!")
        

def ler_dados_excel_manaus(arquivo):
    df = pd.read_excel(arquivo, engine='openpyxl')
    return df

def criar_graficos_manaus(df):

    sns.set(style="whitegrid")

    plt.figure(figsize=(12, 6))
    
    
    bar_width = 0.35
    x = range(len(df))

    # Gráfico de Temperaturas Máximas
    plt.bar(x, df['Temp. maxima'], width=bar_width, color='orange', label='Temperatura Máxima')

    # Gráfico de Temperaturas Mínimas
    plt.bar([p + bar_width for p in x], df['Tem. minima '], width=bar_width, color='blue', label='Temperatura Mínima')

    # Configurações do gráfico
    plt.title('Temperaturas Máximas e Mínimas por Dia')
    plt.xlabel('Dia')
    plt.ylabel('Temperatura (°C)')
    plt.xticks([p + bar_width / 2 for p in x], df['Dia'], rotation=45)  
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Gráfico de Umidade
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Dia', y='Umidade do dia', data=df, marker='o', label='Umidade Dia') 
    sns.lineplot(x='Dia', y='Umidade da noite', data=df, marker='o', label='Umidade Noite')  
    plt.title('Umidade por Dia')
    plt.xlabel('Dia')
    plt.ylabel('Umidade (%)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Gráfico de Índice UV
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Dia', y='Índice UV do dia', data=df, marker='o', label='UV Dia')  
    sns.lineplot(x='Dia', y='Índice UV da noite', data=df, marker='o', label='UV Noite')  
    plt.title('Índice UV por Dia')
    plt.xlabel('Dia')
    plt.ylabel('Índice UV')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()
  
  # -------------------------------------------------------------------------------São Paulo -----------------------------------------------------------------------


def dados_clima_saopaulo(bot):
    bot.browse("https://weather.com/pt-BR/clima/10dias/l/dfb390d5d0537ed3c80f13693bce4fb5ab75fb5fa1ddd5c46fb61fc04264005d")

    bot.sleep(2000)

    dados = []

    for i in range(1, 11):
    
        bot.find_element(f'//*[@id="detailIndex{i}"]/summary/div/div/h2', By.XPATH).click()

    
        dia = bot.find_element(f'//*[@id="detailIndex{i}"]/div/div[1]/h2/span', By.XPATH).text
        max_temp = bot.find_element(f'//*[@id="detailIndex{i}"]/div/div[1]/div/div[1]/span', By.XPATH).text
        min_temp = bot.find_element(f'//*[@id="detailIndex{i}"]/div/div[3]/div/div[1]/span', By.XPATH).text
        umidadeDia = bot.find_element(f'//*[@id="detailIndex{i}"]/div/div[2]/ul/li[1]/div/span[2]', By.XPATH).text
        umidadeNoite = bot.find_element(f'//*[@id="detailIndex{i}"]/div/div[4]/ul/li[1]/div/span[2]', By.XPATH).text
        uvD = bot.find_element(f'//*[@id="detailIndex{i}"]/div/div[2]/ul/li[2]/div/span[2]', By.XPATH).text
        uvN = bot.find_element(f'//*[@id="detailIndex{i}"]/div/div[4]/ul/li[2]/div/span[2]', By.XPATH).text

        print(f'\nDia: {dia}, max: {max_temp}, min: {min_temp}, umidade: dia: {umidadeDia}, noite: {umidadeNoite}, índice UV: dia: {uvD}, noite: {uvN}\n')

        dados.append({
                'Dia': dia,
                'Temp. maxima': max_temp,
                'Tem. minima ': min_temp,
                'Umidade do dia': umidadeDia,
                'Umidade da noite': umidadeNoite,
                'Índice UV do dia': uvD,
                'Índice UV da noite': uvN
            })

   
    salvar_em_excel_saopaulo(dados)
     
 
def salvar_em_excel_saopaulo(dados):
   
    df = pd.DataFrame(dados)

    df.to_excel('dados_clima_saopaulo.xlsx', index=False, engine='openpyxl')

    print("Dados salvos em 'dados_clima_saopaulo.xlsx' com sucesso!")
        

def ler_dados_excel_saopaulo(arquivo):
    df = pd.read_excel(arquivo, engine='openpyxl')
    return df

def criar_graficos_saopaulo(df):

    sns.set(style="whitegrid")

    plt.figure(figsize=(12, 6))
    
    
    bar_width = 0.35
    x = range(len(df))

    # Gráfico de Temperaturas Máximas
    plt.bar(x, df['Temp. maxima'], width=bar_width, color='orange', label='Temperatura Máxima')

    # Gráfico de Temperaturas Mínimas
    plt.bar([p + bar_width for p in x], df['Tem. minima '], width=bar_width, color='blue', label='Temperatura Mínima')

    # Configurações do gráfico
    plt.title('Temperaturas Máximas e Mínimas por Dia')
    plt.xlabel('Dia')
    plt.ylabel('Temperatura (°C)')
    plt.xticks([p + bar_width / 2 for p in x], df['Dia'], rotation=45)  
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Gráfico de Umidade
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Dia', y='Umidade do dia', data=df, marker='o', label='Umidade Dia') 
    sns.lineplot(x='Dia', y='Umidade da noite', data=df, marker='o', label='Umidade Noite')  
    plt.title('Umidade por Dia')
    plt.xlabel('Dia')
    plt.ylabel('Umidade (%)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Gráfico de Índice UV
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Dia', y='Índice UV do dia', data=df, marker='o', label='UV Dia')  
    sns.lineplot(x='Dia', y='Índice UV da noite', data=df, marker='o', label='UV Noite')  
    plt.title('Índice UV por Dia')
    plt.xlabel('Dia')
    plt.ylabel('Índice UV')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()
    


def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.CHROME

    # Uncomment to set the WebDriver path
    bot.driver_path = ChromeDriverManager().install()


   

    # Implement here your logic...
    dados_clima_manaus(bot)
    arquivo_excel = 'dados_clima_manaus.xlsx'
    dados = ler_dados_excel_manaus(arquivo_excel)
    criar_graficos_manaus(dados)

    dados_clima_saopaulo(bot)
    arquivo_excel = 'dados_clima_saopaulo.xlsx'
    dados = ler_dados_excel_saopaulo(arquivo_excel)
    criar_graficos_saopaulo(dados)


 
    bot.wait(5000)
    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
