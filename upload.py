from auth import get_auth
from requests import Response, post
import json
from typing import List


class Poem:
    def __init__(self, title: str, poet: str, content: str) -> None:
        if not title or not content:
            raise Exception("invalid content or title")
        self.title = title
        self.poet = poet
        self.content = content

    def to_dict(self) -> dict:
        return {"title": self.title, "poet": self.poet, "poem": self.content}


def upload(poems: List[Poem]):
    auth = get_auth()
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer {}".format(auth),
    }
    poem_dict: List[dict] = map(lambda p: p.to_dict(), poems)
    res: Response = post(
        "https://poemwiki.org/api/v1/poem/import",
        headers=headers,
        data=json.dumps({"poems": poem_dict}),
    )
    status_code = res.status_code
    if res.status_code != 200:
        raise Exception("Failed with status {}".format(status_code))
