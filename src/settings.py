URL_ASSYNC = "http://127.0.0.1:8000/anonymize"
URL_SYNC = "http://127.0.0.1:8000/anonymize_sync"
LOGIN_URL = "http://127.0.0.1:8000/login"
REGISTER_URL = "http://127.0.0.1:8000/register"

USERNAME = "teste01"
PASSWORD = "teste01"

RESULTS_PATH = "./tests/results/"

ERROR_SLEEP_TIME = 1

PAYLOAD_CONFIGURATION_1 = {
    "sensitive_columns": [
        "nome",
        "sobrenome",
        "email",
        "ip",
        "endereco",
        "rg",
        "cpf",
        "data_de_nascimento",
        "local_de_nascimento",
        "telefone",
        "celular",
        "titulo_de_eleitor",
        "ra_exercito",
    ],
    "diversity_columns": [
        "gender",
        "cidade",
        "estado"
    ],
    "closeness_columns": [
        "latitude",
        "longitude",
        "renda"
    ],
    "execution_parameters": [
        {
            "algorithm": "mask.full",
            "columns": [
                "nome",
                "sobrenome",
                "email",
                "ip",
                "endereco",
                "rg",
                "cpf",
                "data_de_nascimento",
                "local_de_nascimento",
                "telefone",
                "celular",
                "titulo_de_eleitor",
                "ra_exercito",
                "anamnese",
                "plano_terapeutico",
                "laudo_exames",
                "prescricao_medica",
                "evolucao_quadro_clinico",
                "trajetoria_clinica",
                "historico_pagamentos",
                "habitos_consumo",
                "preferencias_lazer",
                "origem_etnica",
                "religiao",
                "filiacao_politica",
                "orientacao_sexual",
                "biometria"
            ]
        }
    ]
}

PAYLOAD_CONFIGURATION_2 = {
    "execution_parameters": [
        {
            "algorithm": "mask.full",
            "columns": [
                "nome",
                "sobrenome",
                "endereco",
                "local_de_nascimento"
            ]
        },
        {
            "algorithm": "mask.email",
            "columns": [
                "email"
            ]
        },
        {
            "algorithm": "mask.last_n_characters",
            "configuration": {
                "n": 7
            },
            "columns": [
                "telefone",
                "celular"
            ]
        },
        {
            "algorithm": "mask.last_n_characters",
            "configuration": {
                "n": 12
            },
            "columns": [
                "ip",
                "titulo_de_eleitor"
            ]
        },
        {
            "algorithm": "mask.first_n_characters",
            "configuration": {
                "n": 8
            },
            "columns": [
                "rg",
                "ra_exercito"
            ]
        },
        {
            "algorithm": "mask.cpf",
            "columns": [
                "cpf"
            ]
        },
        {
            "algorithm": "perturb.date",
            "configuration": {
                "unit": "days",
                "min_value": 1,
                "max_value": 30
            },
            "columns": [
                "data_de_nascimento"
            ]
        },
        {
            "algorithm": "perturb.numeric_range",
            "configuration": {
                "min_value": 100,
                "max_value": 500
            },
            "columns": [
                "renda"
            ]
        },
        {
            "algorithm": "perturb.numeric_gaussian",
            "configuration": {
                "std": 0.5
            },
            "columns": [
                "latitude"
            ]
        },
        {
            "algorithm": "perturb.numeric_laplacian",
            "configuration": {
                "value": 3
            },
            "columns": [
                "longitude"
            ]
        }
    ],
    "sensitive_columns": [
        "nome",
        "sobrenome",
        "endereco",
        "local_de_nascimento"
    ],
    "diversity_columns": [
        "gender",
        "cidade",
        "estado"
    ],
    "closeness_columns": [
        "latitude",
        "longitude",
        "renda"
    ]
}

PAYLOAD_CONFIGURATION_3 = {
    "execution_parameters": [
        {
            "algorithm": "encrypt.aes",
            "configuration": {
                "key": "secret_key"
            },
            "columns": [
                "nome",
                "sobrenome",
                "email",
                "gender",
                "ip",
                "endereco",
                "cidade",
                "estado",
                "rg",
                "cpf",
                "data_de_nascimento",
                "local_de_nascimento",
                "telefone",
                "celular",
                "cartao_de_credito",
                "titulo_de_eleitor",
                "ra_exercito",
                "nacionalidade",
                "anamnese",
                "plano_terapeutico",
                "laudo_exames",
                "prescricao_medica",
                "evolucao_quadro_clinico",
                "trajetoria_clinica",
                "historico_pagamentos",
                "habitos_consumo",
                "preferencias_lazer",
                "origem_etnica",
                "religiao",
                "filiacao_politica",
                "orientacao_sexual",
                "biometria"
            ]
        },
        {
            "algorithm": "perturb.numeric_gaussian",
            "configuration": {
                "std": 0.1
            },
            "columns": [
                "latitude",
                "longitude",
                "renda"
            ]
        }
    ],
    "sensitive_columns": [
        "nome",
        "sobrenome",
        "email",
        "gender",
        "ip",
        "endereco",
        "cidade",
        "estado",
        "rg",
        "cpf",
        "data_de_nascimento",
        "local_de_nascimento",
        "telefone",
        "celular",
        "cartao_de_credito",
        "titulo_de_eleitor",
        "ra_exercito",
        "nacionalidade",
        "anamnese",
        "plano_terapeutico",
        "laudo_exames",
        "prescricao_medica",
        "evolucao_quadro_clinico",
        "trajetoria_clinica",
        "historico_pagamentos",
        "habitos_consumo",
        "preferencias_lazer",
        "origem_etnica",
        "religiao",
        "filiacao_politica",
        "orientacao_sexual",
        "biometria"
    ],
    "diversity_columns": [
        "nome",
        "sobrenome",
        "email",
        "gender",
        "ip",
        "endereco",
        "cidade",
        "estado",
        "rg",
        "cpf",
        "data_de_nascimento",
        "local_de_nascimento",
        "telefone",
        "celular",
        "cartao_de_credito",
        "titulo_de_eleitor",
        "ra_exercito",
        "nacionalidade",
        "anamnese",
        "plano_terapeutico",
        "laudo_exames",
        "prescricao_medica",
        "evolucao_quadro_clinico",
        "trajetoria_clinica",
        "historico_pagamentos",
        "habitos_consumo",
        "preferencias_lazer",
        "origem_etnica",
        "religiao",
        "filiacao_politica",
        "orientacao_sexual",
        "biometria"
    ],
    "closeness_columns": [
        "latitude",
        "longitude",
        "renda"
    ]
}
