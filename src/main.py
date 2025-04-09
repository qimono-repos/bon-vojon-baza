import flet as ft
from flet.core.map.marker_layer import Marker
import flet.map as map
from datetime import datetime
import os
import asyncio
import json
from pathlib import Path 

async def main(page: ft.Page):
    map_container_ref = ft.Ref[ft.Container]()
    marker_layer = map.MarkerLayer(markers=[])
    route_layer = map.PolylineLayer(polylines=[])
    save_path = None 
    circle_layer_ref = ft.Ref[map.CircleLayer]()

    async def take_screenshot():
        try:
            os.makedirs("screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshots/map_{timestamp}.png"

            # page.snack_bar= ft.SnackBar(ft.Text(f'Compartir Rutas'), action='OK')
            # page.snack_bar.open = True
            # await map_container_ref.current.screenshot_async(filename=filename)
            # await page.screenshot_async(filename=filename, control=map_container_ref.current)
            # await asyncio.to_thread(lambda: page.screenshot(filename=filename, source= map_container_ref.current))
            # page.take_screenshot(filename=filename, source= map_container_ref.current)

            print('SCREENSHOT')
            page.update()
        except Exception as e:
            print('EXCEPTION: taking screenshot ', e)

    async def manage_fab(e):
            print('FAB')
            await take_screenshot()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.AIRPLAY, on_click=manage_fab
    )
    
    async def get_save_path():
        nonlocal save_path
        if save_path is None:
            downloads_dir = str(Path.home() / "Documents")
        os.makedirs(str(Path.home() / 'Documents'), exist_ok=True)
        save_path= os.path.join(str(Path.home() / 'Documents'), 'qimono_document.json')
        # save_path= os.path.join(downloads_dir, 'qimono_document.json')
        return save_path 

    def update_polyline():
        coordinates= [m.coordinates for m in marker_layer.markers]

        if len(coordinates) >= 2:
            route_layer.polylines = [
                map.PolylineMarker(
                border_stroke_width=3,
                border_color=ft.colors.PINK,
                coordinates=coordinates
                )
            ]
        else:
            route_layer.polylines = []

    async def save_markers():
        try:
            file_path = await get_save_path()
            markers_list = [{
                "latitude": marker.coordinates.latitude,
                "longitude": marker.coordinates.longitude } for marker in marker_layer.markers ]
            with open(file_path, 'w') as f: 
                json.dump(markers_list, f)
            print(f'Markers saved to {file_path }')

        except Exception as e:
            print('ERROR saving maker ', e)

    async def load_markers():
        try:
            file_path= await get_save_path()
            if os.path.exists(file_path):
                with open(file_path, 'r') as f: 
                    markers_list= json.load(f)

                marker_layer.markers.clear()
                for item in markers_list:
                    marker_layer.markers.append(
                        map.Marker(
                            content= ft.Icon(ft.icons.LOCATION_ON, color= ft.colors.RED),
                            coordinates= map.MapLatitudeLongitude(item['latitude'], item['longitude'])
                        )
                    )
                update_polyline()
                page.update()

        except Exception as e:
            print('ERROR loading markers: ',e)

    async def manage_map_tap(e: map.MapTapEvent):
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
            update_polyline()
            await save_markers()
            page.update()
    
    def handle_map_event(e: map.MapEvent):
        print(e)

    # page.add(
    #     ft.SafeArea(
    map_container=ft.Container(
        map.Map(
            expand=True,
            initial_center= map.MapLatitudeLongitude(-44,-65),
            initial_zoom= 4.75,
            on_init=lambda e: print("New Map"),
            on_tap=manage_map_tap,
            ref= map_container_ref,
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
                route_layer,
                ],
            ),
            alignment=ft.alignment.center_left,
        )

    await load_markers()
    page.add(ft.SafeArea(map_container, expand= True))

ft.app(main)
