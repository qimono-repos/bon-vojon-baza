import flet as ft

async def main(page: ft.Page):
    page.theme_mode= ft.ThemeMode.LIGHT
    container_ref = ft.Ref[ft.Container]()

    async def manage_fab(e):
            print('FAB')

    page.floating_action_button = ft.FloatingActionButton(
        text= str('+'),
        icon=None,
        # ft.Icons.AIRPLAY,
        on_click=manage_fab
    )
    
    container=ft.Container(
        ft.Video(
            playlist=[
                ft.VideoMedia(resource='https://videos.pexels.com/video-files/3196600/3196600-uhd_2560_1440_25fps.mp4'),
                ],
                playlist_mode=ft.PlaylistMode.LOOP,
                fill_color=ft.colors.LIGHT_GREEN,
                aspect_ratio= 4/3,
                volume=100,
                autoplay=True,
                muted= False,
                show_controls= True,
                expand= True,
                on_error= lambda e: print('VIDEO ERROR', e.data),
                on_loaded= lambda e: print('LOAD VIDEO'),

            )
    
    )

    page.add(ft.SafeArea(container, expand= True))

ft.app(main)
