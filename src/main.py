import flet as ft

async def main(page: ft.Page):
    page.theme_mode= ft.ThemeMode.LIGHT
    container_ref = ft.Ref[ft.Container]()

    async def manage_fab(e):
        print('FAB')                                                                                                                                                                                             
        page.floating_action_button = ft.FloatingActionButton(
            text= str('+'),                                                                                                                                                                                                      icon=None,
            # ft.Icons.AIRPLAY,
            on_click=manage_fab
            )

    container=ft.Container(
        ft.ElevatedButton(text="Say helo to QiMono")
    )                                                                                                                                                                                                                
    page.add(ft.SafeArea(container, expand= True))

ft.app(main)
