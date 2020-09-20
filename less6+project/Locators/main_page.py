from dataclasses import dataclass


@dataclass(frozen=True)
class MainPage:
    @dataclass(frozen=True)
    class NavTop:
        nav: str = '#top-links'
        phone: str = '#top-links > ul > li:nth-child(1)'
        my_account: str = '#top-links > ul > li:nth-child(2)'
        wish_list: str = '#top-links > ul > li:nth-child(3)'
        shopping_cart: str = '#top-links ul li:nth-child(4)'  # '#top-links ul .fa-shopping-cart'
        chekout: str = '#top-links > ul > li:nth-child(5)'

    @dataclass(frozen=True)
    class Currency:
        currency_button: str = '.btn-link'
        euro: str = '.btn-group ul [name=EUR]'
        pound_sterling: str = '.btn-group ul [name=GBP]'
        us_dollar: str = '.btn-group ul [name=USD]'

    @dataclass(frozen=True)
    class NavBar:
        navbar: str = '.navbar-collapse'
        desktops: str = '.navbar-collapse > ul > li:nth-child(1)'
        laptops_and_notebooks: str = '.navbar-collapse > ul > li:nth-child(2)'
        components: str = '.navbar-collapse > ul > li:nth-child(3)'
        tablets: str = '.navbar-collapse > ul > li:nth-child(4)'
        software: str = '.navbar-collapse > ul > li:nth-child(5)'
        phones_and_pdas: str = '.navbar-collapse > ul > li:nth-child(6)'
        cameras: str = '.navbar-collapse > ul > li:nth-child(7)'
        mp3_players: str = '.navbar-collapse > ul > li:nth-child(8)'

    @dataclass(frozen=True)
    class Search:
        search_field = '#search .form-control input-lg'
        search_button = '#search .input-group-btn'