import flet as ft
import json
from datetime import datetime
from pathlib import Path

class MapControl(ft.Control):
    def __init__(self):
        super().__init__()
        self.markers = []
        self.polylines = []
        self._map_initialized = False

    def _init_map(self):
        self.page.web.execute_js_async(f"""
            const map = L.map('map_{self.uid}').setView([-44, -65], 4.75);
            L.tileLayer('https://tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png').addTo(map);

            window.map_{self.uid} = map;
            window.markers_{self.uid} = [];
            window.polylines_{self.uid} = null;

            map.on('click', (e) => {{
                const event = {{
                    type: 'map_click',
                    latlng: e.latlng,
                        control_id: '{self.uid}'
                }};
                window.handleMapEvent(JSON.stringify(event));
            }});
        """)
        self._map_initialized = True

    def update_markers(self):
        if not self._map_initialized:
            return

        self.page.web.execute_js_async(f"""
            window.markers_{self.uid}.forEach(marker => map_{self.uid}.removeLayer(marker));
            window.markers_{self.uid} = [];

            {self._generate_marker_js()}
            if(window.polylines_{self.uid}) {{
                map_{self.uid}.removeLayer(window.polylines_{self.uid});
            }}
            {self._generate_polyline_js()}
        """)
    
    def _generate_marker_js(self):
        return "\n".join([
            f"""const marker_{i} = L.marker([{m['lat']}, {m['lng']}]).addTo(map_{self.uid});
            f"window.markers_{self.uid}.push(marker_{i});"""
            for i, m in enumerate(self.markers)
        ])

    def _generate_polyline_js(self):
        if len(self.markers) < 2:
            return ""

        coords = ",".join([f"[{m['lat']}, {m['lng']}]" for m in self.markers])
        return f"""
            window.polylines_{self.uid} = L.polyline([{coords}], {{color: '#ff69b4'}}).addTo(map_{self.uid});
        """

def main(page: ft.Page):
   
    page.platform = ft.PagePlatform.ANDROID
    page.web_renderer = ft.WebRenderer.CANVAS_KIT

    debug = ft.Text("Init...", color="red", size=24)
    page.add(debug)

    # try:
    #     page.update()
    # except Exception as e:
    #     debug.value = f"CRASH: {str(e)}"
    # raise

    page.title = "Bon Vojojn Baza"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0

    map_control = MapControl()

    def load_markers():
        try:
            save_path = Path.home() / "Documents" / "qimono_routes.json"
            if save_path.exists():
                with open(save_path, "r") as f:
                    map_control.markers = json.load(f)
                map_control.update_markers()
        except Exception as e:
            print(f"Load error: {e}")

    def save_markers(e):
        try:            
            save_path = Path.home() / "Documents" / "qimono_routes.json"
            with open(save_path, "w") as f:
                json.dump(map_control.markers, f)
            print("Markers saved!")
        except Exception as e:
            print(f"Save failed: {e}")

    def handle_map_event(e: ft.JsEvent):
        data = json.loads(e.data)
        if data['type'] == 'map_click' and data.get('control_id') == map_control.uid:
            map_control.markers.append({
                "lat": data['latlng']['lat'],
                "lng": data['latlng']['lng']
            })
            map_control.update_markers()
            page.update()

    page.add(
        ft.Stack([
            ft.Container(
                content=map_control,
                expand=True
            ),
            ft.FloatingActionButton(
                icon=ft.icons.SAVE,
                on_click=save_markers,
                bottom=20,
                right=20
            )
        ])
    )
    try:
        map_control._init_map()
        load_markers()

        page.web.register_js_event_handler_async("handleMapEvent", handle_map_event)

        # page.web.register_js_event_handler_async(
        #     event_name="handleMapEvent",
        #     handler=handle_map_event
        # )

        ft.app(target=main)
    #ft.app(target=main, view=ft.WEB_BROWSER)

    except Exception as e:
        debug.value = f"CRASH: {str(e)}"
    raise

