import re
import random

respostas = {
    r"oi|olá|e aí|eae|eai|opa": ["Olá", "Oi", "E aí, tudo bem?", "Opa, tudo certo?"],
    r"como você está\??|você está bem\??|como tem estado\??": ["Estou bem, e você?", "Tenho estado bem, obrigado", "Tudo certo, e com você?"],
    r"como é o seu nome\??|como você se chama\??|quem é você\??": ["Meu nome é Pyman, muito prazer.", "Eu sou o Pyman, prazer em conhecer!"],
    r"o que você faz\??|qual a sua função\??": ["Eu ajudo os usuários a entenderem melhor a plataforma e como utilizá-la da maneira que lhes for útil", "Minha função é te ajudar a navegar pela plataforma da melhor maneira", "Eestou aqui para te ajudar a utlizar a plataforma, qual a sua dúvida?"],
    r"tchau|até mais|até a próxima|adeus|até logo|falou": ["Tchau, foi um prazer ajudar!", "Até mais, quando precisar estou aqui!", "Até logo, foi bom falar com você."]
}