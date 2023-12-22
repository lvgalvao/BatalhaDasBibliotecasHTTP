# Batalha das Bibliotecas HTTP em Python

Este projeto visa comparar diferentes bibliotecas HTTP em Python em termos de desempenho (tempo de execução) e uso de memória. As bibliotecas testadas incluem `requests`, `httpx` (com e sem sessões), e `aiohttp`.

## Objetivo

O principal objetivo deste projeto é fornecer insights práticos sobre o desempenho de várias bibliotecas HTTP populares em Python. Isso pode ajudar desenvolvedores a escolher a biblioteca mais adequada para suas necessidades específicas, levando em conta não apenas a facilidade de uso, mas também a eficiência em termos de tempo de resposta e consumo de memória.

## Bibliotecas Testadas

* **`requests`**: Uma biblioteca HTTP simples, porém poderosa.
* **`httpx`**: Uma biblioteca HTTP de próxima geração, com suporte para HTTP/1.1 e HTTP/2.
* **`aiohttp`**: Uma biblioteca HTTP assíncrona.

## Metodologia

Cada biblioteca foi utilizada para fazer requisições GET a um servidor de teste. Foram medidos o tempo de execução e o uso de memória para as seguintes abordagens:

1. Requisições síncronas sem sessão.
2. Requisições síncronas com sessão.
3. Requisições assíncronas com sessão.

## Módulos

1. **`usando_request` (`lib_request`)**:
    
    * Este módulo utiliza a biblioteca `requests` de maneira síncrona e sem sessão para realizar requisições HTTP GET.
    * Destaca-se pela simplicidade de uso, mas sem a eficiência de sessões, pode ter um desempenho mais lento e maior uso de memória.
2. **`usando_request_session` (`lib_request_session`)**:
    
    * Similar ao módulo `usando_request`, mas utiliza a biblioteca `requests` com sessões.
    * A reutilização de conexões em sessões melhora significativamente o tempo de execução e reduz o uso de memória.
3. **`usando_httpx` (`lib_httpx`)**:
    
    * Usa a biblioteca `httpx` de forma síncrona e sem sessão.
    * `httpx` é mais avançada e suporta HTTP/2, o que pode trazer vantagens em termos de desempenho em comparação com `requests`.
4. **`usando_httpx_session` (`lib_httpx_session`)**:
    
    * Usa a biblioteca `httpx` com sessões.
    * A gestão de sessões em `httpx` pode oferecer melhorias no desempenho e eficiência de memória, similar ao observado com `requests`.
5. **`usando_httpx_session_async` (`lib_httpx_session_async`)**:
    
    * Realiza requisições HTTP de maneira assíncrona usando `httpx` com sessões.
    * Esta abordagem assíncrona é mais eficiente em termos de tempo de execução, adequada para operações I/O-bound como requisições de rede.
6. **`usando_aiohttp_session_async` (`lib_aiohttp_session_async`)**:
    
    * Utiliza `aiohttp` de forma assíncrona com sessões.
    * `aiohttp` é otimizada para operações assíncronas e é uma escolha popular para aplicações que necessitam de alta performance em requisições HTTP.


## Como Executar

Para executar os testes, clone este repositório e instale as dependências:

```bash
git clone git@github.com:lvgalvao/BatalhaDasBibliotecasHTTP.git
cd BatalhaDasBibliotecasHTTP
pip install -r requirements.txt
```

Execute o script principal:

```bash
python main.py
```

## Resultado Final

```bash
Tempos de Execução e Uso de Memória:
lib_request: Tempo de execução: 8.19 segundos, Uso de memória: 31.31 MiB.
lib_request_session: Tempo de execução: 1.91 segundos, Uso de memória: 0.31 MiB.
lib_httpx: Tempo de execução: 5.75 segundos, Uso de memória: 17.67 MiB.
lib_httpx_session: Tempo de execução: 1.95 segundos, Uso de memória: 0.39 MiB.
lib_httpx_session_async: Tempo de execução: 0.89 segundos, Uso de memória: 7.42 MiB.
lib_aiohttp_session_async: Tempo de execução: 0.79 segundos, Uso de memória: 13.45 MiB.
```

Os resultados mostram uma variação significativa entre os módulos em termos de tempo de execução e uso de memória. Os módulos assíncronos (`lib_httpx_session_async` e `lib_aiohttp_session_async`) tendem a ter os melhores tempos de execução devido à sua capacidade de realizar múltiplas requisições simultaneamente, mas com um aumento no uso de memória.

Por outro lado, os módulos síncronos que utilizam sessões (`lib_request_session` e `lib_httpx_session`) mostram uma melhoria no desempenho em comparação com suas contrapartes sem sessão, evidenciando a eficiência da reutilização de conexões.

Esses resultados oferecem insights valiosos sobre as compensações entre diferentes abordagens de requisições HTTP em Python, destacando a importância de escolher a biblioteca e o método apropriados para as necessidades específicas de desempenho e eficiência de cada aplicação.