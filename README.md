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

### Análise dos resultados

A análise dos tempos de execução de cada uma das suas funções revela informações importantes sobre a eficiência de diferentes abordagens e bibliotecas para fazer requisições HTTP em Python. Vamos discutir cada uma delas:

1. **`lib_request` (8.19 segundos, 31.31 MiB)**:
    
    * Esta é a implementação mais lenta e também a que mais consome memória. Isso ocorre porque `lib_request` utiliza a biblioteca `requests` sem sessão, fazendo com que cada requisição estabeleça uma nova conexão. Isso resulta em maior latência e maior uso de memória devido ao overhead de estabelecer conexões e gerenciar recursos separadamente para cada requisição.
2. **`lib_request_session` (1.91 segundos, 0.31 MiB)**:
    
    * A utilização de sessões com `requests` melhora drasticamente o tempo de execução e reduz significativamente o uso de memória. Isso se deve à reutilização de conexões TCP, que reduz o overhead de rede e melhora a eficiência geral das requisições.
3. **`lib_httpx` (5.75 segundos, 17.67 MiB)**:
    
    * `lib_httpx` utiliza a biblioteca `httpx` de forma síncrona e sem sessão. Embora seja mais rápida que `lib_request`, ainda é menos eficiente do que as implementações com sessão. Isso sugere que, enquanto `httpx` pode ter algumas otimizações internas em comparação com `requests`, a ausência de sessões ainda resulta em tempos de execução mais longos e maior uso de memória.
4. **`lib_httpx_session` (1.95 segundos, 0.39 MiB)**:
    
    * Similar à `lib_request_session`, a versão com sessão de `httpx` mostra uma melhoria significativa em termos de tempo de execução e uso de memória. Isso reforça a importância da reutilização de conexões para melhorar a eficiência das requisições HTTP.
5. **`lib_httpx_session_async` (0.89 segundos, 7.42 MiB)** e **`lib_aiohttp_session_async` (0.79 segundos, 13.45 MiB)**:
    
    * Estas são as implementações mais rápidas, aproveitando a natureza assíncrona de `httpx` e `aiohttp` com sessões. A capacidade de fazer várias requisições simultaneamente de forma não bloqueante explica os tempos de execução significativamente mais curtos. No entanto, isso vem com um custo de uso de memória mais alto devido ao gerenciamento de múltiplas operações concorrentes.

### Detalhe do uso de memória

As versões com sessão (lib_request_session e lib_httpx_session) apresentam um uso de pico de memória significativamente menor do que as outras, podem ser explicados por algumas características fundamentais do gerenciamento de conexões e sessões nas bibliotecas requests e httpx:

**Reutilização de Conexões:** Quando você usa sessões em requests ou httpx, a conexão TCP estabelecida com o servidor é reutilizada para várias requisições. Isso reduz o overhead de abrir e fechar conexões TCP para cada requisição individual. Abrir e fechar conexões repetidamente (como no caso sem sessão) consome mais memória devido ao overhead de estabelecer novas conexões TCP e ao armazenamento temporário de dados associados a cada conexão.

**Eficiência no Gerenciamento de Recursos:** As sessões gerenciam eficientemente os recursos como sockets e buffers internos. Em contraste, realizar requisições sem sessão pode resultar em um uso menos eficiente desses recursos, pois cada requisição trata seus próprios recursos de rede de forma isolada.

**Menos Overhead de Alocação de Memória:** Usar sessões significa que menos objetos são criados e destruídos durante o processo de fazer várias requisições, o que leva a um menor overhead de alocação de memória. Sem sessões, cada requisição precisa criar seus próprios objetos de conexão, headers, cookies, etc., o que aumenta o uso de memória.

**Menor Carga de I/O:** Ao reutilizar conexões, as sessões podem reduzir a carga geral de I/O, pois menos operações de rede são necessárias. Menos I/O geralmente se traduz em menos uso de memória.

Uso de Memória em Requisições Assíncronas: As versões assíncronas (lib_httpx_session_async e lib_aiohttp_session_async) mostram um maior uso de memória porque gerenciam várias requisições em paralelo, o que naturalmente exige mais recursos de memória para manter o estado de múltiplas operações simultâneas.

O uso de sessões otimiza o processo de fazer várias requisições HTTP ao reutilizar conexões e gerenciar recursos de forma mais eficiente. Isso explica por que as versões com sessão têm um pico de uso de memória significativamente menor em comparação com as versões sem sessão ou as assíncronas, que lidam com requisições de maneira isolada ou simultânea, respectivamente.

### Conclusão

* A utilização de sessões é crucial para otimizar tanto o tempo de execução quanto o uso de memória em requisições HTTP, como demonstrado pelas implementações `lib_request_session` e `lib_httpx_session`.
* Para operações de I/O-bound, como requisições de rede, as abordagens assíncronas (`lib_httpx_session_async` e `lib_aiohttp_session_async`) são significativamente mais rápidas, embora exijam mais memória devido à natureza concorrente.
* Em geral, escolher a abordagem certa depende do equilíbrio entre a eficiência de tempo de execução e o uso de recursos, como memória, com base nas necessidades específicas da aplicação.

### Literatura

- [Real Python](https://realpython.com/python-concurrency/)
- [Arjan Codes](https://www.youtube.com/watch?v=OPyoXx0yA0I)