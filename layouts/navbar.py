from dash import html
import dash_bootstrap_components as dbc

LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

# make a reuseable navitem for the different examples
navitem = [dbc.NavItem(dbc.NavLink("Home", href="/")),
            dbc.NavItem(dbc.NavLink("Sobre", href="/sobre"))]

navbar = dbc.Navbar([
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand(html.H5("Interaciômetro"), className="ml-2")),
                ],
                align="center",
                className="g-0",
            ),
            href="/",
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(
            dbc.Nav(
                navitem, className="ml-auto", navbar=True
            ),
            id="navbar-collapse",
            navbar=True,
        ),
    ],
    color="dark",
    dark=True,
    fixed=True
    # className="mb-5",
)