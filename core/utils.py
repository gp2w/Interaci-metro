import json
import logging

logging.basicConfig(format='[%(levelname)s][%(asctime)s]: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.INFO)


def to_json(obj, filename):
    filename = filename.replace('@', '')
    logging.info(f'Criando o arquivo {filename}.json')
    with open(f'{filename}.json', 'w') as writer:
        json.dump(obj, writer, indent=3, ensure_ascii=False)
    logging.info(f'{filename}.json criado.')
