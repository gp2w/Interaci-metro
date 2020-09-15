# Interaciômetro

## Description

This repository contains the source code for searching a Twitter's user interaction data. The application can be accessed in [interaciometro.herokuapp.com](https://interaciometro.herokuapp.com/).

## Requirements

All dependencies to build up the application on localhost can be installed using [requirements.txt](requirements.txt) file.

A developer account on Twitter is necessary to run the code localy. The develop Twitter tokens must be inserted on [.env.example](.env.example) file, which must be renamed to only `.env`. Tokens can also be added as OS environment variables.

## Local running 

Run `app.py` file and go to your machine's localhost address on port 8050 (for exemple, [127.0.0.1:8050](http://127.0.0.1:8050/))

## Usage

On browser, the user must insert a Twitter's username and hit "Buscar" button. After some research time it will be shown a table with the users with most interactions, highlighting the number of likes, replies and retweet, together with a score based on those three values.

Besides that, two graphs are shown, one showing together the number of likes, replies and retweets, and the other showing the score. Filters applied on the table are reflected on graphs.

## License

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
