import flet as ft
from flet.core.map.marker_layer import Marker
import flet.map as map

def main(page: ft.Page):

    def manage_fab(e):
            print('FAB')

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=manage_fab
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
                    initial_center= map.MapLatitudeLongitude(34,58),
                    initial_zoom= 4.5,
                    on_init=lambda e: print("New Map"),
                    on_tap=manage_map_tap,
                    layers=[
                        map.TileLayer(url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png"),
                        marker_layer 
                        ],
                        
                    ),
                alignment=ft.alignment.center_left,
            ),
            expand=True,
        )
     )


ft.app(main)
