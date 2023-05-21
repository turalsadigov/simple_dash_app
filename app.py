import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1("Perfect Square Checker"),
        dcc.Input(
            id="number-input",
            type="number",
            placeholder="Enter a number",
            debounce=True,
        ),
        html.Div(id="result"),
    ]
)


@app.callback(
    dash.dependencies.Output("result", "children"),
    [dash.dependencies.Input("number-input", "value")],
)
def check_perfect_square(number):
    if number is not None:
        square_root = number**0.5
        if square_root == int(square_root):
            return f"{number} is a perfect square!"
        else:
            return f"{number} is not a perfect square."
    else:
        return ""


if __name__ == "__main__":
    app.run_server(debug=True)
