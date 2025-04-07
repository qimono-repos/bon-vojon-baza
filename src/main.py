import flet as ft
import flet.map as map

def main(page: ft.Page):
    def manage_tap(e: map.MapTapEvent):
        print(e)

    page.add(
            # map.Map(
            #     expand=True,
            #     on_init=lambda e: print("Map Init"),
            #     on_tap=manage_tap,
            #     layers=[
            #         map.TileLayer(
            #             url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png"
            #             )
            #         ]
            #     )
            # )

# counter = ft.Text("0", size=75, data=1337)

    # def increment_click(e):
    #     counter.data += 1
    #     counter.value = str(counter.data)
    #     counter.update()

    # page.floating_action_button = ft.FloatingActionButton(
    #     icon=ft.Icons.ADD, on_click=increment_click
    # )
    # page.add(
        ft.SafeArea(
            ft.Container(

                map.Map(
                    expand=True,
                    on_init=lambda e: print("Map Init"),
                    on_tap=manage_tap,
                    layers=[
                        map.TileLayer(
                            url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png"
                            )
                        ]
                    ),
                # counter,
                alignment=ft.alignment.center_left,
            ),
            expand=True,
        )
     )


ft.app(main)
