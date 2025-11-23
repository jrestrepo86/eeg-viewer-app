import os

from dash import Dash, Input, Output, callback, dcc, html
from dotenv import load_dotenv

load_dotenv(".env.dev")


app = Dash()

app.layout = [
    html.H1(children="Title of Dash App", style={"textAlign": "center"}),
]


def main():
    app_name = os.getenv("APP_NAME")
    debug_mode = os.getenv("DEBUG_MODE")
    local_host = os.getenv("HOST")
    local_port = os.getenv("PORT")
    print(f"APP_NAME: {app_name}")
    print(f"DEBUG_MODE: {debug_mode}")
    app.run(debug=debug_mode, host=local_host, port=local_port)


if __name__ == "__main__":
    main()
