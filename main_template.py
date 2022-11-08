import json
from common import BatchIterator
from upload import Poem, upload

with open("origin/PortuguesePoems.json", "r") as file:
    # 1. read poem array
    data = json.load(file)
    # 2. initiliaze one BatchIterator(capcity, batch_process_func, sleep_duration)
    iterator = BatchIterator(200, upload, 5)
    for poem in data:
        # 3. convert to Poem
        poet = poem["poet_name"]
        title = poem["title"]
        content = poem["content"]
        # 4. append into the BatchIterator
        iterator.iterate(Poem(title, poet, content))
    # 5. tail process
    iterator.tail()
