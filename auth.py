from requests import post, Response
import json
import os


def find_email(email: str):
    if email:
        return email
    else:
        env = "POEMWIKI_EMAIL"
        email = os.environ.get(env)
        if not email:
            print("Failed to found email with env[{}]".format(env))
            quit(0)
        return email


def find_psw(psw: str):
    if psw:
        return psw
    else:
        env = "POEMWIKI_PSW"
        psw = os.environ.get(env)
        if not psw:
            print("Failed to found password with env[{}]".format(env))
            quit(0)
        return psw


def get_auth(email: str = None, psw: str = None):
    email = find_email(email)
    psw = find_psw(psw)

    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    data = json.dumps({"email": email, "password": psw})
    res: Response = post(
        "https://poemwiki.org/api/v1/user/login", headers=headers, data=data
    )
    status_code = res.status_code
    if status_code != 200:
        content = res.content
        print(
            "Failed to get auth: status_code={}, content={}".format(
                status_code, content
            )
        )
        quit()
    res_json = res.json()
    token = res_json["data"]["access_token"]
    return token


if __name__ == "__main__":
    auth = get_auth()
    print(auth)
