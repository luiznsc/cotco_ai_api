# SPRINT 4 | COT&CO | 2TDSPT
Entrega da sprint 4 | DISRUPTIVE ARCHITECTURES: IT, IOB & IA
> [!NOTE]
>INTEGRANTES<br>
> Nome: Eduardo Fagundes Correa | RM: 97195 <BR>
> Nome: Murilo Ariel Reis | RM: 97002 <BR>
> Nome: Luiz Henrique de Jesus do Nascimento | RM: 96335 <BR>
> Nome: Samuel Enderson Lima da Silva | RM: 96677 <BR>

---
## DOCUMENTAÇÃO DA API
#### FUNCIONALIDADES:
> - Receber valores para análise de dados - Nome do Produto e Arquivo CSV<BR>
> - Enviar resultado da análise de dados - JSON

> [!IMPORTANT]
> **Deverá ter instalado o Flask na máquina.** <BR>
> "pip install flask" <BR>
> <BR>
> **Deverá ser usado URL:** <BR>
> URL: http://127.0.0.1:5000 <BR>
> <BR>
> **Rodando API** <BR>
> Abrir a pasta do projeto no terminal; <BR>
> rodar o comando: python app.py <BR>
![image](https://github.com/luiznsc/cotco_ai_api/assets/111553441/68d6b5de-a44c-426e-bcbc-bb71854ab766)

  ---
  
### :page_with_curl:  Resultado da análise
- **URL:** /analise
- **Método:** GET
- **Descrição:** Buscar o resultado da análise de um csv.
- **Códigos de Status:**
  - :white_check_mark: 200 (Created) - Análise gerada com sucesso.
  -  :warning: 400 (Bad Request) - Dados enviados incorreto/incompletos.

![image](https://github.com/luiznsc/cotco_ai_api/assets/111553441/14c9f908-cc18-4870-ab6f-5feb2a774de2)


  ---
