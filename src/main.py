import flet as ft 

def line_chart():
    class State:
        toggle = True

    s = State()

    data_1 = [
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(1, 1),
                ft.LineChartDataPoint(3, 1.5),
                ft.LineChartDataPoint(5, 1.4),
                ft.LineChartDataPoint(7, 3.4),
                ft.LineChartDataPoint(10, 2),
                ft.LineChartDataPoint(12, 2.2),
                ft.LineChartDataPoint(13, 1.8),
            ],
            stroke_width=8,
            color=ft.colors.LIGHT_GREEN,
            curved=True,
            stroke_cap_round=True,
        ),
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(1, 1),
                ft.LineChartDataPoint(3, 2.8),
                ft.LineChartDataPoint(7, 1.2),
                ft.LineChartDataPoint(10, 2.8),
                ft.LineChartDataPoint(12, 2.6),
                ft.LineChartDataPoint(13, 3.9),
            ],
            color=ft.colors.PINK,
            below_line_bgcolor=ft.colors.with_opacity(0, ft.colors.PINK),
            stroke_width=8,
            curved=True,
            stroke_cap_round=True,
        ),
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(1, 2.8),
                ft.LineChartDataPoint(3, 1.9),
                ft.LineChartDataPoint(6, 3),
                ft.LineChartDataPoint(10, 1.3),
                ft.LineChartDataPoint(13, 2.5),
            ],
            color=ft.colors.CYAN,
            stroke_width=8,
            curved=True,
            stroke_cap_round=True,
        ),
    ]

    chart = ft.LineChart(
        data_series=data_1,
        border=ft.Border(
            bottom=ft.BorderSide(4, ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE))
        ),
        left_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=1,
                    label=ft.Text("0%", size=10, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=2,
                    label=ft.Text("20%", size=10, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=3,
                    label=ft.Text("40%", size=10, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=4,
                    label=ft.Text("60%", size=10, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=5,
                    label=ft.Text("80%", size=10, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=6,
                    label=ft.Text("100%", size=10, weight=ft.FontWeight.W_100),
                ),
            ],
            labels_size=60,
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=2,
                    label=ft.Container(
                        ft.Text(
                            "Mon",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=7,
                    label=ft.Container(
                        ft.Text(
                            "Tue",
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=12,
                    label=ft.Container(
                        ft.Text(
                            "Tue",
                            size=14,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
            ],
            labels_size=32,
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
        min_y=0,
        max_y=4,
        min_x=0,
        max_x=14,
        # animate=5000,
        # expand=True,
        # width=700,
        # height=500,
    )

    def toggle_data(e):
        if s.toggle:
            print('toggle')
        else:
            chart.data_series = data_1
            chart.max_y = 4
            chart.interactive = True
        s.toggle = not s.toggle
        chart.update()

    return ft.Column(
        controls=[ft.IconButton(ft.icons.REFRESH, on_click=toggle_data), chart],
    )

def example(page):
    def tabs_changed(e):
        print(f'Tab changed to {e.control.selected_index}')

    charts = ft.Tabs(
        selected_index=0,
        scrollable=False,
        expand=True,
        # on_change=tabs_changed,
        tabs=[
            ft.Tab(text='Crypto', content=line_chart()),
            ft.Tab(text='News', content= ft.ElevatedButton(text='Keep Reading'))
        ],
    )
    return ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[charts],
        )
    
async def manage_fab(e):
    print('FAB')                                                                                                                                                                                             

def main(page: ft.Page):
    page.title= 'BORSO'
    page.theme_mode= ft.ThemeMode.DARK
    
    # page.window_width = 390
    # page.window_height = 844

    # container_ref = ft.Ref[ft.Container]()

    page.floating_action_button = ft.FloatingActionButton(
        #text= str('+'),                                                                                                                                                                                                      
        icon= ft.Icons.AIRPLAY,
        on_click=manage_fab
    )

   

    container=ft.Container(
        ft.ElevatedButton(text="Say helo to QiMono")
    )     

    # page.add(example(page))
    page.add(ft.SafeArea(example(page), expand= True))
    # page.add(ft.SafeArea(container, expand= True))

ft.app(main)
