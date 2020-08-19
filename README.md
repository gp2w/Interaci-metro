# Interaciômetro

## Descrição

Este repositório contém o código fonte para consulta de dados de interação para um usuário do Twitter. A aplicação pode ser acessada em [interaciometro.herokuapp.com](https://interaciometro.herokuapp.com/).

## Requisitos

Todas as dependências para levantar a aplicação localmente podem ser instaladas usando o arquivo [requirements.txt](requirements.txt).

Uma conta de desenvolvedor no Twitter é necessária para a execução local do código. Os _tokens_ gerados pelo Twitter devem ser inseridos no arquivo [.env.example](.env.example) de exemplo, que deve ser renomeado para apenas `.env`. Os _tokens_ também podem ser inseridos em variáveis de ambiente do sistema.

## Execução local

Rode o arquivo `app.py` e acesse o endereço do _localhost_ da sua máquina, na porta 8050 (por exemplo, [127.0.0.1:8050](http://127.0.0.1:8050/)).

## Uso

No navegador, o usuário deve inserir um nome de usuário do twitter e clicar em "Buscar". Após um tempo para consulta será exibida uma tabela listando os usuários que o usuário buscado interagiu mais recentemente, destacando a quantidade de curtidas, respostas e _retweets_, bem como um _score_ baseado nos três valores citados.

Além disso, dois gráficos são exibidos, um exibindo simultaneamente a quantidade de curtidas, respostas e _retweets_, e o outro mostrando o _score_. Filtros aplicados na tabela são refletidos nos gráficos.

## Licença

   Copyright 2020 Geandreson Costa, Pedro Nascimento, Wesler Sales & Weverson Nascimento

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
