import flet as ft
import requests


def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def on_dropdown_change(e):
        if url_mode_switch.value:
            active_url = urls_list.value

    def on_url_field_submit(e):
        if not url_mode_switch.value:
            active_url = url_field.value

    def on_switch_change(e):
        if url_mode_switch.value:
            active_url = urls_list.value
        else:
            active_url = url_field.value

    def onButtonClick(e):
        text.value = 'request in progress'
        page.update()
        try:
            data = requests.get(
                urls_list.value, params=param_field.value, json=json_field.value).text
        except:
            data = 'An error has occured ...'
        text.value = f'{data}  {active_url}  {urls_list.value} {url_mode_switch.value}'
        page.update()

    url_field = ft.TextField(
        label='Url',
        value='https://www.httpbin.org/anything',
        on_submit=on_url_field_submit)

    param_field = ft.TextField(label='Params')
    json_field = ft.TextField(label='Json')
    url_mode_switch = ft.Switch(
        label='Url Mode', value=True, on_change=on_switch_change)
    urls_list = ft.Dropdown(width=300, options=[
        ft.dropdown.Option('https://httpbin.org/anything', text='httpbin'),
        ft.dropdown.Option('http://localhost:8080/api', text='local:8080'),
        ft.dropdown.Option('https://google.com', text='google')
    ], on_change=on_dropdown_change)
    active_url = url_field.value

    send_request_button = ft.FilledButton(text='send', on_click=onButtonClick)

    text = ft.Text(value='text is here ...')

    page.add(
        ft.Column(
            [
                ft.Row([url_field, param_field, json_field],
                       # alignment=ft.MainAxisAlignment.START,
                       # vertical_alignment=ft.CrossAxisAlignment.START
                       ),
                send_request_button,
                url_mode_switch,
                urls_list,
                text
            ],
        )
    )
    print(active_url)


ft.app(target=main, view=ft.WEB_BROWSER)
