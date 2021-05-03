# crawling
Este crawler consiste em dois exemplos de como podemos obter dados de páginas web com um simples programa feito em python e como podemos consumir esses dados e como podemos processar e analisa-los.

## JC web crawler
Como primeiro exemplo, utilizei o site do *Jornal do Comércio* para extrair informações das notícias da primeira página. Para rodar-mos o web crawler, precisamos acessar a pasta interna de noticias com o comando `cd noticias/noticias`. Destro da pasta iremos executar o comando `scrapy crawl jc -o noticias.json`. Esse comando executa o spider, que irá coletar os dados na página do jornal, e irá retornar um arquivo json com as informações coletadas. Após isso, criei um arquivo *analitico.py* que é responsável por utilizar o pandas e extrair algumas informações desse *json*, exportando as informações em um csv. Para executar o programa, iremos digitar o comando `python analitico.py`

## Quotes web crawler
Para complementar o projeto, fiz mais um crawler de um site que é bastante usado para estudos de web crawler, o *quotes.toscrape*. Nele, a idéia é a mesma do que foi feito no site do JC porém, eu faço uma abordagem diferente na análise dos dados. Já estando dentro da pasta noticias, o camndo é bem parecido com o crawler anterior, `scrapy crawl quotes -o noticias.json`. Ele irá retornar um *json* com todas as citações, autores e tags citadas. Após a coleta dessa informações iremos executar `python quotes.py`. Nesse programa eu também executo o pandas, importando as informações a partir do *json* e elenco quais tags foram mais citadas, retornando as 10 primeiras em um arquivo csv. 

## Considerações
Web Crawler é uma ferramenta bastante poderosa na área de ciência de dados, podemos extrair várias informações de forma automática e fazer análises poderosíssimas, trazendo insights podendo definir padrões de público que consome essas informações, análises de sentimentos, entre outros. Esse foi meu primeiro projeto de crawling.
