import requests
import json

url = 'https://petstore.swagger.io/v2/pet'

def test_incluir_pet(): # Add new
    # Configura

    headers = {'content-Type': 'application/json'}
    status_code_esperado = 200      # Comunicação

    # Executa
    resposta = requests.post(url,
                             data=open('json/pet.json', 'rb'),
                             headers=headers)
    print(resposta)
    print(resposta.status_code)
    print(json.dumps(resposta.json(), indent=2))

    # Valida
    assert resposta.status_code == status_code_esperado

def testar_get_pet(): # busca pelo ID
     # Configura

    headers = {'content-Type': 'application/json'}
    pet_id = 1976060733
    cat_name_esperado = {'id': 1, 'name': 'welita45sucesso'}
    pet_name_esperado = 'Lobo'
    tag_tipo_esperado =[{'id': 2021, 'name': 'sta'}]
    status_esperado = 'available'
    status_code_esperado = 200


    #executa
    resposta = requests.get(f'{url}/{pet_id}', headers=headers)
    corpo_da_resposta = resposta.json()
    print(corpo_da_resposta)
    print(resposta.status_code)
    print(json.dumps(resposta.json(), indent=2))

    #valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['category'] == cat_name_esperado
    assert corpo_da_resposta['name'] == pet_name_esperado
    assert corpo_da_resposta['status'] == status_esperado
    assert corpo_da_resposta['tags'] == tag_tipo_esperado

def testar_alterar_pet(): # Put
    # configura

    headers = {'content-Type': 'application/json'}
    status_code_esperado = 200  # comunicação

    # executa
    resposta = requests.post(url,
                             data=open('json/pet2.json', 'rb'),
                             headers=headers)
    print(resposta)
    print(resposta.status_code)
    print(json.dumps(resposta.json(), indent=2))

    # valida
    assert resposta.status_code == status_code_esperado

def testar_excluir_pet(): # deletar
    # Configura

    headers = {'Content-Type': 'application/json'}
    pet_id = '51123756'
    status_code_esperado = 200  # comunicação

    # Executa
    resposta = requests.delete(f'{url}/{pet_id}', headers=headers)

    # Valida
    assert resposta.status_code == status_code_esperado