# Email Reader

Este script em Python permite conectar-se a uma conta de email via IMAP, buscar por emails não lidos na caixa de entrada e retornar uma lista com os assuntos desses emails.

## Configurações
As seguintes variáveis de ambiente devem ser definidas no arquivo .env na raiz do projeto:

- `IMAP_SERVER`: o endereço do servidor IMAP.
- `EMAIL`: o email da conta que será usada para acessar o servidor IMAP.
- `PASSWORD`: a senha da conta que será usada para acessar o servidor IMAP.

## Dependências
As dependências do projeto podem ser instaladas usando o gerenciador de pacotes pipenv através do comando:
    `pipenv install`


## Como usar
Para rodar o script, execute o seguinte comando:
    `pipenv run python3 run.py`

O script irá buscar por emails não lidos na caixa de entrada e retornar uma lista com os assuntos desses emails. Os emails encontrados serão marcados como lidos.

## Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.