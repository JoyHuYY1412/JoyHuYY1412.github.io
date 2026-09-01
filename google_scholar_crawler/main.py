from scholarly import scholarly
import json
from datetime import datetime
import os

SCHOLAR_AUTHOR_ID = 'o6h6sVMAAAAJ'


def main() -> None:
    author: dict = scholarly.search_author_id(SCHOLAR_AUTHOR_ID)
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
    author['updated'] = datetime.now().astimezone().isoformat()
    author['publications'] = {
        publication['author_pub_id']: publication
        for publication in author.get('publications', [])
    }

    print(json.dumps(author, indent=2, ensure_ascii=False))
    os.makedirs('results', exist_ok=True)
    with open('results/gs_data.json', 'w', encoding='utf-8') as outfile:
        json.dump(author, outfile, ensure_ascii=False)

    shieldio_data = {
        'schemaVersion': 1,
        'label': 'citations',
        'message': str(author.get('citedby', 0)),
    }
    with open('results/gs_data_shieldsio.json', 'w', encoding='utf-8') as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)


if __name__ == '__main__':
    main()
