from dash import html
import dash_bootstrap_components as dbc

LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

# make a reuseable navitem for the different examples
navitem = [dbc.NavItem(dbc.NavLink("Home", href="/")),
            # dbc.NavItem(dbc.NavLink("Sobre", href="/sobre")),
        ]

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Interaciômetro", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                dbc.Nav(
                    navitem, className="ml-auto", navbar=True
                ),
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ],
        fluid=True
    ),
    color="dark",
    dark=True,
    fixed=True,
)