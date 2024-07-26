import asyncio  # Biblioteca para programação assíncrona em Python
from time import sleep  # Função para pausar a execução por um número de segundos
import httpx  # Biblioteca para fazer requisições HTTP
from django.http import HttpResponse  # Função para criar respostas HTTP

# Função assíncrona que realiza chamadas HTTP
async def http_call_async():
    # Loop que espera 1 segundo e imprime um número, repetido 6 vezes
    for num in range(0, 6):
        await asyncio.sleep(1)  # Pausa assíncrona por 1 segundo
        print(num)

    # Realiza uma requisição HTTP de forma assíncrona
    async with httpx.AsyncClient() as client:
        r = await client.get('<https://httpbin.org/>')  # Faz a requisição GET de forma assíncrona
        print(r)  # Imprime a resposta da requisição

# Função síncrona que realiza chamadas HTTP
def http_call_sync():
    # Loop que espera 1 segundo e imprime um número, repetido 6 vezes
    for num in range(0, 6):
        sleep(1)  # Pausa por 1 segundo
        print(num)

    # Realiza uma requisição HTTP de forma síncrona
    r = httpx.get('<https://httpbin.org/>')  # Faz a requisição GET de forma síncrona
    print(r)  # Imprime a resposta da requisição

# View assíncrona do Django
async def async_view(request):
    loop = asyncio.get_event_loop()  # Obtém o loop de eventos atual
    loop.create_task(http_call_async())  # Cria uma tarefa assíncrona para a função http_call_async
    return HttpResponse("Non-blocking HTTP request")  # Retorna uma resposta HTTP não bloqueante

# View síncrona do Django
def sync_view(request):
    http_call_sync()  # Chama a função síncrona http_call_sync
    return HttpResponse("Blocking HTTP request")  # Retorna uma resposta HTTP bloqueante
