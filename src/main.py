import flet as ft
from flet.core.map.marker_layer import Marker
import flet.map as map

def main(page: ft.Page):

    def manage_fab(e):
            print('FAB')

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.AIRPLAY, on_click=manage_fab
    )
    
    marker_layer = map.MarkerLayer(markers=[])
    circle_layer_ref = ft.Ref[map.CircleLayer]()

    def manage_map_tap(e: map.MapTapEvent):
        #marker_layer_ref.current.markers = []
        print(e)
        if e.name == 'tap':
            marker_layer.markers.append(
                    map.Marker(
                        content= ft.Icon(
                            ft.Icons.LOCATION_ON, color= ft.cupertino_colors.DESTRUCTIVE_RED 
                            ),
                        coordinates= e.coordinates,
                        )
                    )
            page.update()
    
    def handle_map_event(e: map.MapEvent):
        print(e)

    page.add(
        ft.SafeArea(
            ft.Container(
                map.Map(
                    expand=True,
                    initial_center= map.MapLatitudeLongitude(-64,58),
                    initial_zoom= 3,
                    on_init=lambda e: print("New Map"),
                    on_tap=manage_map_tap,
                    #on_event= handle_map_event,
                    layers=[
                        map.TileLayer(
                            url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                            on_image_error= lambda e: print(e)),
                        
                        marker_layer,
                        map.SimpleAttribution(
                            text='By QiMono. ',
                            bgcolor=ft.colors.BLUE_GREY_50,
                            alignment= ft.alignment.bottom_left ,
                            on_click=lambda e: e.page.launch_url('https://qimono76.wordpress.com'),

                            ),
                        map.PolylineLayer(
                            polylines=[
                                map.PolylineMarker(
                                    border_stroke_width=3,
                                    border_color= ft.colors.PINK,
                                    # gradient_colors=[ft.colors.BLACK, ft.colors.BLACK],
                                    # color=ft.Colors.with_opacity(0.6, ft.colors.GREEN), 
                                    coordinates=[
                                        map.MapLatitudeLongitude(-32.9,-60.9),
                                        map.MapLatitudeLongitude(-34.9,-67.6),
                                        map.MapLatitudeLongitude(-38.9,-68.1),
                                        ]
                                    )
                                ]
                            ),

                        # map.RichAttribution(
                        #     alignment= ft.alignment.button_left,
                            # attributions=[
                            #     map.TextSourceAttribution(
                            #         prepend_copyright = False,
                            #         text='Powered by QiMono(TM)',
                            #         on_click=lambda e: e.page.launch_url('https://qimono76.wordpress.com'),
                            #         ),
                            #     ],
                            # )
                        ],
                    ),
                alignment=ft.alignment.center_left,
            ),
            expand=True,
        )
     )


ft.app(main)
